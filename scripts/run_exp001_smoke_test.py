#!/usr/bin/env python3
"""
EXP-001 — NeoMundi smoke-test runner
Runner version: v0.1.1

Purpose
-------
Execute the frozen EXP-001 corpus against the NeoMundi /v1/govern endpoint
and record the MET-003 factual risk signal without exposing ground-truth
labels to NeoMundi.

This runner:
- reads the frozen 20-case corpus;
- verifies the exact SHA-256 before execution;
- refuses to execute if the corpus hash differs;
- verifies that the run manifest explicitly authorizes execution;
- sends only prompt + response to NeoMundi;
- never sends ground_truth_label, final_label, reviewer labels or references;
- records factual_hallucination_score;
- derives the frozen experimental classification using threshold 0.5;
- records API errors explicitly;
- preserves the raw NeoMundi response for auditability;
- uses an explicit HTTP User-Agent for API compatibility;
- never stores the NeoMundi API key in the repository;
- returns a non-zero process exit code if any computation error occurs.

This script does NOT:
- modify the frozen corpus;
- modify the frozen threshold;
- calculate the independent baseline;
- calculate the final confusion matrix;
- make any scientific or commercial performance claim.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


# =============================================================================
# EXPERIMENT CONSTANTS — FROZEN FOR EXP-001 v0.1
# =============================================================================

EXPERIMENT_ID = "EXP-001"
EXPERIMENT_VERSION = "v0.1"
RUNNER_VERSION = "v0.1.1"
RUN_ID = "EXP001-SMOKE-RUN-001"

EXPECTED_CASE_COUNT = 20

EXPECTED_CORPUS_SHA256 = (
    "bd9ac82fd53aab35fba15ff999033f894"
    "f69775d256940f27694677720174ce1"
)

METRIC_ID = "MET-003"
METRIC_VERSION = "EXP001_MET003_v0.1"

THRESHOLD_VERSION = "EXP001_THRESHOLD_v0.1"
THRESHOLD_VALUE = 0.5
THRESHOLD_OPERATOR = ">="

DEFAULT_NEOMUNDI_BASE_URL = "https://api.neomundi.io"
GOVERN_PATH = "/v1/govern"

HTTP_TIMEOUT_SECONDS = 180

HTTP_USER_AGENT = (
    "NeoMundi-Metrology-Validation/"
    "EXP-001-v0.1.1"
)


# =============================================================================
# PATHS
# =============================================================================

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

CORPUS_PATH = (
    REPOSITORY_ROOT
    / "experiments"
    / "EXP-001"
    / "EXP-001_smoke_test_20_cases_FR.csv"
)

MANIFEST_PATH = (
    REPOSITORY_ROOT
    / "experiments"
    / "EXP-001"
    / "EXP-001_smoke_test_run_manifest.json"
)

RESULTS_DIR = REPOSITORY_ROOT / "results" / "EXP-001"

OUTPUT_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_neomundi_outputs.csv"
)

ERROR_LOG_PATH = (
    RESULTS_DIR
    / "EXP-001_smoke_test_error_log.csv"
)


# =============================================================================
# OUTPUT SCHEMA
# =============================================================================

OUTPUT_FIELDS = [
    "experiment_id",
    "experiment_version",
    "runner_version",
    "run_id",
    "github_run_id",
    "github_run_attempt",
    "case_id",
    "target_event_id",

    "metric_id",
    "metric_version",
    "threshold_version",
    "threshold_value",
    "threshold_operator",

    "request_started_at_utc",
    "request_completed_at_utc",

    "http_status",
    "request_id",
    "api_timestamp",
    "system_id",
    "mode",

    "factual_hallucination_score",
    "is_hallucinated",
    "experimental_signal_class",

    "judge_model_configured",
    "judge_model_exposed_by_api",

    "fallback_status",
    "fallback_information_exposed_by_api",

    "api_latency_ms",
    "processing_time_ms",

    "calculation_status",
    "error_type",
    "error_message",

    "measurement_version",
    "normalizer_version",
    "trace_id",

    "raw_govern_response",
]


ERROR_FIELDS = [
    "experiment_id",
    "experiment_version",
    "runner_version",
    "run_id",
    "github_run_id",
    "github_run_attempt",
    "case_id",
    "timestamp_utc",
    "error_type",
    "error_message",
    "http_status",
]


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def utc_now_iso() -> str:
    """Return a UTC ISO-8601 timestamp."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def github_run_id() -> str:
    return os.environ.get("GITHUB_RUN_ID", "").strip()


def github_run_attempt() -> str:
    return os.environ.get("GITHUB_RUN_ATTEMPT", "").strip()


def sha256_file(path: Path) -> str:
    """Calculate SHA-256 of a file without modifying it."""
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def nested_get(
    obj: Any,
    path: str,
    default: Any = None,
) -> Any:
    """Read a nested dictionary value using dot notation."""
    current = obj

    for part in path.split("."):
        if not isinstance(current, dict):
            return default

        if part not in current:
            return default

        current = current[part]

    return current


def safe_json(value: Any) -> str:
    """Serialize JSON compactly for CSV audit storage."""
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
        )
    except Exception:
        return str(value)


def load_manifest() -> dict[str, Any]:
    """Load the EXP-001 run manifest."""
    if not MANIFEST_PATH.exists():
        raise RuntimeError(
            f"Manifest introuvable : {MANIFEST_PATH}"
        )

    with MANIFEST_PATH.open(
        "r",
        encoding="utf-8",
    ) as handle:
        return json.load(handle)


def verify_manifest_authorization(
    manifest: dict[str, Any],
) -> None:
    """Refuse execution unless the manifest explicitly authorizes the run."""

    if manifest.get("experiment_id") != EXPERIMENT_ID:
        raise RuntimeError(
            "Le manifest ne correspond pas à EXP-001."
        )

    if manifest.get("experiment_version") != EXPERIMENT_VERSION:
        raise RuntimeError(
            "La version du manifest ne correspond pas à EXP-001 v0.1."
        )

    manifest_run_id = manifest.get("run_id")

    if manifest_run_id != RUN_ID:
        raise RuntimeError(
            f"run_id du manifest = {manifest_run_id!r}, "
            f"attendu = {RUN_ID!r}."
        )

    authorization = manifest.get("authorization", {})

    required_true_fields = [
        "metric_frozen",
        "threshold_frozen",
        "baseline_frozen",
        "protocol_frozen",
        "corpus_frozen",
        "frozen_validation_passed",
        "repository_freeze_anchor_recorded",
        "environment_recorded",
        "execution_authorized",
    ]

    missing = [
        field
        for field in required_true_fields
        if authorization.get(field) is not True
    ]

    if missing:
        raise RuntimeError(
            "Exécution interdite. "
            "Les autorisations suivantes ne sont pas à true : "
            + ", ".join(missing)
        )

    status = manifest.get("status")

    if status != "AUTHORIZED_FOR_EXECUTION":
        raise RuntimeError(
            "Exécution interdite : "
            f"status du manifest = {status!r}, "
            "attendu = 'AUTHORIZED_FOR_EXECUTION'."
        )


def verify_frozen_constants(
    manifest: dict[str, Any],
) -> None:
    """Verify critical frozen experimental parameters."""

    metric = manifest.get("metric", {})
    corpus = manifest.get("corpus", {})

    if metric.get("metric_id") != METRIC_ID:
        raise RuntimeError(
            "MET-003 ne correspond plus au manifest."
        )

    if metric.get("metric_version") != METRIC_VERSION:
        raise RuntimeError(
            "La version de MET-003 ne correspond plus au manifest."
        )

    if float(metric.get("threshold_value")) != THRESHOLD_VALUE:
        raise RuntimeError(
            "Le seuil gelé ne correspond plus à 0.5."
        )

    if metric.get("threshold_operator") != THRESHOLD_OPERATOR:
        raise RuntimeError(
            "L'opérateur du seuil gelé ne correspond plus à >=."
        )

    manifest_hash = corpus.get("sha256")

    if manifest_hash != EXPECTED_CORPUS_SHA256:
        raise RuntimeError(
            "Le SHA-256 enregistré dans le manifest ne correspond "
            "pas au SHA-256 gelé attendu par le runner."
        )


def verify_corpus_hash() -> str:
    """Verify the frozen corpus SHA-256 before any API request."""

    if not CORPUS_PATH.exists():
        raise RuntimeError(
            f"Corpus introuvable : {CORPUS_PATH}"
        )

    actual_hash = sha256_file(CORPUS_PATH)

    if actual_hash != EXPECTED_CORPUS_SHA256:
        raise RuntimeError(
            "\nCORPUS HASH MISMATCH — EXECUTION REFUSED\n"
            f"Expected : {EXPECTED_CORPUS_SHA256}\n"
            f"Actual   : {actual_hash}\n"
            "Le corpus gelé ne doit pas être exécuté dans cet état."
        )

    return actual_hash


def load_corpus() -> list[dict[str, str]]:
    """Load and minimally validate the frozen CSV corpus."""

    with CORPUS_PATH.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    required_columns = {
        "case_id",
        "prompt",
        "response",
        "ground_truth_label",
        "target_event_id",
        "final_label",
        "freeze_status",
        "exclusion_status",
    }

    actual_columns = set(fieldnames)

    missing_columns = required_columns - actual_columns

    if missing_columns:
        raise RuntimeError(
            "Colonnes requises absentes du corpus : "
            + ", ".join(sorted(missing_columns))
        )

    if len(rows) != EXPECTED_CASE_COUNT:
        raise RuntimeError(
            f"Nombre de cas incorrect : {len(rows)} "
            f"(attendu : {EXPECTED_CASE_COUNT})."
        )

    case_ids = [row["case_id"] for row in rows]

    if len(case_ids) != len(set(case_ids)):
        raise RuntimeError(
            "Des case_id dupliqués ont été détectés."
        )

    for row in rows:
        case_id = row["case_id"]

        if row.get("freeze_status") != "FROZEN":
            raise RuntimeError(
                f"{case_id}: freeze_status != FROZEN."
            )

        if row.get("exclusion_status") != "INCLUDED":
            raise RuntimeError(
                f"{case_id}: le cas n'est pas INCLUDED."
            )

        if not row.get("prompt", "").strip():
            raise RuntimeError(
                f"{case_id}: prompt vide."
            )

        if not row.get("response", "").strip():
            raise RuntimeError(
                f"{case_id}: response vide."
            )

    return rows


def get_api_configuration() -> tuple[str, str]:
    """Read NeoMundi API configuration from environment variables."""

    api_key = os.environ.get(
        "NEOMUNDI_API_KEY",
        "",
    ).strip()

    base_url = os.environ.get(
        "NEOMUNDI_BASE_URL",
        DEFAULT_NEOMUNDI_BASE_URL,
    ).strip()

    if not api_key:
        raise RuntimeError(
            "NEOMUNDI_API_KEY est absente.\n"
            "La clé doit être définie comme variable d'environnement "
            "et ne doit jamais être écrite dans le repository."
        )

    if not base_url:
        raise RuntimeError(
            "NEOMUNDI_BASE_URL est vide."
        )

    return api_key, base_url.rstrip("/")


# =============================================================================
# NEOMUNDI API
# =============================================================================

def call_neomundi(
    *,
    api_key: str,
    base_url: str,
    prompt: str,
    response_text: str,
) -> tuple[int, dict[str, Any], float]:
    """
    Call the NeoMundi /v1/govern endpoint.

    Only prompt and response are sent from the experimental corpus.
    Ground-truth labels and reference information are never included.
    """

    url = f"{base_url}{GOVERN_PATH}"

    payload = {
        "source_type": "llm",
        "mode": "OBS",
        "llm_prompt": prompt,
        "llm_response": response_text,
        "raw_metrics": {
            "token_count": 0,
            "latency_ms": 0,
        },
    }

    body = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")

    request = Request(
        url=url,
        data=body,
        method="POST",
        headers={
            "X-API-Key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": HTTP_USER_AGENT,
            "X-NeoMundi-Client": "EXP-001-Metrology-Validation",
        },
    )

    started = time.perf_counter()

    try:
        with urlopen(
            request,
            timeout=HTTP_TIMEOUT_SECONDS,
        ) as response:
            raw = response.read().decode(
                "utf-8",
                errors="replace",
            )

            elapsed_ms = (
                time.perf_counter() - started
            ) * 1000.0

            status = response.getcode()

    except HTTPError as exc:
        elapsed_ms = (
            time.perf_counter() - started
        ) * 1000.0

        error_body = exc.read().decode(
            "utf-8",
            errors="replace",
        )

        raise RuntimeError(
            f"HTTP {exc.code}: {error_body}"
        ) from exc

    except URLError as exc:
        raise RuntimeError(
            f"Erreur réseau : {exc.reason}"
        ) from exc

    except TimeoutError as exc:
        raise RuntimeError(
            "Timeout lors de l'appel à NeoMundi."
        ) from exc

    try:
        parsed = json.loads(raw)

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "NeoMundi a retourné une réponse qui n'est pas "
            f"un JSON valide : {raw[:1000]}"
        ) from exc

    if not isinstance(parsed, dict):
        raise RuntimeError(
            "La réponse NeoMundi JSON n'est pas un objet."
        )

    return status, parsed, elapsed_ms


# =============================================================================
# RESULT INTERPRETATION
# =============================================================================

def normalize_score(value: Any) -> float | None:
    """Safely normalize factual_hallucination_score."""

    if value is None:
        return None

    if isinstance(value, bool):
        return None

    try:
        score = float(value)
    except (TypeError, ValueError):
        return None

    if not 0.0 <= score <= 1.0:
        return None

    return score


def classify_signal(
    score: float | None,
) -> tuple[bool | None, str]:
    """Apply the frozen EXP-001 threshold."""

    if score is None:
        return None, "SIGNAL_UNAVAILABLE"

    is_hallucinated = score >= THRESHOLD_VALUE

    if is_hallucinated:
        return True, "SIGNAL_POSITIVE"

    return False, "SIGNAL_NEGATIVE"


def detect_fallback_information(
    response: dict[str, Any],
) -> tuple[str, bool]:
    """
    Record fallback information conservatively.

    If no explicit fallback field is exposed by the API, the runner records
    UNKNOWN_NOT_EXPOSED instead of assuming that no fallback occurred.
    """

    explicit_candidates = [
        nested_get(response, "fallback"),
        nested_get(response, "fallback_status"),
        nested_get(response, "quality.fallback"),
        nested_get(response, "quality.fallback_status"),
        nested_get(response, "audit.fallback"),
        nested_get(response, "audit.fallback_status"),
    ]

    exposed_values = [
        value
        for value in explicit_candidates
        if value is not None
    ]

    if not exposed_values:
        return "UNKNOWN_NOT_EXPOSED", False

    return safe_json(exposed_values), True


def extract_judge_model_exposed(
    response: dict[str, Any],
) -> str:
    """Look only for an explicitly exposed judge-model field."""

    candidates = [
        nested_get(response, "judge_model"),
        nested_get(response, "quality.judge_model"),
        nested_get(response, "audit.judge_model"),
        nested_get(response, "hallucination_judge_model"),
    ]

    for candidate in candidates:
        if candidate is not None:
            text = str(candidate).strip()

            if text:
                return text

    return ""


# =============================================================================
# CSV WRITERS
# =============================================================================

def prepare_output_files() -> None:
    """
    Refuse to overwrite existing non-empty outputs in the current workspace.
    """

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in [OUTPUT_PATH, ERROR_LOG_PATH]:
        if path.exists() and path.stat().st_size > 0:
            raise RuntimeError(
                f"Sortie existante détectée : {path}\n"
                "Le protocole interdit d'écraser un résultat antérieur "
                "sans versionnement explicite."
            )


def write_output_header() -> None:
    with OUTPUT_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=OUTPUT_FIELDS,
        )

        writer.writeheader()


def write_error_header() -> None:
    with ERROR_LOG_PATH.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ERROR_FIELDS,
        )

        writer.writeheader()


def append_output(row: dict[str, Any]) -> None:
    with OUTPUT_PATH.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=OUTPUT_FIELDS,
            extrasaction="ignore",
        )

        writer.writerow(row)


def append_error(
    *,
    case_id: str,
    error_type: str,
    error_message: str,
    http_status: str = "",
) -> None:
    with ERROR_LOG_PATH.open(
        "a",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ERROR_FIELDS,
        )

        writer.writerow(
            {
                "experiment_id": EXPERIMENT_ID,
                "experiment_version": EXPERIMENT_VERSION,
                "runner_version": RUNNER_VERSION,
                "run_id": RUN_ID,
                "github_run_id": github_run_id(),
                "github_run_attempt": github_run_attempt(),
                "case_id": case_id,
                "timestamp_utc": utc_now_iso(),
                "error_type": error_type,
                "error_message": error_message,
                "http_status": http_status,
            }
        )


# =============================================================================
# RESULT BUILDERS
# =============================================================================

def build_result_row(
    *,
    case_id: str,
    target_event_id: str,
    request_started_at: str,
    request_completed_at: str,
    http_status: int,
    api_response: dict[str, Any],
    api_latency_ms: float,
    judge_model_configured: str,
) -> dict[str, Any]:

    raw_score = nested_get(
        api_response,
        "quality.factual_hallucination_score",
    )

    score = normalize_score(raw_score)

    is_hallucinated, experimental_class = classify_signal(
        score
    )

    fallback_status, fallback_exposed = (
        detect_fallback_information(api_response)
    )

    judge_model_exposed = extract_judge_model_exposed(
        api_response
    )

    calculation_status = (
        "CALCULATED"
        if score is not None
        else "SIGNAL_UNAVAILABLE"
    )

    return {
        "experiment_id": EXPERIMENT_ID,
        "experiment_version": EXPERIMENT_VERSION,
        "runner_version": RUNNER_VERSION,
        "run_id": RUN_ID,
        "github_run_id": github_run_id(),
        "github_run_attempt": github_run_attempt(),
        "case_id": case_id,
        "target_event_id": target_event_id,

        "metric_id": METRIC_ID,
        "metric_version": METRIC_VERSION,
        "threshold_version": THRESHOLD_VERSION,
        "threshold_value": THRESHOLD_VALUE,
        "threshold_operator": THRESHOLD_OPERATOR,

        "request_started_at_utc": request_started_at,
        "request_completed_at_utc": request_completed_at,

        "http_status": http_status,

        "request_id": nested_get(
            api_response,
            "request_id",
            "",
        ),

        "api_timestamp": nested_get(
            api_response,
            "timestamp",
            "",
        ),

        "system_id": nested_get(
            api_response,
            "system_id",
            "",
        ),

        "mode": nested_get(
            api_response,
            "mode",
            "",
        ),

        "factual_hallucination_score": (
            ""
            if score is None
            else score
        ),

        "is_hallucinated": (
            ""
            if is_hallucinated is None
            else str(is_hallucinated).lower()
        ),

        "experimental_signal_class": experimental_class,

        "judge_model_configured": judge_model_configured,
        "judge_model_exposed_by_api": judge_model_exposed,

        "fallback_status": fallback_status,

        "fallback_information_exposed_by_api": (
            str(fallback_exposed).lower()
        ),

        "api_latency_ms": round(
            api_latency_ms,
            3,
        ),

        "processing_time_ms": nested_get(
            api_response,
            "processing_time_ms",
            "",
        ),

        "calculation_status": calculation_status,
        "error_type": "",
        "error_message": "",

        "measurement_version": nested_get(
            api_response,
            "audit.measurement_version",
            "",
        ),

        "normalizer_version": nested_get(
            api_response,
            "audit.normalizer_version",
            "",
        ),

        "trace_id": nested_get(
            api_response,
            "audit.trace_id",
            "",
        ),

        "raw_govern_response": safe_json(
            api_response
        ),
    }


def build_error_output_row(
    *,
    case_id: str,
    target_event_id: str,
    started_at: str,
    completed_at: str,
    error_type: str,
    error_message: str,
    judge_model_configured: str,
) -> dict[str, Any]:

    return {
        "experiment_id": EXPERIMENT_ID,
        "experiment_version": EXPERIMENT_VERSION,
        "runner_version": RUNNER_VERSION,
        "run_id": RUN_ID,
        "github_run_id": github_run_id(),
        "github_run_attempt": github_run_attempt(),
        "case_id": case_id,
        "target_event_id": target_event_id,

        "metric_id": METRIC_ID,
        "metric_version": METRIC_VERSION,
        "threshold_version": THRESHOLD_VERSION,
        "threshold_value": THRESHOLD_VALUE,
        "threshold_operator": THRESHOLD_OPERATOR,

        "request_started_at_utc": started_at,
        "request_completed_at_utc": completed_at,

        "http_status": "",
        "request_id": "",
        "api_timestamp": "",
        "system_id": "",
        "mode": "OBS",

        "factual_hallucination_score": "",
        "is_hallucinated": "",
        "experimental_signal_class": "COMPUTATION_ERROR",

        "judge_model_configured": judge_model_configured,
        "judge_model_exposed_by_api": "",

        "fallback_status": "UNKNOWN_DUE_TO_ERROR",
        "fallback_information_exposed_by_api": "false",

        "api_latency_ms": "",
        "processing_time_ms": "",

        "calculation_status": "COMPUTATION_ERROR",
        "error_type": error_type,
        "error_message": error_message,

        "measurement_version": "",
        "normalizer_version": "",
        "trace_id": "",

        "raw_govern_response": "",
    }


# =============================================================================
# EXECUTION
# =============================================================================

def main() -> int:
    print("=" * 72)
    print("NeoMundi Metrology Validation")
    print(
        f"EXP-001 — Smoke Test Runner {RUNNER_VERSION}"
    )
    print("=" * 72)
    print()

    # -------------------------------------------------------------------------
    # 1. Manifest
    # -------------------------------------------------------------------------

    print("[1/7] Lecture du manifeste...")

    manifest = load_manifest()

    verify_manifest_authorization(manifest)
    verify_frozen_constants(manifest)

    print("      OK — exécution explicitement autorisée.")

    # -------------------------------------------------------------------------
    # 2. Frozen corpus hash
    # -------------------------------------------------------------------------

    print("[2/7] Vérification du SHA-256 du corpus...")

    actual_hash = verify_corpus_hash()

    print(f"      OK — {actual_hash}")

    # -------------------------------------------------------------------------
    # 3. Corpus
    # -------------------------------------------------------------------------

    print("[3/7] Chargement du corpus gelé...")

    rows = load_corpus()

    print(f"      OK — {len(rows)} cas chargés.")

    # -------------------------------------------------------------------------
    # 4. API configuration
    # -------------------------------------------------------------------------

    print("[4/7] Vérification de la configuration API...")

    api_key, base_url = get_api_configuration()

    endpoint = f"{base_url}{GOVERN_PATH}"

    print(f"      Endpoint : {endpoint}")
    print("      API key  : présente (valeur masquée)")
    print(f"      User-Agent : {HTTP_USER_AGENT}")

    # -------------------------------------------------------------------------
    # 5. Judge configuration
    # -------------------------------------------------------------------------

    environment = manifest.get(
        "environment",
        {},
    )

    judge_model_configured = str(
        environment.get(
            "judge_model",
            "",
        )
    )

    print(
        "      Juge configuré : "
        f"{judge_model_configured or 'NON RENSEIGNÉ'}"
    )

    # -------------------------------------------------------------------------
    # 6. Output preparation
    # -------------------------------------------------------------------------

    print("[5/7] Préparation des fichiers de sortie...")

    prepare_output_files()

    write_output_header()
    write_error_header()

    print(f"      {OUTPUT_PATH}")
    print(f"      {ERROR_LOG_PATH}")

    # -------------------------------------------------------------------------
    # 7. Execute cases
    # -------------------------------------------------------------------------

    print("[6/7] Exécution des 20 cas...")
    print()

    success_count = 0
    unavailable_count = 0
    error_count = 0

    for index, row in enumerate(
        rows,
        start=1,
    ):
        case_id = row["case_id"].strip()
        prompt = row["prompt"]
        response_text = row["response"]
        target_event_id = row["target_event_id"].strip()

        print(
            f"      [{index:02d}/{len(rows):02d}] "
            f"{case_id} ... ",
            end="",
            flush=True,
        )

        started_at = utc_now_iso()

        try:
            (
                http_status,
                api_response,
                api_latency_ms,
            ) = call_neomundi(
                api_key=api_key,
                base_url=base_url,
                prompt=prompt,
                response_text=response_text,
            )

            completed_at = utc_now_iso()

            result_row = build_result_row(
                case_id=case_id,
                target_event_id=target_event_id,
                request_started_at=started_at,
                request_completed_at=completed_at,
                http_status=http_status,
                api_response=api_response,
                api_latency_ms=api_latency_ms,
                judge_model_configured=judge_model_configured,
            )

            append_output(result_row)

            signal_class = result_row[
                "experimental_signal_class"
            ]

            score = result_row[
                "factual_hallucination_score"
            ]

            if signal_class == "SIGNAL_UNAVAILABLE":
                unavailable_count += 1

            else:
                success_count += 1

            print(
                f"{signal_class}"
                + (
                    f" | score={score}"
                    if score != ""
                    else ""
                )
            )

        except Exception as exc:
            completed_at = utc_now_iso()

            error_count += 1

            error_type = type(exc).__name__
            error_message = str(exc)

            append_error(
                case_id=case_id,
                error_type=error_type,
                error_message=error_message,
            )

            append_output(
                build_error_output_row(
                    case_id=case_id,
                    target_event_id=target_event_id,
                    started_at=started_at,
                    completed_at=completed_at,
                    error_type=error_type,
                    error_message=error_message,
                    judge_model_configured=judge_model_configured,
                )
            )

            print(
                f"COMPUTATION_ERROR | "
                f"{error_type}: {error_message}"
            )

    # -------------------------------------------------------------------------
    # Technical summary
    # -------------------------------------------------------------------------

    print()
    print("[7/7] Résumé technique")
    print()

    print(f"      Cas prévus               : {len(rows)}")
    print(f"      Signaux calculés          : {success_count}")
    print(f"      Signaux indisponibles     : {unavailable_count}")
    print(f"      Erreurs de calcul         : {error_count}")

    print()
    print(f"      Sorties NeoMundi : {OUTPUT_PATH}")
    print(f"      Journal erreurs  : {ERROR_LOG_PATH}")
    print()

    total = (
        success_count
        + unavailable_count
        + error_count
    )

    if total != len(rows):
        print(
            "FATAL — le nombre de résultats ne correspond "
            "pas au nombre de cas.",
            file=sys.stderr,
        )
        return 2

    if error_count > 0:
        print(
            "RUN FAILED — au moins une erreur de calcul "
            "a été enregistrée.",
            file=sys.stderr,
        )
        return 3

    if unavailable_count > 0:
        print(
            "RUN COMPLETED WITH UNAVAILABLE SIGNALS — "
            "une revue technique est requise."
        )
        return 0

    print(
        "RUN COMPLETED — les 20 cas ont produit un signal. "
        "Aucune interprétation de performance n'est produite "
        "par ce script."
    )

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())

    except KeyboardInterrupt:
        print(
            "\nExécution interrompue manuellement.",
            file=sys.stderr,
        )
        sys.exit(130)

    except Exception as exc:
        print(
            "\nEXECUTION REFUSED / FATAL ERROR",
            file=sys.stderr,
        )
        print(
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)
