# Modèle d’expérience méthodologique NeoMundi

## 1. Identification

- **Identifiant de l’expérience :**
- **Titre :**
- **Version :**
- **Statut :**
- **Date de création :**
- **Responsable :**
- **Contributeurs :**

Statuts recommandés :

- `DRAFT`
- `READY`
- `FROZEN`
- `RUNNING`
- `COMPLETED`
- `INVALIDATED`
- `ARCHIVED`

---

## 2. Question de recherche

> Quelle question précise cette expérience cherche-t-elle à résoudre ?

La question doit être :

- bornée ;
- testable ;
- liée à un claim identifié ;
- compréhensible indépendamment des résultats ;
- formulée avant l’exécution.

---

## 3. Claim évalué

- **Identifiant du claim :**
- **Affirmation testée :**
- **Statut avant expérience :**
- **Formulation autorisée actuelle :**
- **Formulation qui pourrait être autorisée après validation :**

---

## 4. Hypothèse

### Hypothèse principale

> Formuler l’effet ou la capacité attendue.

### Hypothèse nulle

> Formuler l’absence d’effet ou d’amélioration attendue.

### Hypothèses secondaires

- 
- 
- 

---

## 5. Événement cible

- **Identifiant de l’événement cible :**
- **Définition opérationnelle :**
- **Condition positive :**
- **Condition négative :**
- **Cas ambigus :**
- **Référence de validation :**

---

## 6. Signal ou métrique évalué

- **Identifiant de la métrique :**
- **Nom :**
- **Version :**
- **Implémentation :**
- **Entrées :**
- **Sortie :**
- **Seuil testé :**
- **Statut méthodologique actuel :**
- **Limites connues :**

---

## 7. Baselines

### Baseline principale

- **Nom :**
- **Version :**
- **Méthode :**
- **Seuil :**
- **Justification :**

### Baselines secondaires

- 
- 
- 

### Comparaisons prévues

- baseline seule ;
- NeoMundi seul ;
- baseline + NeoMundi.

---

## 8. Corpus

- **Identifiant du corpus :**
- **Version :**
- **Nombre total de cas :**
- **Nombre de cas positifs :**
- **Nombre de cas négatifs :**
- **Nombre de cas ambigus :**
- **Modèles ou profils :**
- **Langues :**
- **Familles de risque :**
- **Nombre de répétitions :**
- **Hash du corpus :**
- **Statut de gel :**

---

## 9. Répartition des données

### Jeu de calibration

- Nombre de cas :
- Rôle :
- Utilisation autorisée :

### Jeu de validation

- Nombre de cas :
- Rôle :
- Utilisation autorisée :

### Jeu de test final

- Nombre de cas :
- Rôle :
- Statut de gel :
- Date d’ouverture prévue :

Le jeu de test final ne doit pas être utilisé pour ajuster les seuils.

---

## 10. Protocole de revue humaine

- **Guide utilisé :**
- **Version :**
- **Nombre d’évaluateurs :**
- **Mode d’aveuglement :**
- **Règle d’arbitrage :**
- **Mesure d’accord prévue :**
- **Expertise nécessaire :**

---

## 11. Variables contrôlées

Les éléments suivants doivent être documentés :

- modèle ;
- version du modèle ;
- fournisseur ;
- paramètres ;
- température ;
- prompt ;
- langue ;
- nombre de répétitions ;
- modèle d’embedding ;
- juge ;
- seuils ;
- version du pipeline ;
- environnement d’exécution.

---

## 12. Critères d’inclusion

Un cas est inclus si :

- 
- 
- 

---

## 13. Critères d’exclusion

Un cas est exclu si :

- 
- 
- 

Toute exclusion après exécution doit être documentée et justifiée.

---

## 14. Métriques de performance

Les métriques prévues peuvent inclure :

- vrais positifs ;
- faux positifs ;
- vrais négatifs ;
- faux négatifs ;
- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- F1 ;
- exactitude ;
- couverture ;
- délai de détection ;
- coût ;
- latence.

---

## 15. Critères de réussite

Les critères doivent être définis avant l’exécution.

Exemples :

- rappel supérieur ou égal à :
- taux maximal de faux positifs :
- amélioration minimale par rapport à la baseline :
- stabilité minimale entre profils :
- couverture minimale :
- coût maximal acceptable :

---

## 16. Plan d’analyse

L’analyse prévue doit préciser :

- calcul de la matrice de confusion ;
- comparaison aux baselines ;
- intervalles d’incertitude ;
- analyse par sous-groupes ;
- analyse des erreurs ;
- analyse des cas ambigus ;
- analyse des répétitions ;
- tests statistiques éventuels ;
- traitement des données manquantes.

---

## 17. Risques méthodologiques

Risques identifiés :

- fuite entre les jeux ;
- sur-ajustement ;
- biais du juge ;
- biais d’annotation ;
- faible taille d’échantillon ;
- classes déséquilibrées ;
- dépendance au modèle ;
- corpus non représentatif ;
- changement de version ;
- défaut d’instrumentation.

Mesures de réduction prévues :

- 
- 
- 

---

## 18. Gel du protocole

Avant l’exécution, les éléments suivants doivent être gelés :

- question de recherche ;
- hypothèses ;
- événement cible ;
- métrique ;
- baselines ;
- corpus ;
- répartition des données ;
- seuils ;
- critères de réussite ;
- règles d’exclusion ;
- plan d’analyse.

- **Date de gel :**
- **Version gelée :**
- **Responsable de validation :**

---

## 19. Résultats

### Matrice de confusion

| Méthode | VP | FP | VN | FN |
|---|---:|---:|---:|---:|
| Baseline |  |  |  |  |
| NeoMundi |  |  |  |  |
| Baseline + NeoMundi |  |  |  |  |

### Performances

| Méthode | Précision | Rappel | Spécificité | F1 |
|---|---:|---:|---:|---:|
| Baseline |  |  |  |  |
| NeoMundi |  |  |  |  |
| Baseline + NeoMundi |  |  |  |  |

### Résultats par sous-groupes

À compléter.

---

## 20. Analyse des erreurs

### Faux positifs

- causes principales ;
- sous-groupes concernés ;
- exemples ;
- impact ;
- corrections envisagées.

### Faux négatifs

- causes principales ;
- sous-groupes concernés ;
- exemples ;
- impact ;
- corrections envisagées.

### Cas ambigus

- nombre ;
- causes ;
- décisions ;
- impact sur les conclusions.

---

## 21. Résultats non attendus

Documenter :

- résultats négatifs ;
- absence d’amélioration ;
- comportements inattendus ;
- limites découvertes ;
- hypothèses invalidées ;
- biais révélés.

---

## 22. Conclusion méthodologique

- **Hypothèse principale :** confirmée / partiellement confirmée / non confirmée
- **Valeur par rapport à la baseline :**
- **Domaine de validité :**
- **Limites :**
- **Revalidation nécessaire :**
- **Réplication nécessaire :**

---

## 23. Décision sur le claim

Après l’expérience, le claim peut être :

- maintenu comme hypothétique ;
- reformulé ;
- autorisé dans un périmètre limité ;
- validé localement ;
- rejeté ;
- soumis à réplication.

- **Nouveau statut :**
- **Formulation autorisée :**
- **Formulation interdite :**
- **Décision associée :**

---

## 24. Artefacts produits

- protocole gelé ;
- corpus ;
- labels ;
- configuration ;
- scripts ;
- logs ;
- résultats ;
- rapport ;
- journal des erreurs ;
- hashes ;
- preuves de calcul.

---

## 25. Reproductibilité

- **Commande de reproduction :**
- **Environnement :**
- **Dépendances :**
- **Version du code :**
- **Hash du corpus :**
- **Hash des résultats :**
- **Écart toléré :**

---

## 26. Statut final

- **Version :**
- **Statut :**
- **Date de clôture :**
- **Responsable :**
- **Décision méthodologique associée :**
