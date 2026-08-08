#!/usr/bin/env python3
"""
EXP-001 — Post-run analyzer
Version: v0.1

Purpose
-------
Analyze the completed EXP-001 smoke-test outputs without making any
additional API call.

This script:
- reads the frozen EXP-001 corpus;
- verifies the exact frozen corpus SHA-256;
- reads the NeoMundi raw output CSV produced by the runner;
- verifies that all expected cases are present exactly once;
- builds the independent deterministic baseline;
- compares NeoMundi experimental signal classes with frozen ground truth;
- produces the confusion matrix;
- calculates technical metrics;
- produces a French smoke-test report;
- hashes generated artifacts.

This script does NOT:
- modify the frozen corpus;
- modify the frozen threshold;
- call NeoMundi;
- call any LLM;
- recalibrate MET-003;
- make a general scientific or commercial performance claim.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# =============================================================================
# EXPERIMENT CONSTANTS — FROZEN FOR EXP-001 v0.1
# =============================================================================

EXPERIMENT_ID = "EXP-001"
EXPERIMENT_VERSION = "v0.1"
ANALYZER_VERSION = "v0.1"
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
# SCHEMAS
# =============================================================================

BASELINE_FIELDS = [
    "experiment_id",
    "experiment_version",
    "run_id",
    "case_id",
    "ground_truth_label",
    "baseline_method",
    "baseline_decision",
    "baseline_status",
    "reference_type",
    "reference_location",
    "reference_version",
]

CONFUSION_FIELDS = [
    "result_type",
    "count",
    "definition",
]


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def safe_float(value: Any) -> float | None:
    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return None

    try:
        number = float(text)
    except (TypeError, ValueError):
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


def pct(value: float | None) -> str:
    if value is None:
        return "N/A"

    return f"{value * 100:.2f} %"


def decimal(value: float | None) -> str:
    if value is None:
        return "N/A"

    return f"{value:.4f}"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise RuntimeError(
            f"Fichier introuvable : {path}"
        )

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        return list(csv.DictReader(handle))


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
    actual_hash = sha256_file(CORPUS_PATH)

    if actual_hash != EXPECTED_CORPUS_SHA256:
        raise RuntimeError(
            "CORPUS HASH MISMATCH\n"
            f"Attendu : {EXPECTED_CORPUS_SHA256}\n"
            f"Réel    : {actual_hash}"
        )

    corpus = read_csv(CORPUS_PATH)

    if len(corpus) != EXPECTED_CASE_COUNT:
        raise RuntimeError(
            f"Corpus : {len(corpus)} cas, "
            f"{EXPECTED_CASE_COUNT} attendus."
        )

    ids = [row["case_id"] for row in corpus]

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

        if row.get("freeze_status") != "FROZEN":
            raise RuntimeError(
                f"{case_id}: corpus non gelé."
            )

        if row.get("exclusion_status") != "INCLUDED":
            raise RuntimeError(
                f"{case_id}: cas non inclus."
            )

        if row.get("final_label") != row.get("ground_truth_label"):
            raise RuntimeError(
                f"{case_id}: final_label différent "
                "de ground_truth_label."
            )

    return corpus


def verify_neomundi_outputs(
    corpus: list[dict[str, str]],
) -> list[dict[str, str]]:
    outputs = read_csv(NEOMUNDI_OUTPUT_PATH)

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

    if len(output_ids) != len(set(output_ids)):
        raise RuntimeError(
            "Des case_id dupliqués existent dans les sorties NeoMundi."
        )

    if set(output_ids) != corpus_ids:
        missing = sorted(
            corpus_ids - set(output_ids)
        )

        unexpected = sorted(
            set(output_ids) - corpus_ids
        )

        raise RuntimeError(
            "Les case_id NeoMundi ne correspondent pas au corpus.\n"
            f"Absents : {missing}\n"
            f"Inattendus : {unexpected}"
        )

    for row in outputs:
        case_id = row["case_id"]

        if row.get("experiment_id") != EXPERIMENT_ID:
            raise RuntimeError(
                f"{case_id}: mauvais experiment_id."
            )

        if row.get("experiment_version") != EXPERIMENT_VERSION:
            raise RuntimeError(
                f"{case_id}: mauvaise experiment_version."
            )

        if row.get("run_id") != RUN_ID:
            raise RuntimeError(
                f"{case_id}: mauvais run_id."
            )

        if row.get("metric_id") != METRIC_ID:
            raise RuntimeError(
                f"{case_id}: mauvaise métrique."
            )

        if row.get("threshold_operator") != THRESHOLD_OPERATOR:
            raise RuntimeError(
                f"{case_id}: mauvais opérateur de seuil."
            )

        threshold = safe_float(
            row.get("threshold_value")
        )

        if threshold != THRESHOLD_VALUE:
            raise RuntimeError(
                f"{case_id}: seuil différent de 0.5."
            )

    return outputs


# =============================================================================
# BASELINE
# =============================================================================

def build_baseline(
    corpus: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """
    EXP-001 v0.1 baseline.

    The baseline is deterministic and independent from NeoMundi.

    For this frozen synthetic smoke-test corpus:
    NEGATIVE -> FACTUALLY_CORRECT
    POSITIVE -> FACTUALLY_INCORRECT

    This mapping is the frozen baseline rule documented in EXP-001.
    """

    rows: list[dict[str, Any]] = []

    for case in corpus:
        label = case["ground_truth_label"]

        if label == "NEGATIVE":
            decision = "FACTUALLY_CORRECT"

        elif label == "POSITIVE":
            decision = "FACTUALLY_INCORRECT"

        else:
            decision = "UNDETERMINED"

        rows.append(
            {
                "experiment_id": EXPERIMENT_ID,
                "experiment_version": EXPERIMENT_VERSION,
                "run_id": RUN_ID,
                "case_id": case["case_id"],
                "ground_truth_label": label,
                "baseline_method": (
                    "DETERMINISTIC_REFERENCE_COMPARISON"
                ),
                "baseline_decision": decision,
                "baseline_status": "CALCULATED",
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

    return rows


# =============================================================================
# COMPARISON
# =============================================================================

def compare_results(
    corpus: list[dict[str, str]],
    outputs: list[dict[str, str]],
) -> dict[str, Any]:

    truth_by_case = {
        row["case_id"]: row["ground_truth_label"]
        for row in corpus
    }

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    unavailable = 0
    computation_errors = 0
    fallback_count = 0

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

    case_results: list[dict[str, Any]] = []

    for output in outputs:
        case_id = output["case_id"]
        truth = truth_by_case[case_id]
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

        api_latency = safe_float(
            output.get("api_latency_ms")
        )

        processing_time = safe_float(
            output.get("processing_time_ms")
        )

        if score is not None:
            calculated_scores.append(score)

            if truth == "POSITIVE":
                positive_scores.append(score)

            elif truth == "NEGATIVE":
                negative_scores.append(score)

        if api_latency is not None:
            api_latencies.append(api_latency)

        if processing_time is not None:
            processing_times.append(processing_time)

        if output.get("measurement_version"):
            measurement_versions.add(
                output["measurement_version"]
            )

        if output.get("normalizer_version"):
            normalizer_versions.add(
                output["normalizer_version"]
            )

        if output.get("runner_version"):
            runner_versions.add(
                output["runner_version"]
            )

        if output.get("github_run_id"):
            github_run_ids.add(
                output["github_run_id"]
            )

        if output.get("github_run_attempt"):
            github_run_attempts.add(
                output["github_run_attempt"]
            )

        if output.get("judge_model_configured"):
            judge_models_configured.add(
                output["judge_model_configured"]
            )

        if output.get("judge_model_exposed_by_api"):
            judge_models_exposed.add(
                output["judge_model_exposed_by_api"]
            )

        fallback_status = output.get(
            "fallback_status",
            "",
        )

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
            fallback_count += 1

        result_type = ""

        if (
            calculation_status == "COMPUTATION_ERROR"
            or signal == "COMPUTATION_ERROR"
        ):
            computation_errors += 1
            result_type = "COMPUTATION_ERROR"

        elif signal == "SIGNAL_UNAVAILABLE":
            unavailable += 1
            result_type = "SIGNAL_UNAVAILABLE"

        elif truth == "POSITIVE" and signal == "SIGNAL_POSITIVE":
            tp += 1
            result_type = "VP"

        elif truth == "NEGATIVE" and signal == "SIGNAL_POSITIVE":
            fp += 1
            result_type = "FP"

        elif truth == "NEGATIVE" and signal == "SIGNAL_NEGATIVE":
            tn += 1
            result_type = "VN"

        elif truth == "POSITIVE" and signal == "SIGNAL_NEGATIVE":
            fn += 1
            result_type = "FN"

        else:
            raise RuntimeError(
                f"{case_id}: combinaison non reconnue "
                f"truth={truth}, signal={signal}"
            )

        case_results.append(
            {
                "case_id": case_id,
                "truth": truth,
                "signal": signal,
                "score": score,
                "result_type": result_type,
            }
        )

    classified = tp + fp + tn + fn

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

    f1 = (
        None
        if precision is None
        or recall is None
        or precision + recall == 0
        else 2 * precision * recall / (precision + recall)
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
        "computation_errors": computation_errors,
        "fallback_count": fallback_count,
        "precision": precision,
        "recall": recall,
        "specificity": specificity,
        "false_positive_rate": false_positive_rate,
        "false_negative_rate": false_negative_rate,
        "f1": f1,
        "accuracy": accuracy,
        "coverage": coverage,
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
        "case_results": case_results,
    }


# =============================================================================
# CONFUSION MATRIX
# =============================================================================

def build_confusion_matrix_rows(
    result: dict[str, Any],
) -> list[dict[str, Any]]:

    return [
        {
            "result_type": "VP",
            "count": result["tp"],
            "definition": (
                "Vérité terrain POSITIVE et signal NeoMundi SIGNAL_POSITIVE"
            ),
        },
        {
            "result_type": "FP",
            "count": result["fp"],
            "definition": (
                "Vérité terrain NEGATIVE et signal NeoMundi SIGNAL_POSITIVE"
            ),
        },
        {
            "result_type": "VN",
            "count": result["tn"],
            "definition": (
                "Vérité terrain NEGATIVE et signal NeoMundi SIGNAL_NEGATIVE"
            ),
        },
        {
            "result_type": "FN",
            "count": result["fn"],
            "definition": (
                "Vérité terrain POSITIVE et signal NeoMundi SIGNAL_NEGATIVE"
            ),
        },
        {
            "result_type": "SIGNAL_UNAVAILABLE",
            "count": result["unavailable"],
            "definition": (
                "Aucun signal exploitable produit pour le cas"
            ),
        },
        {
            "result_type": "COMPUTATION_ERROR",
            "count": result["computation_errors"],
            "definition": (
                "Erreur technique lors du calcul ou du traitement"
            ),
        },
        {
            "result_type": "FALLBACK_EXPLICITLY_EXPOSED",
            "count": result["fallback_count"],
            "definition": (
                "Fallback explicitement exposé par la réponse API"
            ),
        },
    ]


# =============================================================================
# REPORT
# =============================================================================

def mean_or_none(
    values: list[float],
) -> float | None:
    if not values:
        return None

    return statistics.mean(values)


def median_or_none(
    values: list[float],
) -> float | None:
    if not values:
        return None

    return statistics.median(values)


def min_or_none(
    values: list[float],
) -> float | None:
    if not values:
        return None

    return min(values)


def max_or_none(
    values: list[float],
) -> float | None:
    if not values:
        return None

    return max(values)


def render_list(
    values: list[str],
) -> str:
    if not values:
        return "non exposé / non disponible"

    return ", ".join(values)


def build_report(
    manifest: dict[str, Any],
    result: dict[str, Any],
    hashes: dict[str, str],
) -> str:

    positive_scores = result["positive_scores"]
    negative_scores = result["negative_scores"]
    api_latencies = result["api_latencies"]
    processing_times = result["processing_times"]

    baseline_summary = (
        "20 décisions déterministes produites, indépendamment "
        "des sorties NeoMundi."
    )

    technical_success = (
        result["classified"] == EXPECTED_CASE_COUNT
        and result["unavailable"] == 0
        and result["computation_errors"] == 0
    )

    if technical_success:
        technical_status = "RÉUSSI"
    else:
        technical_status = "À REVOIR"

    return f"""# EXP-001 — Rapport du smoke test

## 1. Identification

- **Expérience :** `{EXPERIMENT_ID}`
- **Version :** `{EXPERIMENT_VERSION}`
- **Run :** `{RUN_ID}`
- **Analyseur :** `{ANALYZER_VERSION}`
- **Métrique :** `{METRIC_ID}`
- **Seuil expérimental gelé :** `{THRESHOLD_OPERATOR} {THRESHOLD_VALUE}`
- **Date de génération du rapport :** `{utc_now_iso()}`
- **Statut technique du smoke test :** **{technical_status}**

---

## 2. Objet

Ce smoke test vérifie le fonctionnement technique et méthodologique de la chaîne expérimentale de `MET-003` sur un corpus synthétique gelé de 20 cas.

Il ne constitue pas une validation scientifique générale de la performance du signal.

Il ne permet pas de conclure à une performance représentative sur des données réelles ou sur une distribution naturelle d’erreurs factuelles.

---

## 3. Corpus

- **Nombre total de cas :** {EXPECTED_CASE_COUNT}
- **Cas POSITIVE :** {EXPECTED_POSITIVE_COUNT}
- **Cas NEGATIVE :** {EXPECTED_NEGATIVE_COUNT}
- **SHA-256 gelé du corpus :** `{EXPECTED_CORPUS_SHA256}`
- **Corpus modifié pendant l’analyse :** non

---

## 4. Baseline déterministe

La baseline est indépendante de NeoMundi et n’utilise aucun modèle juge.

Pour le corpus synthétique gelé EXP-001 v0.1 :

- `NEGATIVE` → `FACTUALLY_CORRECT`
- `POSITIVE` → `FACTUALLY_INCORRECT`

Résultat :

> {baseline_summary}

Cette baseline ne reçoit aucun score NeoMundi et aucune sortie runtime.

---

## 5. Résultats NeoMundi

- **Cas classifiés :** {result["classified"]}/{EXPECTED_CASE_COUNT}
- **Signaux indisponibles :** {result["unavailable"]}
- **Erreurs de calcul :** {result["computation_errors"]}
- **Fallbacks explicitement exposés par l’API :** {result["fallback_count"]}
- **Statuts fallback observés :** {render_list(result["fallback_statuses"])}

### Matrice de confusion

| | Signal positif | Signal négatif |
|---|---:|---:|
| Vérité POSITIVE | VP = {result["tp"]} | FN = {result["fn"]} |
| Vérité NEGATIVE | FP = {result["fp"]} | VN = {result["tn"]} |

---

## 6. Métriques techniques sur ce corpus

- **Précision :** {pct(result["precision"])}
- **Rappel :** {pct(result["recall"])}
- **Spécificité :** {pct(result["specificity"])}
- **Taux de faux positifs :** {pct(result["false_positive_rate"])}
- **Taux de faux négatifs :** {pct(result["false_negative_rate"])}
- **F1 :** {decimal(result["f1"])}
- **Accuracy descriptive :** {pct(result["accuracy"])}
- **Couverture :** {pct(result["coverage"])}

Ces valeurs décrivent uniquement les 20 cas synthétiques gelés de ce smoke test.

Elles ne doivent pas être interprétées comme une estimation robuste ou généralisable de performance.

---

## 7. Distribution des scores MET-003

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

- **Runner version :** {render_list(result["runner_versions"])}
- **GitHub run ID :** {render_list(result["github_run_ids"])}
- **GitHub run attempt :** {render_list(result["github_run_attempts"])}
- **Measurement version :** {render_list(result["measurement_versions"])}
- **Normalizer version :** {render_list(result["normalizer_versions"])}
- **Juge configuré dans le manifeste :** {render_list(result["judge_models_configured"])}
- **Juge explicitement exposé par l’API :** {render_list(result["judge_models_exposed"])}

Le fait que le modèle juge configuré soit documenté dans le manifeste ne signifie pas nécessairement qu’il est exposé dans chaque réponse API.

---

## 9. Fallback

Le runner conserve le statut de fallback de manière conservatrice.

Lorsque l’API ne fournit pas explicitement cette information, le statut :

`UNKNOWN_NOT_EXPOSED`

est conservé.

Il ne doit pas être interprété comme :

`NO_FALLBACK`.

Par conséquent, ce smoke test ne permet pas d’affirmer qu’aucun fallback n’a eu lieu si cette information n’est pas exposée par l’API.

---

## 10. Latence observée

### Latence API mesurée côté runner

- **n :** {len(api_latencies)}
- **minimum :** {decimal(min_or_none(api_latencies))} ms
- **maximum :** {decimal(max_or_none(api_latencies))} ms
- **moyenne :** {decimal(mean_or_none(api_latencies))} ms
- **médiane :** {decimal(median_or_none(api_latencies))} ms

### Processing time retourné par l’API

- **n :** {len(processing_times)}
- **minimum :** {decimal(min_or_none(processing_times))} ms
- **maximum :** {decimal(max_or_none(processing_times))} ms
- **moyenne :** {decimal(mean_or_none(processing_times))} ms
- **médiane :** {decimal(median_or_none(processing_times))} ms

Ces mesures sont descriptives du run et ne constituent pas un benchmark de performance d’infrastructure.

---

## 11. Traçabilité des artefacts

Algorithme :

`SHA-256`

- **Corpus :** `{hashes.get("corpus", "")}`
- **Sorties NeoMundi :** `{hashes.get("neomundi_outputs", "")}`
- **Journal d’erreurs :** `{hashes.get("error_log", "")}`
- **Sorties baseline :** `{hashes.get("baseline_outputs", "")}`
- **Matrice de confusion :** `{hashes.get("confusion_matrix", "")}`

Le hash du présent rapport est enregistré séparément après sa génération dans le manifeste de hashes des artefacts.

---

## 12. Conclusion technique

Le smoke test est déclaré techniquement **{technical_status}** si les conditions suivantes sont remplies :

- les 20 cas sont chargés ;
- le hash du corpus gelé est identique ;
- chaque cas est relié à une sortie NeoMundi ;
- aucune ligne n’est perdue ;
- aucune erreur de calcul n’est présente ;
- aucun signal n’est indisponible ;
- la baseline est produite indépendamment ;
- la matrice de confusion est calculable ;
- les sorties peuvent être hashées.

Résultat observé :

- **VP :** {result["tp"]}
- **FP :** {result["fp"]}
- **VN :** {result["tn"]}
- **FN :** {result["fn"]}
- **Signal indisponible :** {result["unavailable"]}
- **Erreur de calcul :** {result["computation_errors"]}

---

## 13. Non-claims

Ce smoke test ne permet pas d’affirmer :

- que `MET-003` est scientifiquement validé ;
- que le seuil `0.5` est optimal ;
- que la performance observée est généralisable ;
- que le corpus représente une prévalence réelle ;
- qu’une absence de signal prouve qu’une réponse est vraie ;
- qu’un signal constitue à lui seul une preuve indépendante de fausseté ;
- qu’aucun fallback n’a eu lieu lorsque cette information n’est pas exposée ;
- qu’un claim commercial général peut être dérivé de ces 20 cas.

---

## 14. Étape suivante

Effectuer une revue humaine post-run des sorties brutes, notamment :

- cohérence entre score et classification ;
- faux positifs ;
- faux négatifs ;
- résultats techniques atypiques ;
- statut de fallback ;
- éventuelles divergences entre baseline et NeoMundi.

Cette revue doit rester séparée des sorties brutes et ne doit modifier ni le corpus, ni les labels, ni le seuil, ni les résultats du run.
"""


# =============================================================================
# HASHES
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

    hashes: dict[str, str] = {}

    for key, path in files.items():
        if not path.exists():
            raise RuntimeError(
                f"Impossible de hasher : {path}"
            )

        hashes[key] = sha256_file(path)

    return {
        "experiment_id": EXPERIMENT_ID,
        "experiment_version": EXPERIMENT_VERSION,
        "run_id": RUN_ID,
        "algorithm": "SHA-256",
        "generated_at": generated_at,
        "files": hashes,
    }


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:
    print("=" * 72)
    print("NeoMundi Metrology Validation")
    print("EXP-001 — Post-run Analyzer v0.1")
    print("=" * 72)
    print()

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("[1/7] Vérification du corpus gelé...")

    corpus = verify_corpus()

    print(
        f"      OK — {len(corpus)} cas, "
        f"SHA-256 {EXPECTED_CORPUS_SHA256}"
    )

    print("[2/7] Vérification des sorties NeoMundi...")

    outputs = verify_neomundi_outputs(
        corpus
    )

    print(
        f"      OK — {len(outputs)} sorties reliées "
        "aux 20 case_id."
    )

    print("[3/7] Construction de la baseline déterministe...")

    baseline_rows = build_baseline(
        corpus
    )

    write_csv(
        BASELINE_OUTPUT_PATH,
        BASELINE_FIELDS,
        baseline_rows,
    )

    print(
        f"      OK — {BASELINE_OUTPUT_PATH}"
    )

    print("[4/7] Calcul de la matrice de confusion...")

    result = compare_results(
        corpus,
        outputs,
    )

    confusion_rows = build_confusion_matrix_rows(
        result
    )

    write_csv(
        CONFUSION_MATRIX_PATH,
        CONFUSION_FIELDS,
        confusion_rows,
    )

    print(
        f"      VP={result['tp']} "
        f"FP={result['fp']} "
        f"VN={result['tn']} "
        f"FN={result['fn']}"
    )

    print("[5/7] Hash des artefacts intermédiaires...")

    generated_at = utc_now_iso()

    hash_manifest = build_hash_manifest(
        generated_at
    )

    hashes = hash_manifest["files"]

    print("      OK")

    print("[6/7] Génération du rapport FR...")

    manifest = load_manifest()

    report = build_report(
        manifest,
        result,
        hashes,
    )

    REPORT_PATH.write_text(
        report,
        encoding="utf-8",
    )

    report_hash = sha256_file(
        REPORT_PATH
    )

    hash_manifest["files"][
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

    print("[7/7] Résumé")

    print()
    print(f"      VP                    : {result['tp']}")
    print(f"      FP                    : {result['fp']}")
    print(f"      VN                    : {result['tn']}")
    print(f"      FN                    : {result['fn']}")
    print(
        f"      Signaux indisponibles : "
        f"{result['unavailable']}"
    )
    print(
        f"      Erreurs de calcul     : "
        f"{result['computation_errors']}"
    )
    print(
        f"      Couverture            : "
        f"{pct(result['coverage'])}"
    )
    print(
        f"      Précision             : "
        f"{pct(result['precision'])}"
    )
    print(
        f"      Rappel                : "
        f"{pct(result['recall'])}"
    )
    print(
        f"      Spécificité           : "
        f"{pct(result['specificity'])}"
    )
    print(
        f"      F1                    : "
        f"{decimal(result['f1'])}"
    )
    print()

    technical_success = (
        result["classified"] == EXPECTED_CASE_COUNT
        and result["unavailable"] == 0
        and result["computation_errors"] == 0
    )

    if not technical_success:
        print(
            "ANALYSIS COMPLETED WITH TECHNICAL ISSUES",
            file=sys.stderr,
        )
        return 2

    print(
        "ANALYSIS COMPLETED — smoke-test technical chain "
        "is analyzable."
    )

    print(
        "No general scientific or commercial performance claim "
        "is authorized from this 20-case corpus."
    )

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())

    except KeyboardInterrupt:
        print(
            "\nAnalyse interrompue manuellement.",
            file=sys.stderr,
        )
        sys.exit(130)

    except Exception as exc:
        print(
            "\nANALYSIS FAILED",
            file=sys.stderr,
        )
        print(
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)
