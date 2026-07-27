# Protocole des jeux de contrôle NeoMundi

## 1. Objet

Ce document définit la construction, l’utilisation et la validation des jeux de contrôle positifs et négatifs utilisés pour tester les signaux NeoMundi.

L’objectif est de vérifier qu’un signal réagit correctement à des cas dont le statut est connu avant de l’utiliser sur des données réelles ou ambiguës.

---

## 2. Principe général

Un jeu de contrôle contient des cas dont la présence ou l’absence de l’événement cible est connue indépendamment du signal NeoMundi testé.

Les contrôles servent à vérifier :

- que le pipeline fonctionne ;
- que le signal détecte le phénomène recherché ;
- qu’il ne déclenche pas excessivement sur des cas sains ;
- que les seuils sont exploitables ;
- que les modifications techniques ne provoquent pas de régression.

---

## 3. Types de jeux de contrôle

### 3.1 Contrôles positifs

Un contrôle positif contient volontairement ou naturellement l’événement cible.

Exemples :

- erreur factuelle vérifiée ;
- contradiction interne ;
- violation explicite d’une consigne ;
- non-respect d’une règle déclarée ;
- divergence sémantique significative ;
- dégradation runtime contrôlée ;
- donnée manquante volontairement introduite.

Objectif :

> Vérifier que le signal détecte effectivement l’événement cible.

---

### 3.2 Contrôles négatifs

Un contrôle négatif ne contient pas l’événement cible.

Exemples :

- réponse factuellement exacte ;
- réponse cohérente ;
- consigne respectée ;
- règle correctement appliquée ;
- répétitions sémantiquement équivalentes ;
- données runtime complètes ;
- comportement situé dans la baseline attendue.

Objectif :

> Vérifier que le signal ne déclenche pas artificiellement une alerte.

---

### 3.3 Cas limites

Les cas limites se situent près de la frontière entre positif et négatif.

Exemples :

- approximation factuelle mineure ;
- paraphrase importante sans changement de conclusion ;
- omission secondaire ;
- règle partiellement applicable ;
- variation ponctuelle proche du seuil ;
- réponse correcte mais ambiguë.

Objectif :

> Étudier la sensibilité du signal et les zones d’incertitude.

Les cas limites doivent être analysés séparément des contrôles certains.

---

### 3.4 Cas naturels

Les cas naturels proviennent de campagnes réelles ou d’un environnement représentatif.

Ils ne doivent pas être artificiellement modifiés pour produire un défaut.

Objectif :

> Vérifier le comportement du signal dans des conditions écologiques.

---

## 4. Conditions de validité d’un contrôle

Un cas ne peut être utilisé comme contrôle que si :

- l’événement cible est défini ;
- son statut positif ou négatif est documenté ;
- la référence de validation est disponible ;
- la justification est explicite ;
- le cas est indépendant du signal testé ;
- la version du cas est enregistrée ;
- les éventuelles modifications sont traçables.

---

## 5. Contrôles positifs injectés

Un défaut peut être volontairement injecté dans un cas sain.

Exemples :

- remplacer une date correcte par une date erronée ;
- introduire une contradiction ;
- supprimer une information obligatoire ;
- violer une instruction explicite ;
- modifier une entité ;
- interrompre un flux runtime ;
- augmenter artificiellement une consommation mesurée.

Toute injection doit contenir :

- le cas original ;
- la modification effectuée ;
- l’événement cible attendu ;
- la justification ;
- la version ;
- l’auteur de la modification.

---

## 6. Contrôles positifs naturels

Un contrôle positif naturel contient un défaut réellement observé.

Il doit être accompagné de :

- l’observation originale ;
- la référence démontrant le défaut ;
- une annotation humaine ou objective ;
- le niveau de confiance ;
- la date de validation ;
- le statut d’arbitrage.

Les cas naturels doivent être privilégiés pour compléter les défauts artificiellement injectés.

---

## 7. Construction par paires

Lorsque cela est possible, un contrôle positif doit être associé à un contrôle négatif proche.

Exemple :

- version correcte d’une réponse ;
- version contenant une erreur factuelle contrôlée.

Cette approche permet de vérifier que le signal réagit au défaut introduit et non à une caractéristique secondaire du cas.

---

## 8. Équilibrage

Le corpus de contrôle doit être équilibré selon les dimensions pertinentes :

- positifs et négatifs ;
- familles de défauts ;
- modèles ou profils ;
- niveaux de difficulté ;
- langues ;
- longueurs de réponse ;
- contextes d’usage ;
- types de référence.

Un équilibre artificiel peut être utilisé pour comparer les méthodes, mais il ne représente pas automatiquement la fréquence réelle des événements en production.

---

## 9. Niveaux d’échantillonnage

### Niveau 1 — Smoke test

- 10 contrôles positifs ;
- 10 contrôles négatifs.

Objectif :

- vérifier le format ;
- tester le pipeline ;
- détecter les erreurs grossières ;
- confirmer les définitions.

Ce niveau ne constitue pas une validation statistique.

### Niveau 2 — Première estimation

- environ 100 contrôles positifs ;
- environ 100 contrôles négatifs.

Objectif :

- produire une première matrice de confusion ;
- analyser les erreurs ;
- comparer les signaux ;
- calibrer les seuils.

### Niveau 3 — Validation consolidée

- 300 à 500 contrôles positifs ;
- 300 à 500 contrôles négatifs ;
- plusieurs modèles ;
- plusieurs familles ;
- plusieurs campagnes.

Objectif :

- produire une estimation plus robuste ;
- tester la généralisation ;
- préparer une réplication.

---

## 10. Séparation des jeux

Les contrôles doivent être répartis entre :

- jeu de calibration ;
- jeu de validation ;
- jeu de test final.

Un même cas, ou une variante trop proche, ne doit pas apparaître dans plusieurs jeux sans justification.

Le jeu de test final doit rester gelé et ne pas être utilisé pour ajuster les seuils.

---

## 11. Prévention des fuites

Il faut éviter qu’une méthode obtienne artificiellement de bons résultats en reconnaissant les cas.

Risques de fuite :

- même prompt dans plusieurs jeux ;
- variantes quasi identiques ;
- seuil ajusté après lecture du test final ;
- juge ayant accès au label attendu ;
- modèle ayant déjà vu les cas ;
- métadonnées révélant le statut du contrôle.

Toute fuite connue doit être documentée.

---

## 12. Aveuglement

Lorsque cela est possible, les évaluateurs et les systèmes comparés ne doivent pas connaître :

- le statut positif ou négatif du cas ;
- le type d’injection ;
- le score NeoMundi ;
- le résultat attendu ;
- l’identité du modèle.

Le niveau d’aveuglement doit être décrit dans le rapport.

---

## 13. Métadonnées minimales

Chaque contrôle doit contenir :

- identifiant du contrôle ;
- identifiant du cas source ;
- événement cible ;
- type de contrôle ;
- statut positif ou négatif ;
- caractère naturel ou injecté ;
- référence de validation ;
- justification ;
- famille de défaut ;
- niveau de difficulté ;
- modèle ou profil ;
- langue ;
- jeu d’appartenance ;
- version ;
- statut de gel ;
- responsable ;
- date de création.

---

## 14. Statuts recommandés

- `DRAFT`
- `UNDER_REVIEW`
- `APPROVED`
- `FROZEN`
- `DEPRECATED`
- `ARCHIVED`

Seuls les cas `APPROVED` ou `FROZEN` peuvent être utilisés pour une validation formelle.

---

## 15. Contrôle hebdomadaire

Un petit jeu fixe peut être exécuté à chaque baromètre.

Composition indicative :

- 10 à 20 contrôles positifs ;
- 10 à 20 contrôles négatifs ;
- quelques cas limites.

Objectif :

- détecter une régression ;
- vérifier les juges ;
- contrôler les seuils ;
- vérifier les calculs ;
- identifier une rupture méthodologique.

Ce contrôle hebdomadaire ne remplace pas une validation complète.

---

## 16. Déclencheurs de mise à jour

Les contrôles doivent être revus lorsque :

- l’événement cible change ;
- la métrique change ;
- le seuil change ;
- le juge change ;
- une nouvelle langue est ajoutée ;
- une nouvelle famille de risque est introduite ;
- l’architecture du pipeline change ;
- une faiblesse du corpus est identifiée.

---

## 17. Limites

Un contrôle artificiel peut être plus simple qu’un défaut naturel.

Un contrôle négatif peut contenir un défaut non identifié.

Un jeu équilibré ne reflète pas nécessairement la production.

La qualité du test dépend directement de la qualité des contrôles et de leur indépendance par rapport au signal évalué.

---

## 18. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
