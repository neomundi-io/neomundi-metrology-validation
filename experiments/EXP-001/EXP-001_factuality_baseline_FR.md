# EXP-001 — Baseline de factualité

## 1. Objet

Ce document définit la baseline utilisée pour comparer le signal de risque factuel NeoMundi.

La baseline doit rester :

- simple ;
- indépendante des signaux NeoMundi additionnels ;
- reproductible ;
- compréhensible par un tiers ;
- applicable au même corpus que NeoMundi.

---

## 2. Décision initiale

La baseline principale retenue pour l’EXP-001 est :

> une évaluation de factualité fondée sur une référence vérifiée et une décision binaire indépendante.

Pour chaque réponse, la baseline doit produire :

- `FACTUALLY_CORRECT`
- `FACTUALLY_INCORRECT`
- `UNDETERMINED`

---

## 3. Principe de fonctionnement

La réponse est comparée à une référence de validation versionnée.

La baseline vérifie uniquement :

> la présence ou l’absence d’une erreur factuelle significative.

Elle ne doit pas intégrer :

- la stabilité inter-répétitions ;
- la variation sémantique ;
- Delta G ;
- les métriques de trajectoire ;
- les signaux runtime ;
- la combinaison multi-signaux NeoMundi.

---

## 4. Références autorisées

Selon le type de cas, la référence peut être :

- une réponse mathématique exacte ;
- une donnée contenue dans une source officielle ;
- une information explicitement présente dans le corpus ;
- une réponse de référence gelée ;
- une règle factuelle déterministe ;
- une validation experte documentée.

Chaque référence doit être identifiable et versionnée.

---

## 5. Règle de décision

### FACTUALLY_INCORRECT

La réponse contient au moins une affirmation factuelle significative contredisant la référence autorisée.

### FACTUALLY_CORRECT

Aucune affirmation factuelle significative ne contredit la référence autorisée.

### UNDETERMINED

La référence ne permet pas de conclure avec une confiance suffisante.

Les cas `UNDETERMINED` ne doivent pas être intégrés automatiquement dans la matrice de confusion principale.

---

## 6. Significativité de l’erreur

Une erreur est considérée comme significative lorsqu’elle peut modifier :

- la compréhension du cas ;
- la conclusion ;
- la décision ;
- la recommandation ;
- l’usage opérationnel ;
- l’évaluation du risque.

Les erreurs typographiques ou stylistiques sans impact factuel ne sont pas considérées comme positives.

---

## 7. Unité d’analyse

L’unité d’analyse retenue est :

> une réponse individuelle associée à un cas et à une référence de validation.

Chaque réponse est évaluée séparément, même lorsqu’elle appartient à un groupe de répétitions.

---

## 8. Implémentation envisagée

La baseline peut être appliquée selon deux modalités.

### Baseline déterministe

Pour les cas fermés et objectivement vérifiables :

- comparaison exacte ;
- règle logique ;
- calcul ;
- correspondance avec une valeur attendue.

### Baseline par juge de factualité

Pour les cas nécessitant une interprétation :

- prompt de jugement versionné ;
- modèle juge versionné ;
- température contrôlée ;
- réponse structurée ;
- justification courte ;
- possibilité de revue humaine.

Les deux modalités doivent être distinguées dans les résultats.

---

## 9. Indépendance vis-à-vis de NeoMundi

La baseline ne doit pas recevoir :

- le score NeoMundi ;
- la classe NeoMundi ;
- Delta G ;
- les signaux de stabilité ;
- les résultats longitudinaux ;
- les décisions produites par le pipeline NeoMundi.

La baseline doit évaluer la factualité indépendamment.

---

## 10. Sortie minimale

Chaque décision de baseline doit contenir :

- identifiant du cas ;
- identifiant de la réponse ;
- référence utilisée ;
- méthode appliquée ;
- résultat ;
- niveau de confiance ;
- justification ;
- version de la baseline ;
- date ;
- statut de revue humaine.

---

## 11. Méthodes comparées dans l’EXP-001

L’expérience comparera :

1. baseline de factualité seule ;
2. signal NeoMundi seul ;
3. baseline de factualité + signaux NeoMundi.

La troisième configuration servira à mesurer la valeur incrémentale éventuelle de NeoMundi.

---

## 12. Critères d’équité

Les trois méthodes doivent être comparées sur :

- le même corpus ;
- la même vérité terrain ;
- les mêmes cas ;
- la même unité d’analyse ;
- le même jeu de test final ;
- les mêmes règles d’exclusion.

---

## 13. Limites

La baseline peut produire des erreurs.

Un modèle juge peut :

- halluciner ;
- mal interpréter la référence ;
- être sensible à la formulation ;
- varier entre plusieurs exécutions ;
- être influencé par son propre corpus d’entraînement.

La baseline ne doit donc pas être considérée automatiquement comme la vérité terrain.

La vérité terrain reste séparée de la méthode évaluée.

---

## 14. Décision méthodologique

- **Baseline principale :** évaluation de factualité indépendante fondée sur une référence vérifiée
- **Unité d’analyse :** réponse individuelle
- **Sorties :** correcte, incorrecte ou indéterminée
- **Statut :** DRAFT
- **Exécution autorisée :** non
- **Prochaine étape :** définir la structure du corpus de contrôle de l’EXP-001
- **Responsable :** Sébastien
- **Date :** 27 juillet 2026
