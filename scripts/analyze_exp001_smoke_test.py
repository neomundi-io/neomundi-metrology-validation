#!/usr/bin/env python3
"""
EXP-001 — Post-run analyzer
Version: v0.2

Purpose
-------
Analyze the completed EXP-001 smoke-test outputs without making any
additional API call.

This version implements a genuinely independent deterministic baseline.

The baseline decision is produced ONLY from:
- prompt
- response

It never receives:
- ground_truth_label
- final_label
- NeoMundi score
- NeoMundi classification
- reviewer labels

Ground truth is used only AFTER the baseline and NeoMundi decisions have
been produced, for evaluation and confusion-matrix calculation.

This script:
- verifies the frozen corpus SHA-256;
- reads the completed NeoMundi raw outputs;
- builds an independent deterministic baseline;
- compares NeoMundi with frozen ground truth;
- compares the deterministic baseline with frozen ground truth;
- calculates confusion matrices and technical metrics;
- generates the French EXP-001 report;
- hashes all produced artifacts.

This script does NOT:
- modify the frozen corpus;
- modify the frozen threshold;
- call NeoMundi;
- call any LLM;
- recalibrate MET-003;
- make any general scientific or commercial performance claim.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import statistics
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# =============================================================================
# EXPERIMENT CONSTANTS — FROZEN FOR EXP-001 v0.1
# =============================================================================

EXPERIMENT_ID = "EXP-001"
EXPERIMENT_VERSION = "v0.1"
ANALYZER_VERSION = "v0.2"
BASELINE_VERSION = "v0.1"
RUN_ID = "EXP001-SMOKE-RUN-001"

EXPECTED_CASE_COUNT = 20
EXPECTED_POSITIVE_COUNT = 10
EXPECTED_NEGATIVE_COUNT = 10

EXPECTED_CORPUS_SHA256 = (
    "bd9ac82fd53aab35fba15ff999033f894"
    "f69775d256940f27694677720174ce1"
)

METRIC_ID = "MET-003"
THRESHOLD_VALUE = 0.5
THRESHOLD_OPERATOR = ">="


# =============================================================================
# PATHS
# =============================================================================

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

EXPERIMENT_DIR = (
    REPOSITORY_ROOT
    / "experiments"
    / "EXP-001"
)

RESULTS_DIR = (
    REPOSITORY_ROOT
    / "results"
    / "EXP-001"
)

CORPUS_PATH = (
    EXPERIMENT_DIR
    / "EXP-001_smoke_test_20_cases_FR.csv"
)

MANIFEST_PATH = (
    EXPERIMENT_DIR
    / "EXP-001_smoke_test_run_manifest.json"
)

NEOMUNDI_OUTPUT_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_neomundi_outputs.csv"
)

ERROR_LOG_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_error_log.csv"
)

BASELINE_OUTPUT_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_baseline_outputs.csv"
)

CONFUSION_MATRIX_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_confusion_matrix.csv"
)

REPORT_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_report_FR.md"
)

HASH_MANIFEST_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_artifact_hashes.json"
)


# =============================================================================
# OUTPUT SCHEMAS
# =============================================================================

BASELINE_FIELDS = [
    "experiment_id",
    "experiment_version",
    "run_id",
    "case_id",
    "baseline_version",
    "baseline_method",
    "baseline_rule_id",
    "baseline_decision",
    "baseline_status",
    "baseline_reason",
    "reference_type",
    "reference_location",
    "reference_version",
]

CONFUSION_FIELDS = [
    "system",
    "result_type",
    "count",
    "definition",
]


# =============================================================================
# TEXT NORMALIZATION
# =============================================================================

def normalize_text(value: str) -> str:
    """
    Normalize text deterministically:
    - lowercase
    - remove accents
    - normalize apostrophes
    - collapse whitespace
    """

    value = value or ""

    normalized = unicodedata.normalize(
        "NFKD",
        value,
    )

    normalized = "".join(
        char
        for char in normalized
        if not unicodedata.combining(char)
    )

    normalized = normalized.lower()

    normalized = (
        normalized
        .replace("’", "'")
        .replace("œ", "oe")
    )

    normalized = re.sub(
        r"\s+",
        " ",
        normalized,
    ).strip()

    return normalized


# =============================================================================
# INDEPENDENT DETERMINISTIC BASELINE RULES
# =============================================================================

BASELINE_RULES: dict[str, dict[str, Any]] = {
    normalize_text(
        "Quelle est la capitale de la France ?"
    ): {
        "rule_id": "BASE-RULE-001",
        "correct_markers": [
            "paris",
        ],
        "incorrect_markers": [
            "lyon",
        ],
        "reason_correct": (
            "La réponse identifie Paris comme capitale de la France."
        ),
        "reason_incorrect": (
            "La réponse identifie Lyon comme capitale de la France."
        ),
    },

    normalize_text(
        "Combien font 2 plus 2 ?"
    ): {
        "rule_id": "BASE-RULE-002",
        "correct_markers": [
            "2 plus 2 font 4",
            "2 + 2 = 4",
        ],
        "incorrect_markers": [
            "2 plus 2 font 5",
            "2 + 2 = 5",
        ],
        "reason_correct": (
            "La réponse respecte la règle déterministe 2 + 2 = 4."
        ),
        "reason_incorrect": (
            "La réponse contredit la règle déterministe 2 + 2 = 4."
        ),
    },

    normalize_text(
        "Quelle planète est la plus proche du Soleil ?"
    ): {
        "rule_id": "BASE-RULE-003",
        "correct_markers": [
            "mercure",
        ],
        "incorrect_markers": [
            "venus",
        ],
        "reason_correct": (
            "La réponse identifie Mercure comme planète la plus proche du Soleil."
        ),
        "reason_incorrect": (
            "La réponse identifie Vénus à la place de Mercure."
        ),
    },

    normalize_text(
        "En quelle année a commencé la Seconde Guerre mondiale en Europe ?"
    ): {
        "rule_id": "BASE-RULE-004",
        "correct_markers": [
            "1939",
        ],
        "incorrect_markers": [
            "1941",
        ],
        "reason_correct": (
            "La réponse donne 1939 comme début de la Seconde Guerre mondiale "
            "en Europe."
        ),
        "reason_incorrect": (
            "La réponse donne 1941 à la place de 1939."
        ),
    },

    normalize_text(
        "Quel est le symbole chimique de l’eau ?"
    ): {
        "rule_id": "BASE-RULE-005",
        "correct_markers": [
            "h2o",
        ],
        "incorrect_markers": [
            "co2",
        ],
        "reason_correct": (
            "La réponse donne H2O pour l'eau."
        ),
        "reason_incorrect": (
            "La réponse donne CO2 à la place de H2O."
        ),
    },

    normalize_text(
        "Combien de côtés possède un triangle ?"
    ): {
        "rule_id": "BASE-RULE-006",
        "correct_markers": [
            "trois cotes",
            "3 cotes",
        ],
        "incorrect_markers": [
            "quatre cotes",
            "4 cotes",
        ],
        "reason_correct": (
            "La réponse indique qu'un triangle possède trois côtés."
        ),
        "reason_incorrect": (
            "La réponse indique qu'un triangle possède quatre côtés."
        ),
    },

    normalize_text(
        "Quel océan sépare principalement l’Europe de l’Amérique du Nord ?"
    ): {
        "rule_id": "BASE-RULE-007",
        "correct_markers": [
            "atlantique",
        ],
        "incorrect_markers": [
            "indien",
        ],
        "reason_correct": (
            "La réponse identifie l'océan Atlantique."
        ),
        "reason_incorrect": (
            "La réponse identifie l'océan Indien à la place de l'Atlantique."
        ),
    },

    normalize_text(
        "Quelle langue officielle est majoritairement utilisée au Brésil ?"
    ): {
        "rule_id": "BASE-RULE-008",
        "correct_markers": [
            "portugais",
        ],
        "incorrect_markers": [
            "espagnol",
        ],
        "reason_correct": (
            "La réponse identifie le portugais."
        ),
        "reason_incorrect": (
            "La réponse identifie l'espagnol à la place du portugais."
        ),
    },

    normalize_text(
        "Quel gaz les plantes absorbent-elles principalement pour la photosynthèse ?"
    ): {
        "rule_id": "BASE-RULE-009",
        "correct_markers": [
            "dioxyde de carbone",
            "co2",
        ],
        "incorrect_markers": [
            "oxygene",
        ],
        "reason_correct": (
            "La réponse identifie le dioxyde de carbone."
        ),
        "reason_incorrect": (
            "La réponse identifie l'oxygène à la place du dioxyde de carbone."
        ),
    },

    normalize_text(
        "Combien de minutes y a-t-il dans une heure ?"
    ): {
        "rule_id": "BASE-RULE-010",
        "correct_markers": [
            "60 minutes",
        ],
        "incorrect_markers": [
            "100 minutes",
        ],
        "reason_correct": (
            "La réponse respecte la conversion déterministe "
            "1 heure = 60 minutes."
        ),
        "reason_incorrect": (
            "La réponse donne 100 minutes à la place de 60."
        ),
    },
}


# =============================================================================
# GENERAL UTILITIES
# =============================================================================

def utc_now_iso() -> str:
    return datetime.now(
        timezone.utc
    ).isoformat().replace(
        "+00:00",
        "Z",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(1024 * 1024),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def safe_float(
    value: Any,
) -> float | None:

    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return None

    try:
        number = float(text)

    except (
        TypeError,
        ValueError,
    ):
        return None

    if not math.isfinite(number):
        return None

    return number


def division(
    numerator: float,
    denominator: float,
) -> float | None:

    if denominator == 0:
        return None

    return numerator / denominator


def pct(
    value: float | None,
) -> str:

    if value is None:
        return "N/A"

    return f"{value * 100:.2f} %"


def decimal(
    value: float | None,
) -> str:

    if value is None:
        return "N/A"

    return f"{value:.4f}"


def read_csv(
    path: Path,
) -> list[dict[str, str]]:

    if not path.exists():
        raise RuntimeError(
            f"Fichier introuvable : {path}"
        )

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        return list(
            csv.DictReader(handle)
        )


def write_csv(
    path: Path,
    fields: list[str],
    rows: list[dict[str, Any]],
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:

        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
        )

        writer.writeheader()
        writer.writerows(rows)


def load_manifest() -> dict[str, Any]:

    if not MANIFEST_PATH.exists():
        raise RuntimeError(
            f"Manifeste introuvable : {MANIFEST_PATH}"
        )

    with MANIFEST_PATH.open(
        "r",
        encoding="utf-8",
    ) as handle:
        return json.load(handle)


# =============================================================================
# INPUT VALIDATION
# =============================================================================

def verify_corpus() -> list[dict[str, str]]:

    actual_hash = sha256_file(
        CORPUS_PATH
    )

    if actual_hash != EXPECTED_CORPUS_SHA256:
        raise RuntimeError(
            "CORPUS HASH MISMATCH\n"
            f"Attendu : {EXPECTED_CORPUS_SHA256}\n"
            f"Réel    : {actual_hash}"
        )

    corpus = read_csv(
        CORPUS_PATH
    )

    if len(corpus) != EXPECTED_CASE_COUNT:
        raise RuntimeError(
            f"Corpus : {len(corpus)} cas, "
            f"{EXPECTED_CASE_COUNT} attendus."
        )

    ids = [
        row["case_id"]
        for row in corpus
    ]

    if len(ids) != len(set(ids)):
        raise RuntimeError(
            "Des case_id dupliqués existent dans le corpus."
        )

    positive_count = sum(
        row["ground_truth_label"] == "POSITIVE"
        for row in corpus
    )

    negative_count = sum(
        row["ground_truth_label"] == "NEGATIVE"
        for row in corpus
    )

    if positive_count != EXPECTED_POSITIVE_COUNT:
        raise RuntimeError(
            f"Nombre POSITIVE incorrect : {positive_count}"
        )

    if negative_count != EXPECTED_NEGATIVE_COUNT:
        raise RuntimeError(
            f"Nombre NEGATIVE incorrect : {negative_count}"
        )

    for row in corpus:

        case_id = row["case_id"]

        if row.get(
            "freeze_status"
        ) != "FROZEN":
            raise RuntimeError(
                f"{case_id}: corpus non gelé."
            )

        if row.get(
            "exclusion_status"
        ) != "INCLUDED":
            raise RuntimeError(
                f"{case_id}: cas non inclus."
            )

        if row.get(
            "final_label"
        ) != row.get(
            "ground_truth_label"
        ):
            raise RuntimeError(
                f"{case_id}: final_label différent "
                "de ground_truth_label."
            )

    return corpus


def verify_neomundi_outputs(
    corpus: list[dict[str, str]],
) -> list[dict[str, str]]:

    outputs = read_csv(
        NEOMUNDI_OUTPUT_PATH
    )

    if len(outputs) != EXPECTED_CASE_COUNT:
        raise RuntimeError(
            f"Sorties NeoMundi : {len(outputs)} lignes, "
            f"{EXPECTED_CASE_COUNT} attendues."
        )

    corpus_ids = {
        row["case_id"]
        for row in corpus
    }

    output_ids = [
        row["case_id"]
        for row in outputs
    ]

    if len(output_ids) != len(
        set(output_ids)
    ):
        raise RuntimeError(
            "Des case_id dupliqués existent "
            "dans les sorties NeoMundi."
        )

    if set(output_ids) != corpus_ids:

        missing = sorted(
            corpus_ids
            - set(output_ids)
        )

        unexpected = sorted(
            set(output_ids)
            - corpus_ids
        )

        raise RuntimeError(
            "Les case_id NeoMundi ne correspondent pas au corpus.\n"
            f"Absents : {missing}\n"
            f"Inattendus : {unexpected}"
        )

    for row in outputs:

        case_id = row["case_id"]

        if row.get(
            "experiment_id"
        ) != EXPERIMENT_ID:
            raise RuntimeError(
                f"{case_id}: mauvais experiment_id."
            )

        if row.get(
            "experiment_version"
        ) != EXPERIMENT_VERSION:
            raise RuntimeError(
                f"{case_id}: mauvaise experiment_version."
            )

        if row.get(
            "run_id"
        ) != RUN_ID:
            raise RuntimeError(
                f"{case_id}: mauvais run_id."
            )

        if row.get(
            "metric_id"
        ) != METRIC_ID:
            raise RuntimeError(
                f"{case_id}: mauvaise métrique."
            )

        threshold = safe_float(
            row.get(
                "threshold_value"
            )
        )

        if threshold != THRESHOLD_VALUE:
            raise RuntimeError(
                f"{case_id}: seuil différent de 0.5."
            )

        if row.get(
            "threshold_operator"
        ) != THRESHOLD_OPERATOR:
            raise RuntimeError(
                f"{case_id}: mauvais opérateur de seuil."
            )

    return outputs


# =============================================================================
# INDEPENDENT BASELINE ENGINE
# =============================================================================

def deterministic_baseline_decision(
    prompt: str,
    response: str,
) -> tuple[str, str, str]:
    """
    Produce the baseline decision using ONLY prompt + response.

    Returns:
        decision
        rule_id
        reason

    IMPORTANT:
    This function has no access to ground_truth_label or NeoMundi outputs.
    """

    normalized_prompt = normalize_text(
        prompt
    )

    normalized_response = normalize_text(
        response
    )

    rule = BASELINE_RULES.get(
        normalized_prompt
    )

    if rule is None:
        return (
            "UNDETERMINED",
            "NO_MATCHING_RULE",
            "Aucune règle déterministe gelée ne correspond au prompt.",
        )

    correct_markers = [
        normalize_text(marker)
        for marker in rule[
            "correct_markers"
        ]
    ]

    incorrect_markers = [
        normalize_text(marker)
        for marker in rule[
            "incorrect_markers"
        ]
    ]

    correct_found = any(
        marker in normalized_response
        for marker in correct_markers
    )

    incorrect_found = any(
        marker in normalized_response
        for marker in incorrect_markers
    )

    if correct_found and not incorrect_found:
        return (
            "FACTUALLY_CORRECT",
            rule["rule_id"],
            rule["reason_correct"],
        )

    if incorrect_found and not correct_found:
        return (
            "FACTUALLY_INCORRECT",
            rule["rule_id"],
            rule["reason_incorrect"],
        )

    if correct_found and incorrect_found:
        return (
            "UNDETERMINED",
            rule["rule_id"],
            (
                "La réponse contient simultanément un marqueur correct "
                "et un marqueur incorrect."
            ),
        )

    return (
        "UNDETERMINED",
        rule["rule_id"],
        (
            "La réponse ne correspond ni au marqueur correct "
            "ni au marqueur incorrect défini par la règle déterministe."
        ),
    )


def build_independent_baseline(
    corpus: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """
    Build the baseline WITHOUT passing ground truth to the decision function.
    """

    baseline_rows: list[
        dict[str, Any]
    ] = []

    for case in corpus:

        decision, rule_id, reason = (
            deterministic_baseline_decision(
                prompt=case["prompt"],
                response=case["response"],
            )
        )

        baseline_rows.append(
            {
                "experiment_id": EXPERIMENT_ID,
                "experiment_version": EXPERIMENT_VERSION,
                "run_id": RUN_ID,
                "case_id": case["case_id"],
                "baseline_version": BASELINE_VERSION,
                "baseline_method": (
                    "DETERMINISTIC_PROMPT_RESPONSE_RULES"
                ),
                "baseline_rule_id": rule_id,
                "baseline_decision": decision,
                "baseline_status": (
                    "CALCULATED"
                    if decision != "UNDETERMINED"
                    else "UNDETERMINED"
                ),
                "baseline_reason": reason,
                "reference_type": case.get(
                    "reference_type",
                    "",
                ),
                "reference_location": case.get(
                    "reference_location",
                    "",
                ),
                "reference_version": case.get(
                    "reference_version",
                    "",
                ),
            }
        )

    return baseline_rows


# =============================================================================
# GENERIC BINARY PERFORMANCE ENGINE
# =============================================================================

def calculate_binary_metrics(
    *,
    tp: int,
    fp: int,
    tn: int,
    fn: int,
    unavailable: int,
    errors: int,
) -> dict[str, Any]:

    classified = (
        tp
        + fp
        + tn
        + fn
    )

    precision = division(
        tp,
        tp + fp,
    )

    recall = division(
        tp,
        tp + fn,
    )

    specificity = division(
        tn,
        tn + fp,
    )

    false_positive_rate = division(
        fp,
        fp + tn,
    )

    false_negative_rate = division(
        fn,
        fn + tp,
    )

    if (
        precision is None
        or recall is None
        or precision + recall == 0
    ):
        f1 = None

    else:
        f1 = (
            2
            * precision
            * recall
            / (
                precision
                + recall
            )
        )

    accuracy = division(
        tp + tn,
        classified,
    )

    coverage = division(
        classified,
        EXPECTED_CASE_COUNT,
    )

    return {
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "classified": classified,
        "unavailable": unavailable,
        "errors": errors,
        "precision": precision,
        "recall": recall,
        "specificity": specificity,
        "false_positive_rate": false_positive_rate,
        "false_negative_rate": false_negative_rate,
        "f1": f1,
        "accuracy": accuracy,
        "coverage": coverage,
    }


# =============================================================================
# NEOMUNDI COMPARISON
# =============================================================================

def compare_neomundi(
    corpus: list[dict[str, str]],
    outputs: list[dict[str, str]],
) -> dict[str, Any]:

    truth_by_case = {
        row["case_id"]:
        row["ground_truth_label"]
        for row in corpus
    }

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    unavailable = 0
    computation_errors = 0

    calculated_scores: list[float] = []
    positive_scores: list[float] = []
    negative_scores: list[float] = []

    api_latencies: list[float] = []
    processing_times: list[float] = []

    measurement_versions: set[str] = set()
    normalizer_versions: set[str] = set()
    runner_versions: set[str] = set()
    github_run_ids: set[str] = set()
    github_run_attempts: set[str] = set()

    judge_models_configured: set[str] = set()
    judge_models_exposed: set[str] = set()

    fallback_statuses: set[str] = set()
    fallback_explicit_count = 0

    for output in outputs:

        case_id = output[
            "case_id"
        ]

        truth = truth_by_case[
            case_id
        ]

        signal = output.get(
            "experimental_signal_class",
            "",
        )

        calculation_status = output.get(
            "calculation_status",
            "",
        )

        score = safe_float(
            output.get(
                "factual_hallucination_score"
            )
        )

        if score is not None:

            calculated_scores.append(
                score
            )

            if truth == "POSITIVE":
                positive_scores.append(
                    score
                )

            elif truth == "NEGATIVE":
                negative_scores.append(
                    score
                )

        api_latency = safe_float(
            output.get(
                "api_latency_ms"
            )
        )

        if api_latency is not None:
            api_latencies.append(
                api_latency
            )

        processing_time = safe_float(
            output.get(
                "processing_time_ms"
            )
        )

        if processing_time is not None:
            processing_times.append(
                processing_time
            )

        for field, target in [
            (
                "measurement_version",
                measurement_versions,
            ),
            (
                "normalizer_version",
                normalizer_versions,
            ),
            (
                "runner_version",
                runner_versions,
            ),
            (
                "github_run_id",
                github_run_ids,
            ),
            (
                "github_run_attempt",
                github_run_attempts,
            ),
            (
                "judge_model_configured",
                judge_models_configured,
            ),
            (
                "judge_model_exposed_by_api",
                judge_models_exposed,
            ),
        ]:

            value = output.get(
                field,
                "",
            ).strip()

            if value:
                target.add(
                    value
                )

        fallback_status = output.get(
            "fallback_status",
            "",
        ).strip()

        if fallback_status:
            fallback_statuses.add(
                fallback_status
            )

        fallback_exposed = (
            output.get(
                "fallback_information_exposed_by_api",
                "",
            ).lower()
            == "true"
        )

        if fallback_exposed:
            fallback_explicit_count += 1

        if (
            calculation_status
            == "COMPUTATION_ERROR"
            or signal
            == "COMPUTATION_ERROR"
        ):
            computation_errors += 1

        elif signal == "SIGNAL_UNAVAILABLE":
            unavailable += 1

        elif (
            truth == "POSITIVE"
            and signal == "SIGNAL_POSITIVE"
        ):
            tp += 1

        elif (
            truth == "NEGATIVE"
            and signal == "SIGNAL_POSITIVE"
        ):
            fp += 1

        elif (
            truth == "NEGATIVE"
            and signal == "SIGNAL_NEGATIVE"
        ):
            tn += 1

        elif (
            truth == "POSITIVE"
            and signal == "SIGNAL_NEGATIVE"
        ):
            fn += 1

        else:
            raise RuntimeError(
                f"{case_id}: combinaison NeoMundi non reconnue "
                f"truth={truth}, signal={signal}"
            )

    metrics = calculate_binary_metrics(
        tp=tp,
        fp=fp,
        tn=tn,
        fn=fn,
        unavailable=unavailable,
        errors=computation_errors,
    )

    metrics.update(
        {
            "scores": calculated_scores,
            "positive_scores": positive_scores,
            "negative_scores": negative_scores,
            "api_latencies": api_latencies,
            "processing_times": processing_times,
            "measurement_versions": sorted(
                measurement_versions
            ),
            "normalizer_versions": sorted(
                normalizer_versions
            ),
            "runner_versions": sorted(
                runner_versions
            ),
            "github_run_ids": sorted(
                github_run_ids
            ),
            "github_run_attempts": sorted(
                github_run_attempts
            ),
            "judge_models_configured": sorted(
                judge_models_configured
            ),
            "judge_models_exposed": sorted(
                judge_models_exposed
            ),
            "fallback_statuses": sorted(
                fallback_statuses
            ),
            "fallback_explicit_count": (
                fallback_explicit_count
            ),
        }
    )

    return metrics


# =============================================================================
# BASELINE COMPARISON
# =============================================================================

def compare_baseline(
    corpus: list[dict[str, str]],
    baseline_rows: list[dict[str, Any]],
) -> dict[str, Any]:

    truth_by_case = {
        row["case_id"]:
        row["ground_truth_label"]
        for row in corpus
    }

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    undetermined = 0

    for row in baseline_rows:

        case_id = row[
            "case_id"
        ]

        truth = truth_by_case[
            case_id
        ]

        decision = row[
            "baseline_decision"
        ]

        if decision == "UNDETERMINED":
            undetermined += 1
            continue

        baseline_positive = (
            decision
            == "FACTUALLY_INCORRECT"
        )

        if (
            truth == "POSITIVE"
            and baseline_positive
        ):
            tp += 1

        elif (
            truth == "NEGATIVE"
            and baseline_positive
        ):
            fp += 1

        elif (
            truth == "NEGATIVE"
            and not baseline_positive
        ):
            tn += 1

        elif (
            truth == "POSITIVE"
            and not baseline_positive
        ):
            fn += 1

    return calculate_binary_metrics(
        tp=tp,
        fp=fp,
        tn=tn,
        fn=fn,
        unavailable=undetermined,
        errors=0,
    )


# =============================================================================
# CONFUSION MATRIX OUTPUT
# =============================================================================

def build_confusion_rows(
    neomundi: dict[str, Any],
    baseline: dict[str, Any],
) -> list[dict[str, Any]]:

    rows: list[
        dict[str, Any]
    ] = []

    for system, result in [
        (
            "NEOMUNDI_MET003",
            neomundi,
        ),
        (
            "DETERMINISTIC_BASELINE",
            baseline,
        ),
    ]:

        rows.extend(
            [
                {
                    "system": system,
                    "result_type": "VP",
                    "count": result["tp"],
                    "definition": (
                        "Vérité POSITIVE et classification positive"
                    ),
                },
                {
                    "system": system,
                    "result_type": "FP",
                    "count": result["fp"],
                    "definition": (
                        "Vérité NEGATIVE et classification positive"
                    ),
                },
                {
                    "system": system,
                    "result_type": "VN",
                    "count": result["tn"],
                    "definition": (
                        "Vérité NEGATIVE et classification négative"
                    ),
                },
                {
                    "system": system,
                    "result_type": "FN",
                    "count": result["fn"],
                    "definition": (
                        "Vérité POSITIVE et classification négative"
                    ),
                },
                {
                    "system": system,
                    "result_type": "UNAVAILABLE_OR_UNDETERMINED",
                    "count": result["unavailable"],
                    "definition": (
                        "Résultat indisponible ou baseline indéterminée"
                    ),
                },
                {
                    "system": system,
                    "result_type": "COMPUTATION_ERROR",
                    "count": result["errors"],
                    "definition": (
                        "Erreur technique de calcul"
                    ),
                },
            ]
        )

    return rows


# =============================================================================
# REPORT HELPERS
# =============================================================================

def mean_or_none(
    values: list[float],
) -> float | None:

    if not values:
        return None

    return statistics.mean(
        values
    )


def median_or_none(
    values: list[float],
) -> float | None:

    if not values:
        return None

    return statistics.median(
        values
    )


def min_or_none(
    values: list[float],
) -> float | None:

    if not values:
        return None

    return min(
        values
    )


def max_or_none(
    values: list[float],
) -> float | None:

    if not values:
        return None

    return max(
        values
    )


def render_list(
    values: list[str],
) -> str:

    if not values:
        return "non exposé / non disponible"

    return ", ".join(
        values
    )


# =============================================================================
# HASH MANIFEST
# =============================================================================

def build_hash_manifest(
    generated_at: str,
) -> dict[str, Any]:

    files = {
        "corpus": CORPUS_PATH,
        "neomundi_outputs": NEOMUNDI_OUTPUT_PATH,
        "error_log": ERROR_LOG_PATH,
        "baseline_outputs": BASELINE_OUTPUT_PATH,
        "confusion_matrix": CONFUSION_MATRIX_PATH,
    }

    hashes: dict[
        str,
        str,
    ] = {}

    for key, path in files.items():

        if not path.exists():
            raise RuntimeError(
                f"Impossible de hasher : {path}"
            )

        hashes[key] = sha256_file(
            path
        )

    return {
        "experiment_id": EXPERIMENT_ID,
        "experiment_version": EXPERIMENT_VERSION,
        "run_id": RUN_ID,
        "analyzer_version": ANALYZER_VERSION,
        "baseline_version": BASELINE_VERSION,
        "algorithm": "SHA-256",
        "generated_at": generated_at,
        "files": hashes,
    }


# =============================================================================
# REPORT
# =============================================================================

def build_report(
    neomundi: dict[str, Any],
    baseline: dict[str, Any],
    hashes: dict[str, str],
) -> str:

    technical_success = (
        neomundi["classified"]
        == EXPECTED_CASE_COUNT
        and neomundi["unavailable"] == 0
        and neomundi["errors"] == 0
    )

    technical_status = (
        "RÉUSSI"
        if technical_success
        else "À REVOIR"
    )

    positive_scores = neomundi[
        "positive_scores"
    ]

    negative_scores = neomundi[
        "negative_scores"
    ]

    api_latencies = neomundi[
        "api_latencies"
    ]

    processing_times = neomundi[
        "processing_times"
    ]

    return f"""# EXP-001 — Rapport du smoke test

## 1. Identification

- **Expérience :** `{EXPERIMENT_ID}`
- **Version :** `{EXPERIMENT_VERSION}`
- **Run :** `{RUN_ID}`
- **Analyseur :** `{ANALYZER_VERSION}`
- **Baseline :** `{BASELINE_VERSION}`
- **Métrique :** `{METRIC_ID}`
- **Seuil expérimental gelé :** `{THRESHOLD_OPERATOR} {THRESHOLD_VALUE}`
- **Date de génération :** `{utc_now_iso()}`
- **Statut technique :** **{technical_status}**

---

## 2. Objet

EXP-001 est un smoke test technique et méthodologique sur un corpus synthétique gelé de 20 cas.

Il vise à vérifier le fonctionnement de la chaîne expérimentale, la séparation des responsabilités et la production d'artefacts reproductibles.

Il ne constitue pas une validation scientifique générale de `MET-003`.

---

## 3. Séparation méthodologique

Trois niveaux sont maintenus séparément :

1. **vérité terrain gelée** ;
2. **baseline déterministe indépendante** ;
3. **signal NeoMundi MET-003**.

La baseline est calculée avant toute comparaison avec la vérité terrain.

Sa fonction de décision reçoit uniquement :

- `prompt`
- `response`

Elle ne reçoit jamais :

- `ground_truth_label`
- `final_label`
- score NeoMundi
- classification NeoMundi
- labels des évaluateurs.

---

## 4. Corpus

- **Cas :** {EXPECTED_CASE_COUNT}
- **POSITIVE :** {EXPECTED_POSITIVE_COUNT}
- **NEGATIVE :** {EXPECTED_NEGATIVE_COUNT}
- **SHA-256 :** `{EXPECTED_CORPUS_SHA256}`

---

## 5. Baseline déterministe indépendante

Méthode :

`DETERMINISTIC_PROMPT_RESPONSE_RULES`

La baseline contient dix règles déterministes correspondant aux dix familles de faits fermés du corpus.

### Résultats baseline

- **VP :** {baseline["tp"]}
- **FP :** {baseline["fp"]}
- **VN :** {baseline["tn"]}
- **FN :** {baseline["fn"]}
- **Indéterminés :** {baseline["unavailable"]}
- **Couverture :** {pct(baseline["coverage"])}
- **Précision :** {pct(baseline["precision"])}
- **Rappel :** {pct(baseline["recall"])}
- **Spécificité :** {pct(baseline["specificity"])}
- **F1 :** {decimal(baseline["f1"])}

Ces résultats concernent uniquement la baseline déterministe sur ce corpus contrôlé.

---

## 6. Résultats NeoMundi MET-003

- **VP :** {neomundi["tp"]}
- **FP :** {neomundi["fp"]}
- **VN :** {neomundi["tn"]}
- **FN :** {neomundi["fn"]}
- **Signaux indisponibles :** {neomundi["unavailable"]}
- **Erreurs de calcul :** {neomundi["errors"]}
- **Couverture :** {pct(neomundi["coverage"])}

### Métriques descriptives

- **Précision :** {pct(neomundi["precision"])}
- **Rappel :** {pct(neomundi["recall"])}
- **Spécificité :** {pct(neomundi["specificity"])}
- **Taux de faux positifs :** {pct(neomundi["false_positive_rate"])}
- **Taux de faux négatifs :** {pct(neomundi["false_negative_rate"])}
- **F1 :** {decimal(neomundi["f1"])}
- **Accuracy descriptive :** {pct(neomundi["accuracy"])}

Ces valeurs décrivent uniquement les 20 cas synthétiques gelés.

Elles ne constituent pas une estimation généralisable de performance.

---

## 7. Distribution de MET-003

### Cas POSITIVE

- **n :** {len(positive_scores)}
- **minimum :** {decimal(min_or_none(positive_scores))}
- **maximum :** {decimal(max_or_none(positive_scores))}
- **moyenne :** {decimal(mean_or_none(positive_scores))}
- **médiane :** {decimal(median_or_none(positive_scores))}

### Cas NEGATIVE

- **n :** {len(negative_scores)}
- **minimum :** {decimal(min_or_none(negative_scores))}
- **maximum :** {decimal(max_or_none(negative_scores))}
- **moyenne :** {decimal(mean_or_none(negative_scores))}
- **médiane :** {decimal(median_or_none(negative_scores))}

---

## 8. Environnement observé

- **Runner version :** {render_list(neomundi["runner_versions"])}
- **GitHub run ID :** {render_list(neomundi["github_run_ids"])}
- **GitHub run attempt :** {render_list(neomundi["github_run_attempts"])}
- **Measurement version :** {render_list(neomundi["measurement_versions"])}
- **Normalizer version :** {render_list(neomundi["normalizer_versions"])}
- **Juge configuré :** {render_list(neomundi["judge_models_configured"])}
- **Juge exposé par l'API :** {render_list(neomundi["judge_models_exposed"])}

---

## 9. Fallback

- **Fallbacks explicitement exposés :** {neomundi["fallback_explicit_count"]}
- **Statuts observés :** {render_list(neomundi["fallback_statuses"])}

`UNKNOWN_NOT_EXPOSED` signifie uniquement que l'API n'a pas exposé cette information.

Il ne signifie pas `NO_FALLBACK`.

---

## 10. Latence

### Latence côté runner

- **n :** {len(api_latencies)}
- **minimum :** {decimal(min_or_none(api_latencies))} ms
- **maximum :** {decimal(max_or_none(api_latencies))} ms
- **moyenne :** {decimal(mean_or_none(api_latencies))} ms
- **médiane :** {decimal(median_or_none(api_latencies))} ms

### Processing time API

- **n :** {len(processing_times)}
- **minimum :** {decimal(min_or_none(processing_times))} ms
- **maximum :** {decimal(max_or_none(processing_times))} ms
- **moyenne :** {decimal(mean_or_none(processing_times))} ms
- **médiane :** {decimal(median_or_none(processing_times))} ms

Ces valeurs sont descriptives du run et ne constituent pas un benchmark d'infrastructure.

---

## 11. Traçabilité

Algorithme :

`SHA-256`

- **Corpus :** `{hashes.get("corpus", "")}`
- **Sorties NeoMundi :** `{hashes.get("neomundi_outputs", "")}`
- **Journal d'erreurs :** `{hashes.get("error_log", "")}`
- **Baseline :** `{hashes.get("baseline_outputs", "")}`
- **Matrice de confusion :** `{hashes.get("confusion_matrix", "")}`

---

## 12. Conclusion technique

Statut :

**{technical_status}**

Le smoke test confirme uniquement que la chaîne expérimentale EXP-001 fonctionne techniquement sur le corpus synthétique contrôlé si :

- les 20 cas sont traités ;
- le corpus reste identique à son hash gelé ;
- les sorties sont reliées aux `case_id` ;
- la baseline est calculée indépendamment ;
- les erreurs et indisponibilités sont explicitement tracées ;
- la matrice de confusion est calculable ;
- les artefacts sont hashables.

---

## 13. Non-claims

EXP-001 ne permet pas d'affirmer :

- que `MET-003` est scientifiquement validé ;
- que le seuil `0.5` est optimal ;
- que les performances observées sont généralisables ;
- que le corpus représente une prévalence réelle ;
- qu'une absence d'alerte prouve qu'une réponse est vraie ;
- qu'une alerte constitue une preuve indépendante de fausseté ;
- qu'aucun fallback n'a eu lieu lorsque l'information n'est pas exposée ;
- qu'un claim commercial général peut être dérivé de ce smoke test.

---

## 14. Étape suivante

Effectuer la revue humaine post-run des résultats sans modifier :

- le corpus ;
- la vérité terrain ;
- la baseline ;
- le seuil ;
- le protocole ;
- les sorties brutes NeoMundi.

Après cette revue, décider soit :

1. de clôturer EXP-001 comme smoke test techniquement réussi ;
2. de corriger un problème de chaîne identifié ;
3. de préparer une expérience suivante sur un corpus plus large et plus difficile.
"""


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:

    print("=" * 72)
    print("NeoMundi Metrology Validation")
    print(
        f"EXP-001 — Post-run Analyzer {ANALYZER_VERSION}"
    )
    print("=" * 72)
    print()

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # -------------------------------------------------------------------------
    # 1. Frozen corpus
    # -------------------------------------------------------------------------

    print(
        "[1/8] Vérification du corpus gelé..."
    )

    corpus = verify_corpus()

    print(
        f"      OK — {len(corpus)} cas"
    )

    # -------------------------------------------------------------------------
    # 2. NeoMundi outputs
    # -------------------------------------------------------------------------

    print(
        "[2/8] Vérification des sorties NeoMundi..."
    )

    outputs = verify_neomundi_outputs(
        corpus
    )

    print(
        f"      OK — {len(outputs)} sorties"
    )

    # -------------------------------------------------------------------------
    # 3. Independent baseline
    # -------------------------------------------------------------------------

    print(
        "[3/8] Exécution de la baseline déterministe indépendante..."
    )

    baseline_rows = (
        build_independent_baseline(
            corpus
        )
    )

    write_csv(
        BASELINE_OUTPUT_PATH,
        BASELINE_FIELDS,
        baseline_rows,
    )

    baseline_undetermined = sum(
        row[
            "baseline_decision"
        ] == "UNDETERMINED"
        for row in baseline_rows
    )

    print(
        f"      OK — {len(baseline_rows)} décisions, "
        f"{baseline_undetermined} indéterminée(s)"
    )

    # -------------------------------------------------------------------------
    # 4. Comparisons
    # -------------------------------------------------------------------------

    print(
        "[4/8] Comparaison avec la vérité terrain..."
    )

    neomundi_result = compare_neomundi(
        corpus,
        outputs,
    )

    baseline_result = compare_baseline(
        corpus,
        baseline_rows,
    )

    print(
        "      NeoMundi : "
        f"VP={neomundi_result['tp']} "
        f"FP={neomundi_result['fp']} "
        f"VN={neomundi_result['tn']} "
        f"FN={neomundi_result['fn']}"
    )

    print(
        "      Baseline : "
        f"VP={baseline_result['tp']} "
        f"FP={baseline_result['fp']} "
        f"VN={baseline_result['tn']} "
        f"FN={baseline_result['fn']}"
    )

    # -------------------------------------------------------------------------
    # 5. Confusion matrices
    # -------------------------------------------------------------------------

    print(
        "[5/8] Génération des matrices de confusion..."
    )

    confusion_rows = (
        build_confusion_rows(
            neomundi_result,
            baseline_result,
        )
    )

    write_csv(
        CONFUSION_MATRIX_PATH,
        CONFUSION_FIELDS,
        confusion_rows,
    )

    print(
        f"      OK — {CONFUSION_MATRIX_PATH}"
    )

    # -------------------------------------------------------------------------
    # 6. Hashes before report
    # -------------------------------------------------------------------------

    print(
        "[6/8] Calcul des hashes..."
    )

    generated_at = utc_now_iso()

    hash_manifest = (
        build_hash_manifest(
            generated_at
        )
    )

    hashes = hash_manifest[
        "files"
    ]

    print(
        "      OK"
    )

    # -------------------------------------------------------------------------
    # 7. Report
    # -------------------------------------------------------------------------

    print(
        "[7/8] Génération du rapport FR..."
    )

    report = build_report(
        neomundi_result,
        baseline_result,
        hashes,
    )

    REPORT_PATH.write_text(
        report,
        encoding="utf-8",
    )

    report_hash = sha256_file(
        REPORT_PATH
    )

    hash_manifest[
        "files"
    ][
        "report_fr"
    ] = report_hash

    HASH_MANIFEST_PATH.write_text(
        json.dumps(
            hash_manifest,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        f"      OK — {REPORT_PATH}"
    )

    # -------------------------------------------------------------------------
    # 8. Final summary
    # -------------------------------------------------------------------------

    print(
        "[8/8] Résumé"
    )

    print()
    print("      NeoMundi")
    print(
        f"        VP          : {neomundi_result['tp']}"
    )
    print(
        f"        FP          : {neomundi_result['fp']}"
    )
    print(
        f"        VN          : {neomundi_result['tn']}"
    )
    print(
        f"        FN          : {neomundi_result['fn']}"
    )
    print(
        f"        Couverture  : {pct(neomundi_result['coverage'])}"
    )

    print()
    print("      Baseline indépendante")
    print(
        f"        VP          : {baseline_result['tp']}"
    )
    print(
        f"        FP          : {baseline_result['fp']}"
    )
    print(
        f"        VN          : {baseline_result['tn']}"
    )
    print(
        f"        FN          : {baseline_result['fn']}"
    )
    print(
        f"        Indéterminés: {baseline_result['unavailable']}"
    )
    print(
        f"        Couverture  : {pct(baseline_result['coverage'])}"
    )

    print()

    technical_success = (
        neomundi_result[
            "classified"
        ]
        == EXPECTED_CASE_COUNT
        and neomundi_result[
            "unavailable"
        ]
        == 0
        and neomundi_result[
            "errors"
        ]
        == 0
    )

    baseline_complete = (
        baseline_result[
            "classified"
        ]
        == EXPECTED_CASE_COUNT
        and baseline_result[
            "unavailable"
        ]
        == 0
    )

    if not technical_success:
        print(
            "ANALYSIS COMPLETED WITH NEOMUNDI TECHNICAL ISSUES",
            file=sys.stderr,
        )
        return 2

    if not baseline_complete:
        print(
            "ANALYSIS COMPLETED WITH BASELINE UNDETERMINED CASES",
            file=sys.stderr,
        )
        return 3

    print(
        "ANALYSIS COMPLETED — "
        "NeoMundi and independent baseline are analyzable."
    )

    print(
        "No general scientific or commercial performance claim "
        "is authorized from this 20-case corpus."
    )

    return 0


if __name__ == "__main__":

    try:
        sys.exit(
            main()
        )

    except KeyboardInterrupt:

        print(
            "\nAnalyse interrompue manuellement.",
            file=sys.stderr,
        )

        sys.exit(
            130
        )

    except Exception as exc:

        print(
            "\nANALYSIS FAILED",
            file=sys.stderr,
        )

        print(
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )

        sys.exit(
            1
        )
