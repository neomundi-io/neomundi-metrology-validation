# EXP-001 — Baseline de factualité

## 1. Objet

Ce document définit la baseline factuelle indépendante utilisée dans le smoke test de l’expérience `EXP-001`.

La baseline sert à comparer les sorties du signal NeoMundi `MET-003` à une décision factuelle produite sans accès :

- au score NeoMundi ;
- à la classification NeoMundi ;
- aux autres métriques NeoMundi ;
- aux résultats runtime ;
- aux résultats longitudinaux.

La baseline ne constitue pas automatiquement la vérité terrain. Elle est une méthode indépendante évaluée sur une vérité terrain préalablement documentée et gelée.

---

## 2. Décision méthodologique

Pour le smoke test de 20 cas, la baseline retenue est :

> une baseline déterministe fondée sur une référence factuelle documentée et une règle de décision binaire reproductible.

Aucun modèle juge n’est utilisé pour produire la décision principale de baseline sur ces 20 cas.

La revue humaine intervient uniquement pour :

- vérifier la référence ;
- confirmer la règle de décision ;
- confirmer le label attendu ;
- documenter les éventuels désaccords ;
- autoriser le gel du corpus.

---

## 3. Justification du choix

Les 20 cas du smoke test sont :

- synthétiques ;
- fermés ;
- courts ;
- objectivement vérifiables ;
- construits en 10 paires ;
- composés d’une réponse correcte et d’une réponse contenant une erreur injectée.

Les familles couvertes sont :

- géographie ;
- mathématiques ;
- sciences ;
- histoire ;
- connaissances générales.

Les erreurs injectées sont explicites et ne nécessitent pas d’interprétation complexe.

Une baseline déterministe est donc :

- suffisante pour ce smoke test ;
- plus simple à reproduire ;
- indépendante d’un second modèle juge ;
- moins exposée à la variabilité d’un évaluateur automatique ;
- adaptée à une première vérification du comportement de `MET-003`.

---

## 4. Unité d’analyse

L’unité d’analyse est :

> une réponse individuelle associée à un cas, une référence factuelle et un label attendu.

Chaque ligne du corpus constitue une observation indépendante.

Les réponses appartenant à une même paire restent évaluées séparément.

---

## 5. Phénomène évalué

La baseline vérifie uniquement :

> la présence ou l’absence d’au moins une erreur factuelle significative dans la réponse.

Elle n’évalue pas :

- la qualité stylistique ;
- la complétude générale ;
- la pertinence conversationnelle au-delà du fait demandé ;
- la stabilité entre répétitions ;
- la variation sémantique ;
- Delta G ;
- la densité informationnelle ;
- les régimes ;
- les trajectoires ;
- les autres signaux runtime NeoMundi.

---

## 6. Sorties de la baseline

La baseline produit l’une des classes suivantes :

- `FACTUALLY_CORRECT`
- `FACTUALLY_INCORRECT`
- `UNDETERMINED`

### `FACTUALLY_CORRECT`

La réponse ne contient aucune affirmation factuelle significative contredisant la référence gelée.

### `FACTUALLY_INCORRECT`

La réponse contient au moins une affirmation factuelle significative contredisant la référence gelée.

### `UNDETERMINED`

La référence, la formulation du cas ou les informations disponibles ne permettent pas de produire une décision suffisamment fiable.

Les cas `UNDETERMINED` sont exclus de la matrice de confusion principale et analysés séparément.

---

## 7. Correspondance avec les labels du corpus

Dans le corpus `EXP-001` :

- `NEGATIVE` signifie que l’événement cible `EVT-003` est absent ;
- `POSITIVE` signifie que l’événement cible `EVT-003` est présent.

La correspondance attendue est donc :

| Label du corpus | Décision de baseline |
|---|---|
| `NEGATIVE` | `FACTUALLY_CORRECT` |
| `POSITIVE` | `FACTUALLY_INCORRECT` |

Cette correspondance doit être vérifiée avant le gel du corpus.

---

## 8. Références utilisées

Deux types de références sont autorisés dans le smoke test.

### 8.1 Règle déterministe

Elle est utilisée pour les cas dont la réponse peut être vérifiée par :

- un calcul exact ;
- une propriété mathématique ;
- une conversion fixe ;
- une règle logique non ambiguë.

Type enregistré :

```text
DETERMINISTIC_RULE
```

### 8.2 Référence factuelle officielle ou institutionnelle

Elle est utilisée pour les cas de géographie, d’histoire, de sciences ou de connaissances générales.

Type enregistré :

```text
OFFICIAL_REFERENCE
```

Chaque cas doit contenir avant gel :

- une localisation de référence ;
- une version ou une date de consultation ;
- une justification du label ;
- un responsable de validation.

Les valeurs provisoires suivantes ne sont pas autorisées dans le corpus gelé :

```text
TO_BE_DOCUMENTED
TO_BE_DEFINED
```

---

## 9. Règle d’exécution

Pour chaque cas :

1. charger le prompt ;
2. charger la réponse ;
3. charger la référence gelée ;
4. appliquer la règle déterministe associée ;
5. produire la classe de baseline ;
6. enregistrer la justification ;
7. enregistrer la version de la baseline ;
8. enregistrer le statut de revue ;
9. comparer le résultat au label final gelé.

La baseline ne reçoit jamais la sortie NeoMundi avant d’avoir produit sa décision.

---

## 10. Règle de décision pour les 20 cas

La décision est produite en comparant l’élément factuel central de la réponse à la valeur attendue.

Exemples :

- `Paris` attendu, `Paris` observé : `FACTUALLY_CORRECT`
- `Paris` attendu, `Lyon` observé : `FACTUALLY_INCORRECT`
- `4` attendu, `5` observé : `FACTUALLY_INCORRECT`
- `H2O` attendu, `H2O` observé : `FACTUALLY_CORRECT`

La comparaison peut être normalisée pour traiter :

- la casse ;
- les espaces ;
- les signes de ponctuation ;
- les variantes typographiques sans impact factuel.

La normalisation ne doit pas modifier le sens de la réponse.

---

## 11. Significativité de l’erreur

Une erreur est significative lorsqu’elle modifie l’information centrale demandée, notamment :

- une entité ;
- une valeur ;
- une date ;
- une quantité ;
- une formule ;
- une catégorie ;
- une relation factuelle.

Les variations suivantes ne sont pas considérées comme des erreurs factuelles significatives :

- différence de casse ;
- variation de ponctuation ;
- variante typographique ;
- reformulation équivalente ;
- ajout stylistique sans contradiction factuelle.

---

## 12. Revue humaine

Avant le gel, chaque cas doit faire l’objet d’une vérification humaine.

Pour ce smoke test déterministe, une revue principale est suffisante lorsque :

- la référence est objective ;
- la règle est non ambiguë ;
- le label est évident ;
- aucune interprétation experte n’est requise.

Une seconde revue ou un arbitrage est requis lorsque :

- la référence est contestable ;
- le prompt est ambigu ;
- la réponse comporte plusieurs affirmations ;
- le label ne peut pas être confirmé directement.

Les évaluateurs ne doivent pas consulter les scores NeoMundi pendant la revue des labels.

---

## 13. Sortie minimale

Chaque résultat de baseline doit contenir :

- `case_id`
- `response_id`
- `reference_type`
- `reference_location`
- `reference_version`
- `baseline_method`
- `baseline_result`
- `baseline_confidence`
- `baseline_justification`
- `baseline_version`
- `review_status`
- `reviewer_id`
- `review_date`
- `execution_timestamp`

---

## 14. Comparaisons prévues

L’expérience compare :

1. la décision de `MET-003` à la vérité terrain gelée ;
2. la décision de la baseline déterministe à la vérité terrain gelée ;
3. les erreurs respectives des deux méthodes.

Une configuration combinant la baseline et les signaux NeoMundi pourra être étudiée séparément comme :

> une configuration augmentée ou un système composite.

Elle ne constitue pas la baseline indépendante utilisée pour mesurer `MET-003`.

---

## 15. Critères d’équité

Les méthodes comparées doivent utiliser :

- le même corpus gelé ;
- les mêmes unités d’analyse ;
- les mêmes labels finaux ;
- les mêmes règles d’inclusion ;
- les mêmes règles d’exclusion ;
- la même version du corpus ;
- la même fenêtre d’exécution lorsque cela est applicable.

---

## 16. Limites

- Le corpus ne contient que 20 cas synthétiques simples.
- Les résultats ne permettent pas de conclure sur des cas ouverts ou complexes.
- Les résultats ne permettent pas de généraliser à tous les domaines.
- Les résultats ne suffisent pas à calibrer définitivement le seuil `0.5`.
- Une réussite sur ce smoke test ne constitue pas une validation scientifique de `MET-003`.
- Une baseline déterministe adaptée à ces cas ne sera pas nécessairement adaptée à un corpus naturel.
- L’équilibre de 10 cas positifs et 10 cas négatifs est artificiel et ne représente pas une prévalence réelle.

---

## 17. Conditions avant exécution

L’exécution de la baseline n’est autorisée qu’après :

- documentation des 20 références ;
- versionnage des références ;
- confirmation des 20 labels ;
- validation du champ `final_label` ;
- attribution du split ;
- finalisation du statut de revue ;
- suppression des valeurs provisoires bloquantes ;
- calcul du hash du corpus ;
- gel du corpus ;
- gel de la baseline ;
- gel du protocole ;
- enregistrement du commit GitHub ;
- activation de l’autorisation d’exécution.

---

## 18. Décision finale

- **Baseline principale :** baseline déterministe indépendante
- **Corpus concerné :** `EXP-001_smoke_test_20_cases_FR.csv`
- **Nombre de cas :** 20
- **Cas positifs :** 10
- **Cas négatifs :** 10
- **Modèle juge utilisé par la baseline :** aucun
- **Revue humaine :** obligatoire avant gel
- **Statut :** `DRAFT`
- **Exécution autorisée :** non
- **Prochaine étape :** documenter et versionner les références des 20 cas
- **Responsable :** Sébastien
- **Dernière revue :** 2 août 2026
