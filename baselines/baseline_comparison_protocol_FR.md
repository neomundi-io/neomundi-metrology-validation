# Protocole de comparaison aux baselines NeoMundi

## 1. Objet

Ce document définit la manière dont NeoMundi doit être comparé à des méthodes simples ou existantes.

L’objectif est de déterminer si NeoMundi apporte une valeur mesurable au-delà d’une approche classique.

---

## 2. Principe général

NeoMundi ne doit pas être comparé à l’absence de méthode.

Chaque capacité revendiquée doit être comparée à une ou plusieurs baselines pertinentes.

La question centrale est :

> NeoMundi améliore-t-il la détection, la robustesse, la rapidité ou la traçabilité par rapport à une approche plus simple ?

---

## 3. Baselines minimales

Selon l’événement cible, les baselines peuvent inclure :

- factualité seule ;
- similarité sémantique seule ;
- détection de drift seule ;
- règles runtime seules ;
- seuil simple sur une métrique ;
- combinaison classique de plusieurs signaux ;
- journaux d’exécution sans analyse NeoMundi.

---

## 4. Méthodes à comparer

Pour chaque expérience, les lignes suivantes doivent être testées lorsque cela est pertinent :

1. baseline simple ;
2. combinaison de baselines ;
3. NeoMundi seul ;
4. baseline plus NeoMundi.

La comparaison la plus importante est :

> baseline classique + NeoMundi contre baseline classique seule.

---

## 5. Conditions d’équité

Toutes les méthodes doivent être évaluées avec :

- le même corpus ;
- la même vérité terrain ;
- la même unité d’analyse ;
- les mêmes jeux de calibration et de test ;
- les mêmes règles d’exclusion ;
- la même période ;
- des seuils calibrés selon une procédure documentée.

Aucune méthode ne doit bénéficier d’informations supplémentaires non accessibles aux autres, sauf si cette différence constitue précisément l’objet du test.

---

## 6. Calibration

Les seuils doivent être calibrés uniquement sur le jeu prévu à cet effet.

Le jeu de test final ne doit pas être utilisé pour :

- choisir une méthode ;
- ajuster un seuil ;
- modifier une règle ;
- sélectionner les cas les plus favorables.

---

## 7. Métriques de comparaison

Selon l’expérience, comparer :

- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- score F1 ;
- délai de détection ;
- stabilité entre campagnes ;
- robustesse entre modèles ;
- couverture ;
- coût de calcul ;
- latence ;
- taux de données exploitables.

---

## 8. Valeur incrémentale

La valeur incrémentale correspond à l’amélioration obtenue lorsque NeoMundi est ajouté à une baseline.

Elle peut prendre plusieurs formes :

- augmentation du rappel ;
- réduction des faux positifs ;
- réduction des faux négatifs ;
- détection plus précoce ;
- meilleure stabilité longitudinale ;
- amélioration de la traçabilité ;
- couverture d’un défaut non détecté par la baseline.

---

## 9. Valeur localisée

NeoMundi peut apporter une valeur sur certains types de défauts sans améliorer tous les usages.

Exemple :

> NeoMundi n’améliore pas significativement la détection factuelle ponctuelle, mais améliore la détection longitudinale des variations.

Une valeur localisée constitue un résultat utile si elle est clairement documentée.

---

## 10. Résultats négatifs ou équivalents

Les résultats suivants doivent être publiés :

- absence d’amélioration ;
- résultat équivalent à la baseline ;
- dégradation de performance ;
- augmentation des faux positifs ;
- gain trop faible au regard du coût ;
- avantage limité à certains modèles ou corpus.

Un résultat négatif ne doit pas être masqué.

---

## 11. Analyse statistique

Lorsque la taille du corpus le permet, la comparaison doit inclure :

- intervalles de confiance ;
- estimation de l’incertitude ;
- tests adaptés aux données appariées ;
- analyse de la stabilité du résultat ;
- vérification sur plusieurs sous-groupes.

La significativité statistique ne remplace pas l’utilité opérationnelle.

---

## 12. Analyse par sous-groupes

Les résultats doivent être examinés selon :

- modèle ou profil ;
- famille de risque ;
- langue ;
- longueur de réponse ;
- niveau de difficulté ;
- type de vérité terrain ;
- campagne ;
- type de défaut.

Une moyenne globale peut masquer des écarts importants.

---

## 13. Coût de la méthode

La valeur ajoutée doit être mise en regard de :

- la latence supplémentaire ;
- le nombre d’appels ;
- le coût de calcul ;
- la complexité opérationnelle ;
- la couverture obtenue ;
- les ressources humaines nécessaires.

Une amélioration faible peut ne pas être utile si son coût est disproportionné.

---

## 14. Formulations autorisées

Exemple acceptable :

> Sur le corpus de test gelé, l’ajout des signaux NeoMundi à la baseline a amélioré le rappel de X points, avec une variation de Y points du taux de faux positifs.

Exemples interdits sans preuve suffisante :

> NeoMundi est supérieur à toutes les solutions existantes.

> NeoMundi remplace toutes les méthodes classiques.

> NeoMundi détecte mieux tous les types de risques.

---

## 15. Rapport minimal

Chaque comparaison doit documenter :

- l’événement cible ;
- le corpus ;
- la vérité terrain ;
- les baselines ;
- les versions ;
- les seuils ;
- les métriques ;
- les résultats ;
- les intervalles d’incertitude ;
- les sous-groupes ;
- les coûts ;
- les limites ;
- les non-résultats ;
- la décision méthodologique.

---

## 16. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
