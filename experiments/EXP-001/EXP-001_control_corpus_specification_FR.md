# EXP-001 — Spécification du corpus de contrôle factuel

## 1. Objet

Ce document définit la structure du corpus utilisé pour valider le signal de risque factuel NeoMundi.

L’objectif est de construire un corpus suffisamment clair, équilibré et traçable pour mesurer :

- les vrais positifs ;
- les faux positifs ;
- les vrais négatifs ;
- les faux négatifs ;
- la performance de la baseline ;
- la valeur incrémentale éventuelle de NeoMundi.

---

## 2. Taille cible initiale

La première estimation expérimentale reposera sur :

- 100 cas positifs ;
- 100 cas négatifs ;
- cas ambigus conservés séparément.

Total principal visé :

> 200 cas exploitables dans la matrice de confusion.

---

## 3. Définition d’un cas positif

Un cas positif contient :

> au moins une erreur factuelle significative démontrable par une référence vérifiée.

L’erreur doit pouvoir modifier :

- la compréhension ;
- la conclusion ;
- la décision ;
- la recommandation ;
- l’usage opérationnel.

---

## 4. Définition d’un cas négatif

Un cas négatif contient :

> une réponse ne présentant aucune erreur factuelle significative selon la référence utilisée.

Une différence stylistique, une paraphrase ou une variation de longueur ne constitue pas une erreur factuelle.

---

## 5. Cas ambigus

Un cas est classé comme ambigu lorsque :

- les références sont contradictoires ;
- le fait est évolutif ;
- la réponse contient une approximation discutable ;
- le contexte est insuffisant ;
- l’erreur éventuelle est sans impact clair ;
- une expertise supplémentaire est nécessaire.

Les cas ambigus ne doivent pas être intégrés automatiquement dans la matrice de confusion principale.

---

## 6. Types de cas positifs

Le corpus positif doit inclure plusieurs familles d’erreurs.

### Factualité simple

- date erronée ;
- nom incorrect ;
- lieu incorrect ;
- chiffre incorrect ;
- définition fausse.

### Erreur de raisonnement factuel

- conclusion incompatible avec les données ;
- calcul incorrect ;
- relation causale inventée ;
- confusion entre deux entités.

### Omission factuelle significative

- absence d’une information indispensable ;
- omission modifiant la conclusion ;
- réponse partiellement correcte mais trompeuse.

### Contradiction avec la référence

- affirmation opposée à la source ;
- négation d’un fait établi ;
- attribution erronée.

### Erreur contextuelle

- fait correct dans un autre contexte mais faux ici ;
- réponse obsolète ;
- généralisation abusive.

---

## 7. Origine des cas

Le corpus doit combiner :

### Cas naturels

Erreurs réellement observées dans les campagnes NeoMundi.

### Cas injectés

Réponses correctes modifiées volontairement pour introduire une erreur factuelle contrôlée.

### Cas fermés

Questions disposant d’une réponse unique ou déterministe.

### Cas ouverts mais vérifiables

Réponses contenant plusieurs affirmations contrôlables à partir d’une référence documentée.

---

## 8. Construction par paires

Lorsque possible, les cas doivent être construits par paires :

- une version factuellement correcte ;
- une version contenant une erreur contrôlée.

L’objectif est de vérifier que le signal réagit à l’erreur et non à une caractéristique secondaire de la réponse.

---

## 9. Répartition indicative

Le corpus de 200 cas peut être réparti ainsi :

| Catégorie | Positifs | Négatifs |
|---|---:|---:|
| Calculs et logique fermée | 20 | 20 |
| Dates, chiffres et entités | 20 | 20 |
| Sciences et connaissances générales | 20 | 20 |
| Contextes métier ou sectoriels | 20 | 20 |
| Réponses ouvertes vérifiables | 20 | 20 |
| **Total** | **100** | **100** |

Cette répartition reste provisoire jusqu’à l’inventaire des cas disponibles.

---

## 10. Diversité attendue

Le corpus doit documenter :

- le modèle ou profil ;
- la famille de cas ;
- la difficulté ;
- la longueur de réponse ;
- la langue ;
- le type de référence ;
- le caractère naturel ou injecté ;
- la présence éventuelle de répétitions.

---

## 11. Références autorisées

Chaque cas doit être associé à une référence parmi :

- calcul déterministe ;
- source officielle ;
- documentation versionnée ;
- donnée explicitement présente dans le corpus ;
- règle factuelle gelée ;
- validation experte documentée.

La référence doit être indépendante du signal NeoMundi.

---

## 12. Métadonnées minimales

Chaque cas doit contenir :

- identifiant du cas ;
- prompt ;
- réponse ;
- label de vérité terrain ;
- type de cas ;
- famille factuelle ;
- référence ;
- justification ;
- niveau de confiance ;
- caractère naturel ou injecté ;
- modèle ou profil ;
- langue ;
- difficulté ;
- jeu d’appartenance ;
- version ;
- statut de revue ;
- statut de gel.

---

## 13. Répartition des jeux

Proposition initiale :

- 60 % calibration ;
- 20 % validation ;
- 20 % test final.

Pour 200 cas :

- 120 cas de calibration ;
- 40 cas de validation ;
- 40 cas de test final.

La répartition doit maintenir un équilibre entre positifs et négatifs.

---

## 14. Prévention des fuites

Il faut éviter :

- le même prompt dans plusieurs jeux ;
- des variantes trop proches dans plusieurs jeux ;
- une paire correcte et incorrecte répartie entre calibration et test final ;
- l’utilisation du jeu final pour ajuster les seuils ;
- l’accès au label par le système testé.

Les cas similaires doivent être regroupés avant la séparation des jeux.

---

## 15. Statuts des cas

Les statuts recommandés sont :

- `DRAFT`
- `UNDER_REVIEW`
- `APPROVED`
- `FROZEN`
- `EXCLUDED`
- `ARCHIVED`

Seuls les cas `APPROVED` ou `FROZEN` peuvent entrer dans l’expérience finale.

---

## 16. Critères d’inclusion

Un cas est inclus si :

- l’événement cible est applicable ;
- la référence est disponible ;
- le label est justifiable ;
- la réponse est exploitable ;
- les métadonnées minimales sont présentes ;
- le cas n’introduit pas de fuite connue.

---

## 17. Critères d’exclusion

Un cas est exclu si :

- la référence est insuffisante ;
- le label reste ambigu ;
- la réponse est incomplète ;
- le cas est dupliqué ;
- une fuite méthodologique est détectée ;
- l’événement cible ne s’applique pas ;
- la qualité des données est insuffisante.

Toute exclusion doit être tracée.

---

## 18. Limites

Un corpus équilibré ne reflète pas automatiquement la fréquence réelle des erreurs factuelles en production.

Les cas injectés peuvent être plus simples que les erreurs naturelles.

La performance mesurée restera locale au corpus, aux références et aux modèles utilisés.

---

## 19. Décision méthodologique

- **Taille cible :** 200 cas
- **Cas positifs :** 100
- **Cas négatifs :** 100
- **Cas ambigus :** séparés
- **Statut :** DRAFT
- **Exécution autorisée :** non
- **Prochaine étape :** créer le modèle de fichier permettant de recenser les 200 cas
- **Responsable :** Sébastien
- **Date :** 27 juillet 2026
