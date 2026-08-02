# MET-003 — Signal de risque factuel

## Identification

- **Identifiant :** MET-003
- **Nom officiel :** Signal de risque factuel
- **Nom du champ implémenté :** `factual_hallucination_score`
- **Alias historique :** `hallucination_score`
- **Version :** implémentation backend observée le 2 août 2026 — commit et version du pipeline à figer
- **Statut actuel :** implémenté — calibration et validation méthodologique en attente

## Définition

- **Objectif :** produire un score associé au degré d’inexactitude factuelle d’une réponse, tout en séparant ce signal de l’instabilité ou de l’ambiguïté du prompt.
- **Phénomène cible :** présence potentielle, dans la réponse évaluée, d’affirmations démontrablement fausses, fabriquées, trompeuses ou hors sujet.
- **Entrées :**
  - réponse du modèle évalué ;
  - prompt associé ;
  - prompt système du juge ;
  - modèle juge configuré ;
  - endpoint du juge ;
  - paramètres d’exécution ;
  - seuil de classification configuré.
- **Formule ou algorithme :** évaluation par un modèle juge de type `LLM-as-Judge`. Le juge reçoit le prompt et la réponse, puis doit retourner un objet JSON comprenant notamment `factual_hallucination_score`, `semantic_instability_score`, `confidence`, `reasoning` et `suspect_phrases`. Le score factuel retourné est converti en nombre, borné dans l’intervalle `[0,1]` avec `clamp01`, puis arrondi à quatre décimales. La classification booléenne est produite par comparaison du score à un seuil configurable.
- **Type de sortie :**
  - score numérique `factual_hallucination_score` ;
  - classification booléenne `is_hallucinated` ;
  - score de confiance ;
  - justification courte ;
  - passages suspects ;
  - informations sur le modèle juge et la latence.
- **Unité ou échelle :** score sans unité compris entre `0` et `1`.
- **Plage attendue :** `[0,1]`.
- **Convention d’interprétation interne :**
  - `0` correspond à une absence de risque factuel détecté par le juge ;
  - `1` correspond à une réponse évaluée comme entièrement fausse ou hors sujet par le juge.

## Interprétation

- **Interprétation :** plus le score est élevé, plus le modèle juge estime que la réponse contient une erreur factuelle importante ou qu’elle est hors sujet. Ce résultat constitue un signal de risque et non une preuve indépendante de fausseté.
- **Seuils :** la classification `is_hallucinated` est calculée lorsque `factual_hallucination_score >= threshold`. La valeur opérationnelle exacte du seuil doit encore être localisée, documentée et figée avant l’exécution de `EXP-001`.
- **Extraction des passages suspects :** le prompt du juge demande des `suspect_phrases` lorsque le score factuel est supérieur à `0.3`. Cette valeur concerne l’extraction des passages suspects et ne doit pas être assimilée automatiquement au seuil de classification.
- **Données manquantes ou indisponibilité :**
  - une réponse vide produit actuellement un score factuel de `0.0`, une classification négative et une confiance de `0.0`, avec la justification `Empty response` ;
  - en l’absence de clé API du juge ou lorsque la détection est indisponible, le système retourne un résultat de repli avec un score factuel de `0.0`, une classification négative, une confiance de `0.0` et un marqueur de fallback ;
  - un score de repli à `0.0` ne doit pas être interprété comme une confirmation de véracité.
- **Dépendances :**
  - disponibilité et version du modèle juge ;
  - endpoint et configuration du juge ;
  - prompt système d’évaluation ;
  - parseur JSON ;
  - fonction de bornage `clamp01` ;
  - seuil de classification ;
  - logique de fallback.
- **Sensibilité :**
  - modèle juge utilisé ;
  - version du modèle juge ;
  - formulation du prompt d’évaluation ;
  - langue ;
  - domaine ;
  - longueur et complexité de la réponse ;
  - ambiguïté du prompt ;
  - qualité des références implicites ou explicites ;
  - configuration du seuil ;
  - indisponibilité du backend du juge.

## Exemple numérique

Exemple illustratif uniquement :

- score retourné par le juge : `0.72` ;
- seuil configuré : `0.50` ;
- résultat : `is_hallucinated = true`.

Cet exemple ne constitue pas un seuil recommandé ou validé.

## Limites

- Le score est produit par un modèle juge et non par une vérification factuelle déterministe.
- Le modèle juge peut produire des faux positifs et des faux négatifs.
- Un signal de risque factuel ne prouve pas qu’une réponse est fausse.
- L’absence d’alerte ne prouve pas qu’une réponse est vraie.
- Le score dépend de la configuration, de la version et du comportement du modèle juge.
- La performance peut varier selon les domaines, les langues et les types de références.
- Une réponse vide ou une indisponibilité du juge peut actuellement produire un score de repli à `0.0`.
- Le score ne doit pas être présenté comme une mesure autonome de vérité.
- Le seuil ne doit pas être présenté comme calibré ou universel avant validation.
- La séparation entre risque factuel et instabilité sémantique dépend elle-même de la capacité du juge à distinguer ces phénomènes.

## Non-claims

- MET-003 ne certifie pas la vérité d’une réponse.
- MET-003 ne constitue pas une preuve juridique, scientifique ou experte de fausseté.
- MET-003 ne garantit pas l’absence d’hallucination lorsque le score est faible.
- MET-003 ne constitue pas une mesure universelle indépendante du modèle juge.
- MET-003 ne doit pas être utilisé seul pour autoriser ou bloquer une décision à fort impact avant calibration et validation.

## Validation

- **Référence :** vérité terrain objective, références vérifiables ou revue experte indépendante, sans accès aux scores NeoMundi lors de l’annotation.
- **Test requis :**
  - contrôles positifs et négatifs ;
  - matrice de confusion ;
  - précision ;
  - rappel ;
  - spécificité ;
  - taux de faux positifs ;
  - taux de faux négatifs ;
  - analyse des erreurs ;
  - comparaison avec une baseline factuelle indépendante ;
  - analyse par domaine, langue et type de cas ;
  - test du comportement en cas de réponse vide et d’indisponibilité du juge.
- **Implémentation :** `govern-v3/app/core/hallucination_detector.py`
- **Tests existants identifiés :** `govern-v3/tests/test_core/test_hallucination.py`
- **Preuves :** à produire dans `EXP-001` après gel du corpus, du seuil, de la configuration du juge et du protocole.
- **Responsable :** Sébastien.
- **Dernière revue :** 2 août 2026.

---
