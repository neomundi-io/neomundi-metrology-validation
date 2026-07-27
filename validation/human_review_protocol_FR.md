# Protocole de revue humaine NeoMundi

## 1. Objet

Ce document définit la manière dont les observations NeoMundi doivent être examinées, annotées, arbitrées et tracées par des évaluateurs humains.

L’objectif est de produire des décisions suffisamment cohérentes, explicites et reproductibles pour servir de référence de validation.

---

## 2. Principe général

La revue humaine ne doit pas chercher à confirmer les signaux NeoMundi.

Elle doit évaluer indépendamment la présence ou l’absence de l’événement cible.

Dans la mesure du possible, l’évaluateur ne doit pas connaître :

- le signal produit par NeoMundi ;
- le score calculé ;
- le seuil appliqué ;
- l’identité du modèle ou du fournisseur ;
- l’hypothèse attendue par l’équipe.

---

## 3. Unité de revue

L’unité examinée doit être définie avant le début de l’annotation.

Elle peut correspondre à :

- une observation unique ;
- un ensemble de répétitions d’un même cas ;
- une trajectoire longitudinale ;
- une paire de réponses ;
- une réponse comparée à une référence ;
- un événement de gouvernance.

Le protocole doit préciser quelle unité est utilisée pour chaque expérience.

---

## 4. Informations accessibles à l’évaluateur

L’évaluateur peut recevoir uniquement les informations nécessaires à sa décision.

Selon le protocole :

- le prompt ;
- la réponse ;
- la référence de validation ;
- la règle applicable ;
- les répétitions associées ;
- le contexte d’usage ;
- les métadonnées strictement nécessaires.

Les informations non nécessaires doivent être masquées.

---

## 5. Informations à masquer lorsque possible

Pour limiter les biais, il est recommandé de masquer :

- le nom du modèle ;
- le fournisseur ;
- le profil désidentifié ;
- le score NeoMundi ;
- la classification NeoMundi ;
- les résultats des autres évaluateurs ;
- la réponse attendue par l’équipe ;
- le statut positif ou négatif du contrôle.

---

## 6. Tâche de l’évaluateur

Pour chaque cas, l’évaluateur doit :

1. lire l’événement cible ;
2. examiner les éléments disponibles ;
3. consulter uniquement les références autorisées ;
4. attribuer un label ;
5. indiquer son niveau de confiance ;
6. fournir une justification courte ;
7. signaler toute ambiguïté ;
8. indiquer si une expertise supplémentaire est nécessaire.

---

## 7. Labels autorisés

Les labels principaux sont :

- `POSITIVE`
- `NEGATIVE`
- `AMBIGUOUS`
- `NOT_APPLICABLE`
- `REVIEW_REQUIRED`

Aucun autre label ne doit être ajouté pendant l’expérience sans modification versionnée du protocole.

---

## 8. Niveaux de confiance

### HIGH

La décision est directement vérifiable ou très solidement établie.

### MEDIUM

La décision est raisonnablement solide, mais comporte une part d’interprétation.

### LOW

La décision est incertaine, dépendante du contexte ou insuffisamment documentée.

Les cas avec un niveau `LOW` doivent être revus avant intégration dans le jeu de test final.

---

## 9. Justification attendue

La justification doit être courte, factuelle et reliée à la référence.

Exemple acceptable :

> La date indiquée dans la réponse contredit la source de référence versionnée.

Exemple insuffisant :

> La réponse semble mauvaise.

L’évaluateur ne doit pas commenter la qualité générale du modèle si cela ne relève pas de l’événement cible.

---

## 10. Évaluation indépendante

Pour les cas non objectifs, au moins deux évaluateurs indépendants sont recommandés.

Chaque évaluateur doit produire son annotation sans consulter celle de l’autre.

Les annotations initiales doivent être conservées, même après arbitrage.

---

## 11. Désaccord entre évaluateurs

Un désaccord doit être classé selon sa cause probable :

- définition imprécise ;
- référence insuffisante ;
- ambiguïté réelle du cas ;
- différence d’interprétation ;
- erreur d’un évaluateur ;
- expertise insuffisante ;
- information manquante.

Le désaccord ne doit pas être résolu par simple vote automatique lorsque le cas reste ambigu.

---

## 12. Procédure d’arbitrage

L’arbitrage doit suivre les étapes suivantes :

1. conserver les annotations initiales ;
2. comparer les justifications ;
3. vérifier la référence ;
4. vérifier la clarté du guide ;
5. solliciter un troisième évaluateur si nécessaire ;
6. attribuer une décision finale ;
7. documenter la justification ;
8. indiquer si le protocole doit être modifié.

L’arbitre ne doit pas modifier les annotations initiales.

---

## 13. Cas nécessitant une expertise

Certains domaines peuvent exiger une expertise spécifique :

- médical ;
- juridique ;
- financier ;
- cybersécurité ;
- ressources humaines ;
- réglementation sectorielle.

Ces cas ne doivent pas être arbitrés par une personne non qualifiée lorsque la décision dépend réellement de cette expertise.

---

## 14. Contrôle qualité des annotations

Le contrôle qualité peut inclure :

- cas dupliqués ;
- contrôles évidents ;
- vérification de cohérence interne ;
- revue d’un échantillon aléatoire ;
- mesure du temps d’annotation ;
- détection des annotations trop rapides ;
- révision des cas à faible confiance.

Les contrôles ne doivent pas servir à piéger les évaluateurs, mais à vérifier la qualité du processus.

---

## 15. Accord inter-évaluateurs

L’accord doit être calculé uniquement sur des labels comparables.

Le rapport doit préciser :

- le nombre de cas ;
- le nombre d’évaluateurs ;
- la métrique d’accord choisie ;
- le résultat ;
- les catégories les plus conflictuelles ;
- les causes principales de désaccord.

Un accord faible doit déclencher une revue du guide ou de l’événement cible avant toute conclusion sur la performance du signal.

---

## 16. Traçabilité minimale

Chaque annotation doit contenir :

- identifiant de l’annotation ;
- identifiant de l’observation ou du cas ;
- identifiant de l’événement cible ;
- label ;
- niveau de confiance ;
- justification ;
- référence utilisée ;
- identifiant de l’évaluateur ;
- date ;
- version du guide ;
- statut d’arbitrage ;
- décision finale éventuelle.

---

## 17. Règles d’intégrité

Il est interdit de :

- modifier une annotation initiale sans trace ;
- supprimer un désaccord ;
- révéler les scores NeoMundi avant la décision lorsque l’aveuglement est prévu ;
- ajuster les labels pour améliorer artificiellement les résultats ;
- exclure un cas difficile sans justification ;
- modifier le guide sans changement de version.

---

## 18. Limites

Une revue humaine peut contenir des erreurs.

Un consensus humain ne constitue pas automatiquement une vérité objective.

La qualité des labels dépend :

- de la définition de l’événement cible ;
- de la qualité des références ;
- de la compétence des évaluateurs ;
- de la clarté du guide ;
- du contexte disponible.

---

## 19. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
