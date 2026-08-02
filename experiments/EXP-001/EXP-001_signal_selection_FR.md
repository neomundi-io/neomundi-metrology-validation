# EXP-001 — Sélection du signal évalué

## 1. Objet

Ce document définit le signal NeoMundi évalué dans l’expérience `EXP-001`, son rattachement au code observé, le seuil retenu pour le smoke test et les limites d’interprétation associées.

L’objectif est de figer la configuration testée avant toute exécution.

Ce gel expérimental ne constitue ni une calibration ni une validation scientifique générale de la métrique.

---

## 2. Décision

Le signal sélectionné pour l’expérience `EXP-001` est :

> le signal de risque factuel NeoMundi.

---

## 3. Identifiants associés

- **Claim :** `CLM-003`
- **Métrique ou signal :** `MET-003`
- **Événement cible :** `EVT-003`
- **Dimension principale :** factualité
- **Champ implémenté :** `factual_hallucination_score`
- **Classification implémentée :** `is_hallucinated`
- **Alias historique :** `hallucination_score`

---

## 4. Question de recherche

La question de recherche générale associée à `EXP-001` est :

> Le signal de risque factuel NeoMundi permet-il d’identifier des erreurs factuelles significatives sur un corpus documenté, avec une performance mesurable par rapport à une vérité terrain et à une baseline indépendante ?

Pour le smoke test de 20 cas, la question est limitée à :

> La chaîne expérimentale permet-elle de charger les cas, produire les sorties NeoMundi, appliquer la baseline, calculer la matrice de confusion et conserver une traçabilité complète ?

Le smoke test ne vise pas à établir une performance généralisable.

---

## 5. Événement cible

L’événement cible `EVT-003` est :

> la présence, dans une réponse, d’au moins une affirmation factuelle significativement incorrecte et susceptible de modifier la compréhension, la conclusion, la décision ou l’usage.

Les erreurs typographiques, stylistiques ou sans impact factuel significatif ne sont pas considérées comme des événements positifs.

---

## 6. Implémentation sélectionnée

L’implémentation observée pour `EXP-001` est située dans :

```text
govern-v3/app/core/hallucination_detector.py
```

La fonction principale identifiée est :

```text
detect_hallucination
```

Le mécanisme repose sur une évaluation de type :

```text
LLM-as-Judge
```

L’implémentation est rattachée à l’ancre interne suivante :

```text
f02f7ff
```

Cette référence correspond à un commit du repository backend privé NeoMundi.

Elle sert à :

- identifier la version du code observée ;
- empêcher une modification silencieuse après lecture des résultats ;
- permettre un audit interne ;
- relier les résultats du smoke test à une implémentation précise.

Cette ancre interne ne constitue pas une preuve publique autonome ni une mise à disposition du code propriétaire.

---

## 7. Sortie principale

Le signal principal est :

```text
factual_hallucination_score
```

Il s’agit d’un score numérique sans unité, borné dans l’intervalle :

```text
[0,1]
```

Convention interne observée :

- `0` : aucun risque factuel détecté par le modèle juge ;
- `1` : réponse évaluée par le modèle juge comme entièrement fausse ou hors sujet.

Cette convention décrit le comportement attendu du score. Elle ne signifie pas que le score mesure directement ou objectivement la vérité.

---

## 8. Algorithme observé

Le modèle juge reçoit notamment :

- le prompt ;
- la réponse évaluée ;
- un prompt système d’évaluation ;
- une configuration de modèle juge ;
- des paramètres d’exécution.

Il retourne un objet structuré comprenant notamment :

- `factual_hallucination_score`
- `semantic_instability_score`
- `confidence`
- `reasoning`
- `suspect_phrases`

Le score factuel est ensuite :

1. converti en valeur numérique ;
2. borné dans l’intervalle `[0,1]` par la fonction `clamp01` ;
3. arrondi à quatre décimales ;
4. comparé à un seuil configurable.

La métrique n’est donc pas une formule déterministe autonome.

Elle dépend du comportement du modèle juge et de sa configuration.

---

## 9. Seuil retenu pour le smoke test

Le seuil par défaut observé dans la fonction `detect_hallucination` est :

```text
0.5
```

La règle de classification retenue pour `EXP-001` est :

```text
is_hallucinated = factual_hallucination_score >= 0.5
```

Correspondance expérimentale :

- `is_hallucinated = true` → `SIGNAL_POSITIVE`
- `is_hallucinated = false` → `SIGNAL_NEGATIVE`

Le seuil `0.5` est figé pour le smoke test `EXP-001 v0.1`.

Il ne doit pas être modifié après consultation des résultats sans :

- création d’une nouvelle version du protocole ;
- justification méthodologique ;
- nouvelle traçabilité ;
- nouvelle exécution distincte.

Le gel du seuil pour cette expérience ne signifie pas qu’il est :

- calibré ;
- validé ;
- optimal ;
- universel ;
- adapté à tous les domaines.

---

## 10. Seuil des passages suspects

Le prompt du modèle juge demande des `suspect_phrases` lorsque le score factuel est supérieur à :

```text
0.3
```

Cette valeur concerne l’extraction des passages suspects.

Elle ne doit pas être confondue avec le seuil principal de classification `0.5`.

---

## 11. Comportement en cas d’indisponibilité

L’implémentation observée peut produire un score de repli à `0.0` dans certains cas, notamment :

- réponse vide ;
- absence de clé API du juge ;
- indisponibilité du système de détection ;
- activation d’un fallback.

Ces situations doivent être identifiées dans les sorties techniques.

Un score de repli à `0.0` ne doit pas être interprété automatiquement comme :

```text
SIGNAL_NEGATIVE
```

ni comme une confirmation de véracité.

Les statuts suivants doivent pouvoir être distingués :

```text
SIGNAL_POSITIVE
SIGNAL_NEGATIVE
SIGNAL_UNAVAILABLE
COMPUTATION_ERROR
FALLBACK_RESULT
```

---

## 12. Baseline retenue

La baseline retenue pour le smoke test est :

> une baseline déterministe indépendante fondée sur une référence factuelle documentée et versionnée.

Elle n’utilise aucun modèle juge pour produire sa décision principale sur les 20 cas.

Elle produit les classes suivantes :

```text
FACTUALLY_CORRECT
FACTUALLY_INCORRECT
UNDETERMINED
```

La baseline ne reçoit jamais :

- le score NeoMundi ;
- la classification NeoMundi ;
- Delta G ;
- les autres signaux NeoMundi ;
- les résultats runtime.

La baseline est gelée séparément dans :

```text
EXP-001_factuality_baseline_FR.md
```

---

## 13. Unité d’analyse

L’unité d’analyse est :

> une réponse individuelle associée à un cas, une référence factuelle et un label final gelé.

Chaque ligne du corpus constitue une observation indépendante.

---

## 14. Corpus du smoke test

Le smoke test repose sur :

- 20 cas synthétiques ;
- 10 cas `POSITIVE` ;
- 10 cas `NEGATIVE` ;
- 10 paires correcte/incorrecte ;
- des cas fermés ;
- des réponses courtes ;
- des références documentées ;
- des labels revus humainement.

Répartition des splits :

- `CALIBRATION` : 12 cas ;
- `VALIDATION` : 4 cas ;
- `FINAL_TEST` : 4 cas.

Le smoke test ne remplace pas le futur corpus principal de 200 cas.

---

## 15. Résultats attendus

L’expérience doit produire :

- les sorties détaillées de `MET-003` ;
- les sorties de la baseline ;
- une matrice de confusion ;
- le nombre de VP ;
- le nombre de FP ;
- le nombre de VN ;
- le nombre de FN ;
- la précision ;
- le rappel ;
- la spécificité ;
- le taux de faux positifs ;
- le taux de faux négatifs ;
- le score F1 ;
- la couverture ;
- le nombre de fallbacks ;
- le nombre d’erreurs de calcul ;
- une analyse qualitative des erreurs.

Sur 20 cas, ces résultats servent uniquement à vérifier le fonctionnement de la chaîne expérimentale.

---

## 16. Conditions de comparaison

Les sorties suivantes doivent rester séparées :

1. vérité terrain ;
2. baseline indépendante ;
3. signal NeoMundi.

Le label de vérité terrain ne doit jamais être transmis au signal testé.

Le signal NeoMundi ne doit jamais être transmis à la baseline avant que celle-ci ait produit sa décision.

Le seuil `0.5` doit être enregistré avant le run et ne peut pas être ajusté après consultation des résultats dans la même version expérimentale.

---

## 17. Limites

- Le signal repose sur un modèle juge.
- Le modèle juge peut produire des faux positifs et des faux négatifs.
- Le score ne constitue pas une mesure autonome de vérité.
- Le seuil `0.5` n’est pas calibré ni validé.
- Le corpus contient seulement 20 cas synthétiques simples.
- L’équilibre des classes est artificiel.
- Les résultats ne peuvent pas être généralisés à tous les domaines.
- Les résultats ne peuvent pas soutenir une affirmation commerciale ou scientifique générale de performance.
- Une réussite du smoke test confirme uniquement le fonctionnement technique de la chaîne expérimentale.

---

## 18. Non-claims

- `MET-003` ne certifie pas la vérité d’une réponse.
- `MET-003` ne constitue pas une preuve juridique, scientifique ou experte de fausseté.
- Un score faible ne garantit pas l’absence d’erreur factuelle.
- Un score élevé ne constitue pas à lui seul une preuve indépendante de fausseté.
- Le seuil `0.5` n’est pas universel.
- Le commit interne `f02f7ff` ne constitue pas une validation de performance.
- Le smoke test ne permet pas de revendiquer que NeoMundi détecte toutes les erreurs factuelles.

---

## 19. Gel expérimental

Pour `EXP-001 v0.1`, les éléments suivants sont figés :

- **Métrique :** `MET-003`
- **Champ :** `factual_hallucination_score`
- **Classification :** `is_hallucinated`
- **Implémentation observée :** `govern-v3/app/core/hallucination_detector.py`
- **Fonction principale :** `detect_hallucination`
- **Commit interne :** `f02f7ff`
- **Seuil expérimental :** `0.5`
- **Opérateur :** `>=`
- **Événement cible :** `EVT-003`
- **Baseline :** déterministe et indépendante
- **Corpus :** `EXP-001_smoke_test_20_cases_FR.csv`

Toute modification de l’un de ces éléments exige une nouvelle version expérimentale.

---

## 20. Décision méthodologique

- **Signal retenu :** signal de risque factuel
- **Identifiant :** `MET-003`
- **Champ implémenté :** `factual_hallucination_score`
- **Événement cible :** `EVT-003`
- **Version expérimentale :** `EXP-001 v0.1`
- **Implémentation rattachée au commit interne :** `f02f7ff`
- **Seuil figé pour le smoke test :** `0.5`
- **Seuil calibré :** non
- **Seuil validé :** non
- **Métrique validée :** non
- **Statut pour `EXP-001` :** `FROZEN`
- **Date de gel :** 2 août 2026
- **Modification après gel :** interdite sans création d’une nouvelle version
- **Exécution autorisée :** non
- **Conditions restantes :** gel du corpus, mise à jour finale du manifeste, enregistrement du commit du repository expérimental, enregistrement de l’environnement et réussite de la validation `frozen`
- **Responsable du gel :** Sébastien
- **Dernière revue :** 2 août 2026
