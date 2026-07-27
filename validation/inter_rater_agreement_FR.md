# Protocole d’accord inter-évaluateurs NeoMundi

## 1. Objet

Ce document définit la manière dont NeoMundi mesure, interprète et documente l’accord entre plusieurs évaluateurs humains.

L’objectif est d’estimer la solidité des labels utilisés comme référence de validation.

---

## 2. Principe général

Un label humain ne doit pas être considéré comme parfaitement fiable par défaut.

Lorsque plusieurs évaluateurs interviennent, il faut mesurer :

- leur niveau d’accord ;
- la nature des désaccords ;
- la stabilité des catégories ;
- la qualité du guide d’annotation ;
- la nécessité éventuelle d’un arbitrage.

---

## 3. Conditions préalables

L’accord inter-évaluateurs ne doit être calculé que si :

- les évaluateurs utilisent le même guide ;
- les labels autorisés sont identiques ;
- l’unité d’analyse est la même ;
- les cas ont été examinés indépendamment ;
- les versions du protocole sont identiques ;
- les annotations initiales ont été conservées.

---

## 4. Évaluation indépendante

Chaque évaluateur doit annoter les cas sans connaître :

- les décisions des autres évaluateurs ;
- le signal NeoMundi ;
- le score calculé ;
- le résultat attendu ;
- l’identité du modèle lorsque cela est possible.

L’objectif est de limiter les biais de confirmation.

---

## 5. Types de labels

Les labels principaux sont :

- `POSITIVE`
- `NEGATIVE`
- `AMBIGUOUS`
- `NOT_APPLICABLE`
- `REVIEW_REQUIRED`

Les catégories utilisées pour le calcul doivent être clairement définies avant l’analyse.

---

## 6. Accord brut

L’accord brut correspond à la proportion de cas pour lesquels les évaluateurs ont attribué le même label.

> Accord brut = nombre d’accords / nombre total de cas comparables

L’accord brut est facile à comprendre, mais ne tient pas compte de l’accord obtenu par hasard.

---

## 7. Mesures statistiques possibles

Le choix de la métrique dépend du protocole.

### Cohen’s kappa

À utiliser principalement lorsque :

- deux évaluateurs interviennent ;
- les catégories sont nominales ;
- les labels sont comparables.

### Fleiss’ kappa

À utiliser principalement lorsque :

- plus de deux évaluateurs interviennent ;
- plusieurs évaluateurs annotent les mêmes cas ;
- les catégories sont nominales.

### Kappa pondéré

À utiliser lorsque les catégories possèdent un ordre naturel et que certains désaccords sont plus graves que d’autres.

### Krippendorff’s alpha

À envisager lorsque :

- le nombre d’évaluateurs varie selon les cas ;
- certaines annotations sont manquantes ;
- plusieurs types de données sont utilisés ;
- le protocole nécessite une mesure plus générale.

La métrique choisie doit être justifiée dans chaque expérience.

---

## 8. Interprétation prudente

Aucun seuil universel ne doit être appliqué sans tenir compte :

- du nombre de cas ;
- de la prévalence des catégories ;
- du nombre d’évaluateurs ;
- de la difficulté des cas ;
- de la nature de l’événement cible ;
- de la distribution des labels.

Une valeur élevée ne prouve pas automatiquement que les évaluateurs ont raison.

Une valeur faible peut révéler :

- un guide imprécis ;
- un événement cible ambigu ;
- une référence insuffisante ;
- des cas trop difficiles ;
- un manque de formation ;
- une véritable incertitude du domaine.

---

## 9. Analyse des désaccords

Chaque désaccord important doit être qualifié.

Catégories recommandées :

- définition insuffisamment précise ;
- référence contradictoire ;
- contexte manquant ;
- cas réellement ambigu ;
- erreur d’interprétation ;
- expertise insuffisante ;
- différence de seuil implicite ;
- erreur d’annotation ;
- problème de format ou de donnée.

---

## 10. Procédure d’arbitrage

L’arbitrage intervient après le calcul et la conservation des annotations initiales.

Étapes :

1. identifier les cas en désaccord ;
2. comparer les justifications ;
3. vérifier la référence ;
4. vérifier le guide ;
5. solliciter un troisième évaluateur si nécessaire ;
6. enregistrer la décision finale ;
7. documenter la justification ;
8. signaler toute modification méthodologique nécessaire.

La décision finale ne doit jamais remplacer les annotations initiales dans l’historique.

---

## 11. Cas ambigus

Les cas `AMBIGUOUS` ne doivent pas être automatiquement forcés en `POSITIVE` ou `NEGATIVE`.

Ils doivent être :

- conservés ;
- analysés séparément ;
- exclus du test principal si le protocole le prévoit ;
- éventuellement utilisés pour améliorer le guide ;
- intégrés à une étude spécifique des zones d’incertitude.

---

## 12. Taille minimale indicative

### Smoke test

- 20 à 30 cas ;
- objectif : vérifier le guide et identifier les ambiguïtés majeures.

### Première estimation

- environ 100 cas ;
- objectif : produire une première mesure d’accord.

### Validation consolidée

- plusieurs centaines de cas ;
- plusieurs catégories ;
- plusieurs évaluateurs ;
- plusieurs familles de risque.

La taille exacte dépend du protocole et de la distribution des labels.

---

## 13. Rapport minimal

Le rapport d’accord doit contenir :

- nombre de cas ;
- nombre d’évaluateurs ;
- unité d’analyse ;
- catégories utilisées ;
- accord brut ;
- métrique statistique choisie ;
- résultat ;
- distribution des labels ;
- nombre de désaccords ;
- principales causes ;
- nombre de cas arbitrés ;
- limites ;
- version du guide.

---

## 14. Critères de décision

Avant une validation formelle, il faut déterminer :

- si le niveau d’accord est suffisant ;
- si certaines catégories doivent être révisées ;
- si le guide doit être clarifié ;
- si certains cas doivent être exclus ;
- si une expertise supplémentaire est nécessaire.

La décision doit être documentée dans le journal méthodologique.

---

## 15. Limites

Un accord élevé peut provenir d’un biais partagé.

Un désaccord faible en volume peut rester important s’il concerne les cas les plus critiques.

Les métriques d’accord ne remplacent pas l’analyse qualitative des désaccords.

---

## 16. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
