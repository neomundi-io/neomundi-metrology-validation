# Dimensions d’évaluation NeoMundi

## 1. Objet

Ce document définit les principales dimensions observées ou évaluées par NeoMundi.

L’objectif est d’éviter qu’un même score ou une même alerte mélange plusieurs phénomènes différents.

---

## 2. Principe général

Les dimensions suivantes doivent être distinguées :

- factualité ;
- cohérence interne ;
- stabilité ;
- variation sémantique ;
- respect des instructions ;
- conformité à une règle ;
- robustesse ;
- dérive longitudinale ;
- efficacité runtime ;
- risque contextuel.

Une réponse peut être :

- stable mais fausse ;
- variable mais correcte ;
- cohérente mais non conforme ;
- conforme à la consigne mais factuellement erronée ;
- correcte mais inefficace en ressources.

---

## 3. Factualité

### Définition

La factualité concerne la correspondance entre les affirmations produites et une référence vérifiable.

### Question associée

> Les affirmations contenues dans la réponse sont-elles exactes selon la référence définie ?

### Références possibles

- vérité terrain objective ;
- source documentaire ;
- base de connaissances ;
- expertise humaine.

### Limite

La factualité ne mesure pas la stabilité, la conformité ni la qualité globale de la réponse.

---

## 4. Cohérence interne

### Définition

La cohérence interne concerne l’absence de contradiction logique ou sémantique au sein d’une même réponse.

### Question associée

> La réponse reste-t-elle compatible avec elle-même du début à la fin ?

### Limite

Une réponse peut être parfaitement cohérente tout en étant fausse.

---

## 5. Stabilité inter-répétitions

### Définition

La stabilité mesure la constance des réponses produites lors de plusieurs exécutions comparables d’un même cas.

### Question associée

> Le système produit-il des résultats similaires lorsque le même cas est répété ?

### Limite

Une réponse stable peut être systématiquement incorrecte.

---

## 6. Variation sémantique

### Définition

La variation sémantique mesure les différences de sens entre plusieurs réponses.

### Question associée

> Les réponses répétées expriment-elles la même conclusion ou des conclusions différentes ?

### Limite

Une variation de formulation ne constitue pas nécessairement une variation de sens.

---

## 7. Respect des instructions

### Définition

Le respect des instructions concerne la capacité du système à suivre les consignes explicites contenues dans la requête.

### Question associée

> La réponse respecte-t-elle les contraintes et demandes formulées ?

### Limite

Une réponse peut respecter la consigne tout en étant factuellement incorrecte.

---

## 8. Conformité à une règle

### Définition

La conformité concerne le respect d’une règle externe déclarée.

### Exemples

- politique interne ;
- règle métier ;
- procédure ;
- contrat de gouvernance ;
- contrainte réglementaire explicitement traduite en règle testable.

### Question associée

> La réponse ou l’action respecte-t-elle la règle applicable ?

### Limite

NeoMundi peut tracer l’application d’une règle sans prouver que cette règle est juridiquement suffisante ou légitime.

---

## 9. Robustesse

### Définition

La robustesse concerne la capacité d’un système à maintenir un comportement attendu malgré des variations contrôlées.

### Variations possibles

- reformulation du prompt ;
- bruit ;
- ordre des informations ;
- longueur ;
- changement mineur de contexte ;
- paramètres d’exécution.

### Limite

La robustesse doit être définie par rapport à une perturbation et à un résultat attendu précis.

---

## 10. Dérive longitudinale

### Définition

La dérive longitudinale correspond à un changement durable observé entre plusieurs campagnes comparables.

### Question associée

> Le comportement du système a-t-il changé de manière persistante par rapport à une baseline gelée ?

### Limite

Une variation ponctuelle ne constitue pas automatiquement une dérive.

---

## 11. Efficacité runtime

### Définition

L’efficacité runtime concerne les ressources mobilisées pour produire une réponse.

### Exemples

- tokens ;
- latence ;
- coût ;
- énergie estimée ;
- longueur de génération ;
- densité informationnelle.

### Limite

Une réponse plus courte ou moins coûteuse n’est pas automatiquement meilleure.

---

## 12. Risque contextuel

### Définition

Le risque contextuel dépend de l’usage, du domaine, des conséquences possibles et de l’environnement de décision.

### Exemples

- médical ;
- juridique ;
- financier ;
- cybersécurité ;
- ressources humaines ;
- décision à fort impact.

### Limite

Un même signal peut avoir une gravité différente selon le contexte d’utilisation.

---

## 13. Règle de séparation

Chaque métrique doit être reliée à une dimension principale.

Une métrique ne doit pas être utilisée pour conclure sur une autre dimension sans validation spécifique.

Exemple :

> Une métrique de stabilité ne doit pas être présentée comme une métrique de vérité.

---

## 14. Cas multidimensionnels

Une observation peut recevoir plusieurs évaluations indépendantes.

Exemple :

| Dimension | Résultat |
|---|---|
| Factualité | Incorrecte |
| Cohérence | Cohérente |
| Stabilité | Stable |
| Respect des instructions | Conforme |
| Risque contextuel | Élevé |

Les résultats ne doivent pas être fusionnés dans un verdict unique sans règle d’agrégation explicitement définie.

---

## 15. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
