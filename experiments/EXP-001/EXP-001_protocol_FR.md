# EXP-001 — Validation initiale d’un signal NeoMundi

## 1. Identification

- **Identifiant :** EXP-001
- **Titre :** Validation initiale d’un signal NeoMundi contre une baseline simple
- **Version :** v0.1
- **Statut :** DRAFT
- **Responsable :** Sébastien
- **Date de création :** 27 juillet 2026

---

## 2. Objectif

Cette expérience constitue la première validation méthodologique formelle d’un signal NeoMundi.

Elle doit permettre de vérifier si un signal NeoMundi détecte un événement cible mieux qu’une baseline simple, sur un corpus labellisé et gelé.

---

## 3. Signal candidat

Le signal exact n’est pas encore définitivement sélectionné.

Candidats possibles :

- signal de risque factuel ;
- variation sémantique ;
- stabilité inter-répétitions.

Le choix final doit être enregistré avant le gel du protocole.

---

## 4. Question de recherche

> Le signal NeoMundi sélectionné permet-il de détecter l’événement cible avec une performance supérieure ou complémentaire à une baseline simple ?

---

## 5. Claim associé

- **Claim principal :** à sélectionner dans `claims_registry_FR.csv`
- **Statut actuel :** à confirmer
- **Formulation autorisée avant test :** signal en cours de validation
- **Formulation interdite :** capacité validée ou supériorité démontrée

---

## 6. Hypothèses

### Hypothèse principale

Le signal NeoMundi apporte une valeur mesurable par rapport à la baseline sélectionnée.

### Hypothèse nulle

Le signal NeoMundi n’apporte aucune amélioration mesurable par rapport à la baseline.

### Hypothèse secondaire

La combinaison baseline + NeoMundi apporte davantage de valeur que chaque méthode utilisée séparément.

---

## 7. Événement cible

À sélectionner dans :

`validation/target_events_registry_FR.md`

L’événement cible devra être figé avant la construction du corpus.

---

## 8. Unité d’analyse

À choisir parmi :

- une observation ;
- une réponse ;
- un groupe de répétitions ;
- un cas complet.

L’unité retenue ne devra plus changer après le gel du protocole.

---

## 9. Corpus initial

### Niveau prévu

Première estimation expérimentale.

### Taille cible

- 100 cas positifs ;
- 100 cas négatifs ;
- cas ambigus séparés.

### Composition

Le corpus devra inclure :

- plusieurs niveaux de difficulté ;
- plusieurs modèles ou profils lorsque possible ;
- des contrôles naturels ;
- des contrôles injectés ;
- des références documentées.

---

## 10. Répartition des données

Proposition initiale :

- 60 % calibration ;
- 20 % validation ;
- 20 % test final.

La répartition définitive devra être gelée avant l’exécution.

Aucun seuil ne devra être ajusté sur le jeu de test final.

---

## 11. Baseline

La baseline doit être simple, compréhensible et reproductible.

Exemples selon le signal choisi :

- similarité sémantique seule ;
- factualité seule ;
- seuil simple ;
- règle déterministe ;
- juge unique sans combinaison NeoMundi.

---

## 12. Méthodes comparées

L’expérience devra comparer :

1. baseline seule ;
2. NeoMundi seul ;
3. baseline + NeoMundi.

---

## 13. Vérité terrain

Selon l’événement cible :

- vérité objective ;
- référence normative ;
- double annotation humaine ;
- arbitrage documenté.

Les labels devront être produits indépendamment du signal NeoMundi.

---

## 14. Revue humaine

Pour les cas non objectifs :

- deux évaluateurs indépendants ;
- aveuglement au score NeoMundi lorsque possible ;
- conservation des annotations initiales ;
- arbitrage documenté ;
- mesure de l’accord inter-évaluateurs.

---

## 15. Métriques de performance

L’expérience devra produire au minimum :

- vrais positifs ;
- faux positifs ;
- vrais négatifs ;
- faux négatifs ;
- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- score F1.

---

## 16. Analyse des erreurs

Chaque faux positif et faux négatif devra être classé selon une cause probable :

- mauvais seuil ;
- cas ambigu ;
- erreur de référence ;
- erreur d’annotation ;
- faiblesse de la métrique ;
- contexte absent ;
- problème d’instrumentation ;
- défaut non observable ;
- variation normale.

---

## 17. Critères de réussite

Les critères chiffrés ne sont pas encore définis.

Ils devront être fixés avant l’ouverture du jeu de test final.

L’expérience pourra être considérée utile même si NeoMundi ne dépasse pas la baseline sur tous les indicateurs, à condition qu’une valeur complémentaire clairement mesurable soit identifiée.

---

## 18. Conditions de gel

Avant exécution, les éléments suivants devront être figés :

- signal ;
- métrique et version ;
- claim ;
- événement cible ;
- baseline ;
- corpus ;
- labels ;
- seuils ;
- règles d’exclusion ;
- critères de réussite ;
- plan d’analyse.

---

## 19. Résultats attendus

L’expérience devra produire :

- une matrice de confusion ;
- un tableau comparatif ;
- une analyse des erreurs ;
- une conclusion méthodologique ;
- une décision sur le claim ;
- un rapport reproductible ;
- un journal des limites.

---

## 20. Limites initiales

Cette première expérience ne permettra pas à elle seule de conclure à une validation universelle.

Elle constituera :

- une première estimation ;
- un test du processus méthodologique ;
- une base pour les expériences suivantes ;
- un outil de sélection des priorités de consolidation.

---

## 21. Prochaine décision nécessaire

Choisir le premier signal à valider parmi :

1. risque factuel ;
2. variation sémantique ;
3. stabilité inter-répétitions.

---

## 22. Statut

- **Version :** v0.1
- **Statut :** DRAFT
- **Protocole gelé :** non
- **Expérience exécutée :** non
