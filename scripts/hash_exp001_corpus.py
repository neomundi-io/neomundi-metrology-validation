#!/usr/bin/env python3
"""
Calcule le hash SHA-256 du corpus smoke test EXP-001.

Ce script ne modifie aucun fichier.
Il lit le corpus en mode binaire et affiche :

- le chemin du fichier ;
- sa taille en octets ;
- son hash SHA-256.

Usage par défaut :

    python scripts/hash_exp001_corpus.py

Avec un autre fichier :

    python scripts/hash_exp001_corpus.py chemin/vers/fichier.csv
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


DEFAULT_CORPUS_PATH = Path(
    "experiments/EXP-001/"
    "EXP-001_smoke_test_20_cases_FR.csv"
)

READ_CHUNK_SIZE = 1024 * 1024


def calculate_sha256(file_path: Path) -> str:
    """Calcule le SHA-256 exact d’un fichier lu en mode binaire."""

    digest = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(READ_CHUNK_SIZE):
            digest.update(chunk)

    return digest.hexdigest()


def parse_arguments() -> argparse.Namespace:
    """Analyse les arguments de ligne de commande."""

    parser = argparse.ArgumentParser(
        description=(
            "Calcule le hash SHA-256 du corpus smoke test EXP-001."
        )
    )

    parser.add_argument(
        "file_path",
        nargs="?",
        type=Path,
        default=DEFAULT_CORPUS_PATH,
        help=(
            "Fichier à hasher. "
            f"Valeur par défaut : {DEFAULT_CORPUS_PATH}"
        ),
    )

    return parser.parse_args()


def main() -> int:
    """Point d’entrée principal."""

    args = parse_arguments()
    file_path: Path = args.file_path

    if not file_path.exists():
        print(
            f"ERREUR — fichier introuvable : {file_path}",
            file=sys.stderr,
        )
        return 1

    if not file_path.is_file():
        print(
            f"ERREUR — le chemin n’est pas un fichier : {file_path}",
            file=sys.stderr,
        )
        return 1

    try:
        sha256 = calculate_sha256(file_path)
        file_size = file_path.stat().st_size
    except OSError as error:
        print(
            f"ERREUR — impossible de lire le fichier : {error}",
            file=sys.stderr,
        )
        return 1

    print("SUCCÈS — hash du corpus EXP-001 calculé.")
    print(f"Fichier : {file_path.as_posix()}")
    print(f"Taille : {file_size} octets")
    print("Algorithme : SHA-256")
    print(f"SHA-256 : {sha256}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
