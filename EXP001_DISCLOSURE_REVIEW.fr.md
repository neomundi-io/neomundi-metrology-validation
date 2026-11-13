# EXP-001 — Revue des divulgations historiques et de la provenance

**Date :** 13 novembre 2026. **Statut :** revue documentaire, sans modification de l'expérience figée.

**Source :** [manifeste EXP-001](experiments/EXP-001/EXP-001_smoke_test_run_manifest.json).

## Éléments vérifiés

Le manifeste historique public contient une URL complète d'API d'inférence avec identifiant de chemin de service/compte, un alias de modèle évaluateur, des noms de variables de configuration, la température du juge, des détails de format et d'analyse de réponse, des seuils expérimentaux et des références à l'implémentation privée.

**Ce n'est pas une preuve d'exposition de clé d'accès.** Aucun jeton ni secret d'authentification n'a été identifié dans les champs examinés. L'historique Git, les pièces jointes et la configuration actuelle n'ont pas fait l'objet d'un balayage exhaustif.

## Portée

L'URL est une référence historique d'infrastructure, pas une preuve de disponibilité actuelle. Les seuils et paramètres contribuent à la reproductibilité de l'expérience figée ; ils ne sont ni des seuils universels calibrés ni une attestation de la production actuelle.

**Décision : préserver le manifeste figé.** Une suppression silencieuse ferait perdre la fidélité de la provenance sans effacer l'historique Git. Pour les *futures* publications, examiner les chemins complets de service et les paramètres internes et privilégier, lorsque scientifiquement suffisant, une description de service et des empreintes de configuration. Si les détails sont indispensables à la réplication, envisager un accès contrôlé autorisé et une version publique explicitement expurgée.

## Contrôles encore nécessaires

1. Vérifier, sans publier l'information sensible, si le chemin historique reste actif.
2. Chercher les véritables secrets et données confidentielles dans les contenus publics et l'historique.
3. Vérifier les affirmations de production sur des observations récentes autorisées.
4. Évaluer les conséquences scientifiques et d'intégrité avant toute restriction d'un artefact existant.

[Politique de divulgation](PUBLIC_DISCLOSURE_POLICY.fr.md) · [English review](EXP001_DISCLOSURE_REVIEW.md)
