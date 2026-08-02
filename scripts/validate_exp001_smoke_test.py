#!/usr/bin/env python3
"""
Validation du corpus smoke test EXP-001.

Ce script ne mesure pas la performance de NeoMundi.
Il vérifie uniquement la cohérence méthodologique et technique
du fichier CSV.

Trois niveaux de validation sont disponibles :

1. structural
   Vérifie la structure minimale du corpus.
   C'est le niveau utilisé par défaut dans GitHub Actions.

2. documented
   Vérifie que les références ont été documentées et versionnées.

3. frozen
   Vérifie que le corpus a été revu, affecté à un split et gelé
   avant toute exécution expérimentale.

Exemples :

    python scripts/validate_exp001_smoke_test.py

    python scripts/validate_exp001_smoke_test.py \
        --stage documented

    python scripts/validate_exp001_smoke_test.py \
        --stage frozen

    python scripts/validate_exp001_smoke_test.py \
        experiments/EXP-001/EXP-001_smoke_test_20_cases_FR.csv \
        --stage frozen
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_CSV_PATH = Path(
    "experiments/EXP-001/"
    "EXP-001_smoke_test_20_cases_FR.csv"
)

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
    "target_event_id": {
        "EVT-003",
    },
    "case_type": {
        "CLOSED",
        "OPEN_VERIFIABLE",
    },
    "origin_type": {
        "NATURAL",
        "SYNTHETIC",
    },
    "confidence_level": {
        "HIGH",
        "MEDIUM",
        "LOW",
    },
    "natural_or_injected": {
        "NOT_INJECTED",
        "INJECTED",
    },
    "difficulty": {
        "EASY",
        "MEDIUM",
        "HARD",
    },
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
    "reviewer_1_label": {
        "POSITIVE",
        "NEGATIVE",
        "AMBIGUOUS",
        "REVIEW_REQUIRED",
        "NOT_APPLICABLE",
    },
    "reviewer_1_confidence": {
        "HIGH",
        "MEDIUM",
        "LOW",
    },
    "reviewer_2_label": {
        "POSITIVE",
        "NEGATIVE",
        "AMBIGUOUS",
        "REVIEW_REQUIRED",
        "NOT_APPLICABLE",
    },
    "reviewer_2_confidence": {
        "HIGH",
        "MEDIUM",
        "LOW",
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
    "exclusion_status": {
        "INCLUDED",
        "EXCLUDED",
    },
    "freeze_status": {
        "DRAFT",
        "APPROVED",
        "FROZEN",
        "ARCHIVED",
    },
}

PROVISIONAL_VALUES = {
    "",
    "TO_BE_DOCUMENTED",
    "TO_BE_DEFINED",
    "TBD",
    "TODO",
    "UNKNOWN",
}

STRUCTURAL_REQUIRED_FIELDS = [
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
]

DOCUMENTED_REQUIRED_FIELDS = [
    "reference_location",
    "reference_version",
    "label_justification",
    "updated_at",
]

FROZEN_REQUIRED_FIELDS = [
    "split",
    "review_status",
    "reviewer_1_label",
    "reviewer_1_confidence",
    "reviewer_1_justification",
    "final_label",
    "case_version",
    "freeze_status",
    "updated_at",
    "decision_owner",
]


def clean(value: str | None) -> str:
    """Retourne une valeur textuelle nettoyée."""

    return (value or "").strip()


def is_provisional(value: str | None) -> bool:
    """Indique si une valeur est vide ou provisoire."""

    return clean(value).upper() in PROVISIONAL_VALUES


def is_valid_http_url(value: str) -> bool:
    """Vérifie sommairement qu'une valeur est une URL HTTP ou HTTPS."""

    parsed = urlparse(value)

    return (
        parsed.scheme in {"http", "https"}
        and bool(parsed.netloc)
    )


def load_csv(
    csv_path: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    """
    Charge le CSV et vérifie son schéma.

    Retourne :
    - les lignes ;
    - les erreurs rencontrées.
    """

    errors: list[str] = []

    if not csv_path.exists():
        return [], [f"Fichier introuvable : {csv_path}"]

    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != EXPECTED_COLUMNS:
            errors.append(
                "Les colonnes du fichier ne correspondent pas "
                "au schéma attendu."
            )

            if reader.fieldnames is not None:
                missing_columns = [
                    column
                    for column in EXPECTED_COLUMNS
                    if column not in reader.fieldnames
                ]

                unexpected_columns = [
                    column
                    for column in reader.fieldnames
                    if column not in EXPECTED_COLUMNS
                ]

                if missing_columns:
                    errors.append(
                        "Colonnes manquantes : "
                        + ", ".join(missing_columns)
                    )

                if unexpected_columns:
                    errors.append(
                        "Colonnes inattendues : "
                        + ", ".join(unexpected_columns)
                    )

            return [], errors

        rows = list(reader)

    return rows, errors


def validate_allowed_values(
    rows: list[dict[str, str]],
) -> list[str]:
    """Vérifie les vocabulaires contrôlés."""

    errors: list[str] = []

    for line_number, row in enumerate(rows, start=2):
        for field, allowed_values in ALLOWED_VALUES.items():
            value = clean(row.get(field))

            if value and value not in allowed_values:
                errors.append(
                    f"Ligne {line_number} : valeur non autorisée "
                    f"pour {field} : {value}"
                )

    return errors


def validate_required_fields(
    rows: list[dict[str, str]],
    fields: list[str],
    stage_name: str,
) -> list[str]:
    """Vérifie que les champs attendus sont renseignés."""

    errors: list[str] = []

    for line_number, row in enumerate(rows, start=2):
        for field in fields:
            if not clean(row.get(field)):
                errors.append(
                    f"Ligne {line_number} : champ obligatoire vide "
                    f"pour le niveau {stage_name} ({field})."
                )

    return errors


def validate_structural(
    rows: list[dict[str, str]],
) -> list[str]:
    """Validation structurelle minimale du smoke test."""

    errors: list[str] = []

    if len(rows) != 20:
        errors.append(
            "Le corpus doit contenir 20 cas, "
            f"mais {len(rows)} ont été trouvés."
        )

    errors.extend(
        validate_required_fields(
            rows,
            STRUCTURAL_REQUIRED_FIELDS,
            "structural",
        )
    )

    errors.extend(validate_allowed_values(rows))

    case_ids = [
        clean(row.get("case_id"))
        for row in rows
    ]

    if len(case_ids) != len(set(case_ids)):
        errors.append(
            "Des identifiants case_id sont dupliqués."
        )

    expected_ids = {
        f"EXP001-SMOKE-{index:03d}"
        for index in range(1, 21)
    }

    actual_ids = set(case_ids)

    missing_ids = expected_ids - actual_ids
    unexpected_ids = actual_ids - expected_ids

    if missing_ids:
        errors.append(
            "Identifiants manquants : "
            + ", ".join(sorted(missing_ids))
        )

    if unexpected_ids:
        errors.append(
            "Identifiants inattendus : "
            + ", ".join(sorted(unexpected_ids))
        )

    labels = Counter(
        clean(row.get("ground_truth_label"))
        for row in rows
    )

    if labels["POSITIVE"] != 10:
        errors.append(
            "10 cas POSITIVE attendus, "
            f"{labels['POSITIVE']} trouvés."
        )

    if labels["NEGATIVE"] != 10:
        errors.append(
            "10 cas NEGATIVE attendus, "
            f"{labels['NEGATIVE']} trouvés."
        )

    for line_number, row in enumerate(rows, start=2):
        ground_truth = clean(
            row.get("ground_truth_label")
        )

        final_label = clean(
            row.get("final_label")
        )

        if ground_truth != final_label:
            errors.append(
                f"Ligne {line_number} : ground_truth_label et "
                "final_label sont différents."
            )

        construction_type = clean(
            row.get("natural_or_injected")
        )

        injection_description = clean(
            row.get("injection_description")
        )

        if (
            construction_type == "INJECTED"
            and not injection_description
        ):
            errors.append(
                f"Ligne {line_number} : une description "
                "d’injection est obligatoire pour un cas INJECTED."
            )

        if (
            construction_type == "NOT_INJECTED"
            and injection_description
        ):
            errors.append(
                f"Ligne {line_number} : un cas NOT_INJECTED "
                "ne doit pas contenir de description d’injection."
            )

        if clean(row.get("origin_type")) != "SYNTHETIC":
            errors.append(
                f"Ligne {line_number} : tous les cas du smoke test "
                "doivent être SYNTHETIC."
            )

        exclusion_status = clean(
            row.get("exclusion_status")
        )

        exclusion_reason = clean(
            row.get("exclusion_reason")
        )

        if (
            exclusion_status == "EXCLUDED"
            and not exclusion_reason
        ):
            errors.append(
                f"Ligne {line_number} : un motif d’exclusion "
                "est obligatoire pour un cas EXCLUDED."
            )

        if (
            exclusion_status == "INCLUDED"
            and exclusion_reason
        ):
            errors.append(
                f"Ligne {line_number} : un cas INCLUDED "
                "ne doit pas contenir de motif d’exclusion."
            )

    return errors


def validate_documented(
    rows: list[dict[str, str]],
) -> list[str]:
    """
    Vérifie que les références sont documentées.

    Ce niveau n'exige pas encore que la revue humaine soit terminée
    ni que le corpus soit gelé.
    """

    errors: list[str] = []

    errors.extend(
        validate_required_fields(
            rows,
            DOCUMENTED_REQUIRED_FIELDS,
            "documented",
        )
    )

    for line_number, row in enumerate(rows, start=2):
        reference_type = clean(
            row.get("reference_type")
        )

        reference_location = clean(
            row.get("reference_location")
        )

        reference_version = clean(
            row.get("reference_version")
        )

        label_justification = clean(
            row.get("label_justification")
        )

        for field_name, value in [
            ("reference_location", reference_location),
            ("reference_version", reference_version),
            ("label_justification", label_justification),
        ]:
            if is_provisional(value):
                errors.append(
                    f"Ligne {line_number} : valeur provisoire "
                    f"interdite pour {field_name} : {value or '<vide>'}"
                )

        if reference_type == "OFFICIAL_REFERENCE":
            if not is_valid_http_url(reference_location):
                errors.append(
                    f"Ligne {line_number} : une référence officielle "
                    "doit utiliser une URL HTTP ou HTTPS valide."
                )

        if reference_type == "DETERMINISTIC_RULE":
            if not reference_location.startswith(
                "INTERNAL_RULE:"
            ):
                errors.append(
                    f"Ligne {line_number} : une règle déterministe "
                    "doit être identifiée par un emplacement commençant "
                    "par INTERNAL_RULE:."
                )

        if (
            reference_type == "DETERMINISTIC_RULE"
            and not reference_version.startswith(
                "EXP001_DETERMINISTIC_RULES_"
            )
        ):
            errors.append(
                f"Ligne {line_number} : la version d’une règle "
                "déterministe doit commencer par "
                "EXP001_DETERMINISTIC_RULES_."
            )

    return errors


def validate_frozen(
    rows: list[dict[str, str]],
) -> list[str]:
    """
    Vérifie que les cas sont revus, affectés et gelés.

    Ce niveau doit être utilisé avant toute autorisation
    d'exécution expérimentale.
    """

    errors: list[str] = []

    errors.extend(
        validate_required_fields(
            rows,
            FROZEN_REQUIRED_FIELDS,
            "frozen",
        )
    )

    for line_number, row in enumerate(rows, start=2):
        split = clean(row.get("split"))
        review_status = clean(row.get("review_status"))
        reviewer_1_label = clean(
            row.get("reviewer_1_label")
        )
        reviewer_1_confidence = clean(
            row.get("reviewer_1_confidence")
        )
        reviewer_1_justification = clean(
            row.get("reviewer_1_justification")
        )
        reviewer_2_label = clean(
            row.get("reviewer_2_label")
        )
        arbitration_status = clean(
            row.get("arbitration_status")
        )
        final_label = clean(row.get("final_label"))
        freeze_status = clean(row.get("freeze_status"))
        exclusion_status = clean(
            row.get("exclusion_status")
        )

        if split == "UNASSIGNED":
            errors.append(
                f"Ligne {line_number} : le split doit être "
                "attribué avant gel."
            )

        if review_status != "APPROVED":
            errors.append(
                f"Ligne {line_number} : review_status doit être "
                "APPROVED avant gel."
            )

        if reviewer_1_label != final_label:
            errors.append(
                f"Ligne {line_number} : reviewer_1_label doit "
                "correspondre au final_label avant gel."
            )

        if not reviewer_1_confidence:
            errors.append(
                f"Ligne {line_number} : "
                "reviewer_1_confidence est obligatoire avant gel."
            )

        if not reviewer_1_justification:
            errors.append(
                f"Ligne {line_number} : "
                "reviewer_1_justification est obligatoire avant gel."
            )

        if reviewer_2_label:
            if reviewer_2_label != final_label:
                if arbitration_status != "COMPLETED":
                    errors.append(
                        f"Ligne {line_number} : un désaccord entre "
                        "reviewer_2_label et final_label exige un "
                        "arbitration_status à COMPLETED."
                    )
            elif arbitration_status == "PENDING":
                errors.append(
                    f"Ligne {line_number} : l’arbitrage ne peut pas "
                    "rester PENDING lorsque les labels concordent."
                )

        if freeze_status != "FROZEN":
            errors.append(
                f"Ligne {line_number} : freeze_status doit être "
                "FROZEN avant exécution."
            )

        if exclusion_status != "INCLUDED":
            errors.append(
                f"Ligne {line_number} : un cas EXCLUDED ne peut pas "
                "entrer dans le corpus gelé du smoke test."
            )

        for field_name in [
            "reviewer_1_label",
            "reviewer_1_confidence",
            "reviewer_1_justification",
            "final_label",
            "case_version",
            "updated_at",
            "decision_owner",
        ]:
            value = clean(row.get(field_name))

            if is_provisional(value):
                errors.append(
                    f"Ligne {line_number} : valeur provisoire "
                    f"interdite avant gel pour {field_name} : "
                    f"{value or '<vide>'}"
                )

    return errors


def validate_csv(
    csv_path: Path,
    stage: str,
) -> list[str]:
    """Exécute le niveau de validation demandé."""

    rows, errors = load_csv(csv_path)

    if errors:
        return errors

    errors.extend(validate_structural(rows))

    if stage in {"documented", "frozen"}:
        errors.extend(validate_documented(rows))

    if stage == "frozen":
        errors.extend(validate_frozen(rows))

    return errors


def parse_arguments() -> argparse.Namespace:
    """Analyse les arguments de ligne de commande."""

    parser = argparse.ArgumentParser(
        description=(
            "Valide le corpus smoke test EXP-001 "
            "sans mesurer la performance de NeoMundi."
        )
    )

    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=DEFAULT_CSV_PATH,
        help=(
            "Chemin du CSV à valider. "
            f"Valeur par défaut : {DEFAULT_CSV_PATH}"
        ),
    )

    parser.add_argument(
        "--stage",
        choices=[
            "structural",
            "documented",
            "frozen",
        ],
        default="structural",
        help=(
            "Niveau de validation : structural, "
            "documented ou frozen."
        ),
    )

    return parser.parse_args()


def print_success(stage: str) -> None:
    """Affiche le résumé d'une validation réussie."""

    print(
        "SUCCÈS — le corpus EXP-001 est valide "
        f"pour le niveau {stage}."
    )

    print("- 20 cas détectés")
    print("- 10 cas POSITIVE")
    print("- 10 cas NEGATIVE")
    print("- identifiants uniques")
    print("- valeurs autorisées respectées")
    print("- cohérence des injections vérifiée")

    if stage in {"documented", "frozen"}:
        print("- références renseignées")
        print("- références versionnées")
        print("- valeurs provisoires de référence absentes")

    if stage == "frozen":
        print("- splits attribués")
        print("- revue humaine approuvée")
        print("- labels de revue cohérents")
        print("- corpus gelé")
        print("- cas gelés inclus dans l’expérience")


def main() -> int:
    """Point d'entrée principal."""

    args = parse_arguments()

    errors = validate_csv(
        csv_path=args.csv_path,
        stage=args.stage,
    )

    if errors:
        print(
            "ÉCHEC — incohérences détectées "
            f"pour le niveau {args.stage} :"
        )

        for error in errors:
            print(f"- {error}")

        return 1

    print_success(args.stage)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
