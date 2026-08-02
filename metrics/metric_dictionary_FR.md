# Dictionnaire des métriques NeoMundi

## Objet

Ce document définit les métriques officielles NeoMundi, leur signification, leur état d’avancement, leurs limites d’interprétation et les validations nécessaires.

Une métrique ne doit pas être présentée comme validée tant que sa définition, son implémentation, sa calibration et son protocole de validation ne sont pas documentés.

---

## Statuts méthodologiques

- **Exploratoire** : concept ou signal en cours d’étude
- **Défini** : objectif et interprétation documentés
- **Implémenté** : calcul présent dans le pipeline NeoMundi
- **Testé** : calcul vérifié sur des cas contrôlés
- **Calibré** : seuils ou plages d’interprétation estimés
- **Validé** : performance mesurée contre une référence documentée
- **Répliqué** : résultat reproduit sur une autre campagne ou dans un autre environnement

---

## Fiche standard d’une métrique

Chaque métrique doit contenir :

- identifiant ;
- nom officiel ;
- version ;
- statut actuel ;
- objectif de mesure ;
- phénomène cible ;
- données d’entrée ;
- formule ou algorithme ;
- type de sortie ;
- unité ou échelle ;
- plage attendue ;
- interprétation ;
- seuils ;
- comportement en cas de données manquantes ;
- dépendances ;
- facteurs de sensibilité ;
- limites connues ;
- non-claims ;
- exemple numérique ;
- référence de validation ;
- test de validation requis ;
- emplacement de l’implémentation ;
- emplacement des preuves ;
- responsable de décision ;
- date de dernière revue.

---

# MET-001 — Score de stabilité

## Identification

- **Identifiant :** MET-001
- **Nom officiel :** Score de stabilité
- **Version :** à figer
- **Statut actuel :** implémenté — définition méthodologique à consolider

## Définition

- **Objectif :** mesurer les variations entre plusieurs exécutions d’un même cas.
- **Phénomène cible :** stabilité des réponses dans un protocole d’exécutions répétées.
- **Entrées :** à documenter depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code existant.
- **Type de sortie :** score numérique.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** à définir formellement.
- **Seuils :** non encore figés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** protocole de répétition, représentation sémantique et méthode d’agrégation.
- **Sensibilité :** modèle, prompt, paramètres, modèle d’embedding, nombre de répétitions et longueur des réponses.

## Limites

- La stabilité ne garantit pas la vérité.
- La stabilité ne garantit pas la conformité.
- Une réponse variable peut rester correcte.
- Une réponse stable peut rester systématiquement fausse.

## Validation

- **Référence :** corpus de réponses répétées revu humainement.
- **Test requis :** analyse intra-prompt et comparaison avec une baseline de similarité sémantique.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-002 — Taux de variation sémantique

## Identification

- **Identifiant :** MET-002
- **Nom officiel :** Taux de variation sémantique
- **Version :** à figer
- **Statut actuel :** implémenté — définition méthodologique à consolider

## Définition

- **Objectif :** identifier une divergence sémantique significative entre plusieurs réponses.
- **Phénomène cible :** variation du sens entre plusieurs exécutions d’un même cas.
- **Entrées :** à documenter depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code existant.
- **Type de sortie :** taux numérique ou classification.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** à définir formellement.
- **Seuils :** non encore figés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** modèle d’embedding, méthode de similarité, clustering ou seuil.
- **Sensibilité :** longueur, langue, paraphrase et version du modèle d’embedding.

## Limites

- Une variation sémantique ne constitue pas automatiquement une erreur.
- Une variation lexicale peut exister sans variation réelle du sens.
- Une formulation proche peut masquer un désaccord factuel ou logique.

## Validation

- **Référence :** corpus de variations sémantiques labellisé humainement.
- **Test requis :** matrice de confusion contre les labels humains.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-003 — Signal de risque factuel

## Identification

- **Identifiant :** MET-003
- **Nom officiel :** Signal de risque factuel
- **Nom du champ implémenté :** `factual_hallucination_score`
- **Alias historique :** `hallucination_score`
- **Version :** implémentation backend observée le 2 août 2026 au commit `f02f7ff` — seuil par défaut `0.5`
- **Statut actuel :** implémenté et rattaché à une version de code — calibration et validation méthodologique en attente

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
- **Formule ou algorithme :** évaluation par un modèle juge de type `LLM-as-Judge`. Le juge reçoit le prompt et la réponse, puis retourne un objet JSON comprenant notamment `factual_hallucination_score`, `semantic_instability_score`, `confidence`, `reasoning` et `suspect_phrases`. Le score factuel retourné est converti en nombre, borné dans l’intervalle `[0,1]` avec `clamp01`, puis arrondi à quatre décimales. La classification booléenne est produite par comparaison du score à un seuil configurable.
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
- **Seuils :** par défaut, la classification `is_hallucinated` est calculée lorsque `factual_hallucination_score >= 0.5`. Ce seuil est implémenté dans la fonction `detect_hallucination`, mais il n’est pas encore méthodologiquement calibré ni validé. Il peut être remplacé par une autre valeur lors de l’appel de la fonction.
- **Extraction des passages suspects :** le prompt du juge demande des `suspect_phrases` lorsque le score factuel est supérieur à `0.3`. Cette valeur concerne l’extraction des passages suspects et ne constitue pas le seuil par défaut de classification.
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

Cet exemple ne constitue pas un seuil recommandé, calibré ou validé.

## Limites

- Le score est produit par un modèle juge et non par une vérification factuelle déterministe.
- Le modèle juge peut produire des faux positifs et des faux négatifs.
- Un signal de risque factuel ne prouve pas qu’une réponse est fausse.
- L’absence d’alerte ne prouve pas qu’une réponse est vraie.
- Le score dépend de la configuration, de la version et du comportement du modèle juge.
- La performance peut varier selon les domaines, les langues et les types de références.
- Une réponse vide ou une indisponibilité du juge peut actuellement produire un score de repli à `0.0`.
- Le score ne doit pas être présenté comme une mesure autonome de vérité.
- Le seuil `0.5` ne doit pas être présenté comme calibré, validé ou universel.
- La séparation entre risque factuel et instabilité sémantique dépend de la capacité du juge à distinguer ces phénomènes.
- Le rattachement au commit `f02f7ff` fige l’implémentation observée pour `EXP-001`, mais ne constitue pas une validation de sa performance.

## Non-claims

- MET-003 ne certifie pas la vérité d’une réponse.
- MET-003 ne constitue pas une preuve juridique, scientifique ou experte de fausseté.
- MET-003 ne garantit pas l’absence d’hallucination lorsque le score est faible.
- MET-003 ne constitue pas une mesure universelle indépendante du modèle juge.
- MET-003 ne doit pas être utilisé seul pour autoriser ou bloquer une décision à fort impact avant calibration et validation.
- Le seuil `0.5` ne constitue pas un seuil universel ou optimal.
- Le smoke test `EXP-001` ne peut pas autoriser une affirmation générale de performance.

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
  - test du comportement en cas de réponse vide et d’indisponibilité du juge ;
  - comparaison de plusieurs seuils autour de la valeur par défaut `0.5`.
- **Implémentation :** `govern-v3/app/core/hallucination_detector.py`
- **Fonction principale :** `detect_hallucination`
- **Commit d’implémentation :** `f02f7ff`
- **Tests existants identifiés :** `govern-v3/tests/test_core/test_hallucination.py`
- **Preuves :** à produire dans `EXP-001` après gel du corpus, du seuil, de la configuration du juge et du protocole.
- **Responsable :** Sébastien.
- **Dernière revue :** 2 août 2026.

---

# MET-004 — Signal de dérive longitudinale

## Identification

- **Identifiant :** MET-004
- **Nom officiel :** Signal de dérive longitudinale
- **Version :** à figer
- **Statut actuel :** mesuré — validation à réaliser

## Définition

- **Objectif :** détecter un changement durable par rapport à une baseline gelée.
- **Phénomène cible :** évolution longitudinale entre plusieurs campagnes comparables.
- **Entrées :** à documenter.
- **Formule ou algorithme :** à documenter.
- **Type de sortie :** signal ou score.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** changement mesuré par rapport à une baseline et à un protocole définis.
- **Seuils :** à calibrer.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** stabilité du corpus, versionnage et comparabilité des campagnes.
- **Sensibilité :** changement de modèle, fournisseur, juge, corpus ou méthode d’échantillonnage.

## Limites

- Un changement ne représente pas automatiquement une dégradation.
- Une variation ponctuelle ne constitue pas nécessairement une dérive.
- La détection d’une dérive ne permet pas automatiquement de prédire une défaillance future.

## Validation

- **Référence :** campagnes répétées sur corpus fixe.
- **Test requis :** comparaison longitudinale sur plusieurs campagnes.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-005 — Delta G

## Identification

- **Identifiant :** MET-005
- **Nom officiel :** Delta G
- **Version :** à figer
- **Statut actuel :** exploratoire ou implémenté — statut exact à confirmer

## Définition

- **Objectif :** à spécifier formellement.
- **Phénomène cible :** à spécifier formellement.
- **Entrées :** à extraire depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code.
- **Type de sortie :** valeur numérique.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** non encore figée.
- **Seuils :** non encore validés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** à documenter.
- **Sensibilité :** prompt, modèle, longueur, tokenisation et configuration runtime.

## Limites

- Une valeur élevée de Delta G ne doit pas être interprétée automatiquement comme une erreur.
- La métrique ne doit pas être présentée comme une preuve thermodynamique sans validation séparée.
- Aucun seuil universel ne doit être revendiqué avant calibration multi-contextes.

## Validation

- **Référence :** à définir.
- **Test requis :** sensibilité, ablation, perturbations contrôlées et comparaison à des baselines.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

## Métriques à ajouter

Les métriques suivantes devront être ajoutées après extraction depuis le pipeline actuel :

- cohérence ;
- conformité ;
- Runtime R ;
- densité informationnelle ;
- énergie ;
- latence ;
- coût ;
- classification des régimes ;
- métriques de trajectoire ;
- métriques candidates Oracle Law E.
