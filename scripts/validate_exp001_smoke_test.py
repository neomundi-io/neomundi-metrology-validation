#!/usr/bin/env python3
"""
Validation structurelle du corpus smoke test EXP-001.

Ce script ne mesure pas la performance de NeoMundi.
Il vérifie uniquement la cohérence méthodologique et technique du fichier CSV.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


EXPECTED_COLUMNS = [
    "case_id",
    "source_case_id",
    "prompt",
    "response",
    "ground_truth_label",
    "target_event_id",
    "factual_family",
    "case_type",
    "origin_type",
    "reference_type",
    "reference_location",
    "reference_version",
    "label_justification",
    "confidence_level",
    "natural_or_injected",
    "injection_description",
    "model_or_profile",
    "provider",
    "language",
    "difficulty",
    "response_length",
    "split",
    "review_status",
    "reviewer_1_label",
    "reviewer_1_confidence",
    "reviewer_1_justification",
    "reviewer_2_label",
    "reviewer_2_confidence",
    "reviewer_2_justification",
    "arbitration_status",
    "final_label",
    "exclusion_status",
    "exclusion_reason",
    "case_version",
    "freeze_status",
    "created_at",
    "updated_at",
    "decision_owner",
]

ALLOWED_VALUES = {
    "ground_truth_label": {
        "POSITIVE",
        "NEGATIVE",
        "AMBIGUOUS",
        "REVIEW_REQUIRED",
        "NOT_APPLICABLE",
    },
    "target_event_id": {"EVT-003"},
    "case_type": {"CLOSED", "OPEN_VERIFIABLE"},
    "origin_type": {"NATURAL", "SYNTHETIC"},
    "confidence_level": {"HIGH", "MEDIUM", "LOW"},
    "natural_or_injected": {"NOT_INJECTED", "INJECTED"},
    "difficulty": {"EASY", "MEDIUM", "HARD"},
    "split": {
        "CALIBRATION",
        "VALIDATION",
        "FINAL_TEST",
        "UNASSIGNED",
    },
    "review_status": {
        "NOT_REVIEWED",
        "UNDER_REVIEW",
        "APPROVED",
        "REJECTED",
    },
    "arbitration_status": {
        "NOT_REQUIRED",
        "PENDING",
        "COMPLETED",
    },
    "final_label": {
        "POSITIVE",
        "NEGATIVE",
        "AMBIGUOUS",
        "REVIEW_REQUIRED",
        "NOT_APPLICABLE",
    },
    "exclusion_status": {"INCLUDED", "EXCLUDED"},
    "freeze_status": {
        "DRAFT",
        "APPROVED",
        "FROZEN",
        "ARCHIVED",
    },
}


def validate_csv(csv_path: Path) -> list[str]:
    errors: list[str] = []

    if not csv_path.exists():
        return [f"Fichier introuvable : {csv_path}"]

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != EXPECTED_COLUMNS:
            errors.append(
                "Les colonnes du fichier ne correspondent pas au schéma attendu."
            )
            return errors

        rows = list(reader)

    if len(rows) != 20:
        errors.append(
            f"Le corpus doit contenir 20 cas, mais {len(rows)} ont été trouvés."
        )

    case_ids = [row["case_id"].strip() for row in rows]

    if len(case_ids) != len(set(case_ids)):
        errors.append("Des identifiants case_id sont dupliqués.")

    expected_ids = {
        f"EXP001-SMOKE-{index:03d}"
        for index in range(1, 21)
    }

    missing_ids = expected_ids - set(case_ids)
    unexpected_ids = set(case_ids) - expected_ids

    if missing_ids:
        errors.append(
            "Identifiants manquants : " + ", ".join(sorted(missing_ids))
        )

    if unexpected_ids:
        errors.append(
            "Identifiants inattendus : " + ", ".join(sorted(unexpected_ids))
        )

    labels = Counter(
        row["ground_truth_label"].strip()
        for row in rows
    )

    if labels["POSITIVE"] != 10:
        errors.append(
            f"10 cas POSITIVE attendus, {labels['POSITIVE']} trouvés."
        )

    if labels["NEGATIVE"] != 10:
        errors.append(
            f"10 cas NEGATIVE attendus, {labels['NEGATIVE']} trouvés."
        )

    for line_number, row in enumerate(rows, start=2):
        for required_field in [
            "case_id",
            "prompt",
            "response",
            "ground_truth_label",
            "target_event_id",
            "factual_family",
            "case_type",
            "origin_type",
            "reference_type",
            "label_justification",
            "confidence_level",
            "natural_or_injected",
            "language",
            "difficulty",
            "final_label",
            "exclusion_status",
            "case_version",
            "freeze_status",
            "decision_owner",
        ]:
            if not row[required_field].strip():
                errors.append(
                    f"Ligne {line_number} : champ obligatoire vide "
                    f"({required_field})."
                )

        for field, allowed in ALLOWED_VALUES.items():
            value = row[field].strip()

            if value and value not in allowed:
                errors.append(
                    f"Ligne {line_number} : valeur non autorisée "
                    f"pour {field} : {value}"
                )

        ground_truth = row["ground_truth_label"].strip()
        final_label = row["final_label"].strip()

        if ground_truth != final_label:
            errors.append(
                f"Ligne {line_number} : ground_truth_label et "
                f"final_label sont différents."
            )

        construction_type = row["natural_or_injected"].strip()
        injection_description = row["injection_description"].strip()

        if (
            construction_type == "INJECTED"
            and not injection_description
        ):
            errors.append(
                f"Ligne {line_number} : une description d’injection "
                "est obligatoire pour un cas INJECTED."
            )

        if (
            construction_type == "NOT_INJECTED"
            and injection_description
        ):
            errors.append(
                f"Ligne {line_number} : un cas NOT_INJECTED ne doit "
                "pas contenir de description d’injection."
            )

        if row["origin_type"].strip() != "SYNTHETIC":
            errors.append(
                f"Ligne {line_number} : tous les cas du smoke test "
                "doivent être SYNTHETIC."
            )

    return errors


def main() -> int:
    default_path = Path(
        "experiments/EXP-001/"
        "EXP-001_smoke_test_20_cases_FR.csv"
    )

    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path
    errors = validate_csv(csv_path)

    if errors:
        print("ÉCHEC — incohérences détectées :")

        for error in errors:
            print(f"- {error}")

        return 1

    print("SUCCÈS — le corpus EXP-001 est structurellement valide.")
    print("- 20 cas détectés")
    print("- 10 cas POSITIVE")
    print("- 10 cas NEGATIVE")
    print("- identifiants uniques")
    print("- valeurs autorisées respectées")
    print("- cohérence des injections vérifiée")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
