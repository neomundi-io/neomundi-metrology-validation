# Unité d’observation NeoMundi

## 1. Objet

Ce document définit l’unité élémentaire utilisée par NeoMundi pour compter, mesurer, tracer et comparer les interactions avec un système d’intelligence artificielle.

---

## 2. Définition opérationnelle

Une observation NeoMundi correspond à :

> une requête, une réponse, les données runtime capturées, le calcul des métriques applicables, la classification des signaux et les éléments de traçabilité associés.

Sous forme simplifiée :

> 1 observation NeoMundi = 1 requête + 1 réponse + capture runtime + mesures + signaux + traçabilité.

---

## 3. Éléments constitutifs

Une observation peut contenir :

- un identifiant unique d’observation ;
- un identifiant de trace ;
- une requête ou un prompt ;
- une réponse produite ;
- le modèle ou profil utilisé ;
- les paramètres disponibles ;
- un horodatage ;
- des données runtime ;
- les métriques calculées ;
- les signaux ou classifications obtenus ;
- les versions des méthodes utilisées ;
- les éléments de preuve ou de reconstruction disponibles.

---

## 4. Distinctions terminologiques

### Observation

Unité instrumentée complète enregistrée par NeoMundi.

### Exécution

Appel effectif réalisé auprès d’un modèle ou d’un système.

Une exécution devient une observation lorsque les données nécessaires sont capturées et traitées par NeoMundi.

### Cas

Situation expérimentale ou métier soumise à un système.

Un même cas peut être exécuté plusieurs fois.

### Prompt

Instruction textuelle ou structurée transmise au système.

Un cas peut contenir un ou plusieurs prompts selon le protocole.

### Répétition

Nouvelle exécution d’un même cas dans des conditions définies comme comparables.

### Onde

Ensemble organisé de répétitions appartenant à une même séquence expérimentale.

### Campagne

Ensemble d’observations produit selon un protocole, une période et un objectif communs.

### Profil

Configuration désidentifiée représentant un modèle, un fournisseur ou un environnement d’exécution.

### Famille de risque

Catégorie utilisée pour regrouper des cas relevant d’un même type de risque ou d’usage.

---

## 5. Règles de comptage

Une observation est comptabilisée lorsque :

- une requête a été envoyée ;
- une réponse ou un statut d’échec a été enregistré ;
- un identifiant d’observation a été attribué ;
- les données disponibles ont été conservées selon le protocole ;
- le statut de complétude est explicite.

Une observation incomplète peut être conservée, mais elle doit être identifiée comme telle.

Elle ne doit pas être confondue avec une observation complète dans les analyses nécessitant toutes les données runtime.

---

## 6. Observations complètes et incomplètes

### Observation complète

Tous les champs obligatoires du protocole sont disponibles.

### Observation partielle

Certains champs non critiques sont absents, mais une partie des mesures reste exploitable.

### Observation incomplète

Des informations obligatoires manquent ou une étape essentielle du pipeline n’a pas été exécutée.

### Observation échouée

L’exécution n’a pas produit de réponse exploitable, mais l’échec lui-même a été enregistré et tracé.

---

## 7. Ce que le nombre d’observations ne représente pas

Le nombre total d’observations ne correspond pas automatiquement :

- au nombre de prompts distincts ;
- au nombre de cas distincts ;
- au nombre de modèles ;
- au nombre d’utilisateurs ;
- au nombre de vérités terrain ;
- au nombre d’anomalies ;
- au nombre de décisions de gouvernance.

Le total doit toujours être accompagné d’une décomposition du corpus.

---

## 8. Principe méthodologique

Les répétitions ne sont pas des doublons inutiles.

Elles permettent notamment d’étudier :

- la stabilité ;
- la variabilité ;
- les ruptures ;
- les distributions ;
- les changements de régime ;
- les évolutions longitudinales.

---

## 9. Formulation publique autorisée

> Une observation NeoMundi correspond à une interaction IA instrumentée, mesurée et traçable.

Formulation détaillée :

> Une observation NeoMundi associe une requête, une réponse, les données runtime disponibles, les mesures calculées et les éléments nécessaires à leur traçabilité.

---

## 10. Limites

Une observation ne prouve pas automatiquement :

- que la réponse est correcte ;
- que le système est sûr ;
- qu’une règle est légitime ;
- qu’une organisation est conforme ;
- qu’une décision de gouvernance est appropriée.

Une observation constitue une unité de mesure et de traçabilité, et non un verdict.

---

## 11. Statut du document

- Version : v0.1
- Statut : définition opérationnelle à vérifier contre l’implémentation
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
