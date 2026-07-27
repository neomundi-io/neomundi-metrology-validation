# Protocole de structuration du corpus NeoMundi

## 1. Objet

Ce document définit la manière dont les corpus NeoMundi doivent être décrits, décomposés, versionnés et comparés.

L’objectif est d’éviter qu’un nombre total d’observations masque la structure réelle des données.

---

## 2. Principe général

Tout corpus NeoMundi doit être décrit à plusieurs niveaux.

Le nombre total d’observations ne suffit pas.

Chaque corpus doit pouvoir être décomposé selon :

- les cas ;
- les prompts ;
- les répétitions ;
- les modèles ou profils ;
- les campagnes ;
- les ondes ;
- les langues ;
- les familles de risque ;
- les catégories de vérité terrain ;
- les statuts de complétude.

---

## 3. Niveaux obligatoires de description

### 3.1 Observation

Unité instrumentée individuelle.

### 3.2 Cas

Situation expérimentale ou métier évaluée.

### 3.3 Prompt

Instruction exacte transmise au système.

### 3.4 Répétition

Nouvelle exécution d’un même cas dans des conditions comparables.

### 3.5 Onde

Ensemble organisé de répétitions.

### 3.6 Campagne

Ensemble d’observations produit dans une période et selon un protocole communs.

### 3.7 Profil

Configuration désidentifiée associée à un modèle, un fournisseur ou un environnement d’exécution.

### 3.8 Famille de risque

Catégorie regroupant des cas relevant d’un même domaine ou d’un même type de risque.

---

## 4. Métadonnées minimales d’un corpus

Chaque corpus doit contenir au minimum :

- identifiant du corpus ;
- nom du corpus ;
- version ;
- statut ;
- objectif ;
- protocole associé ;
- date de début ;
- date de fin ;
- nombre total d’observations ;
- nombre de cas distincts ;
- nombre de prompts distincts ;
- nombre de répétitions par cas ;
- nombre de modèles ou profils ;
- nombre de langues ;
- nombre de familles de risque ;
- type de vérité terrain ;
- configuration des juges ;
- version des métriques ;
- emplacement des données ;
- hash du corpus ;
- limites connues ;
- responsable de décision.

---

## 5. Catégories de corpus

Les corpus peuvent notamment être classés comme :

- baseline ;
- baromètre hebdomadaire ;
- cartographie mensuelle ;
- étude nominative ;
- étude longitudinale ;
- corpus de calibration ;
- corpus de validation ;
- corpus de test final ;
- corpus de contrôles positifs ;
- corpus de contrôles négatifs ;
- corpus de cas limites ;
- corpus de production.

---

## 6. Règles de comptage

Le nombre total d’observations doit être calculé à partir des enregistrements réellement présents.

Les valeurs théoriques doivent être distinguées des valeurs exécutées.

Les statuts suivants doivent être séparés :

- prévue ;
- exécutée ;
- complète ;
- partielle ;
- incomplète ;
- échouée ;
- exclue ;
- analysée ;
- labellisée.

Une observation ne doit pas être comptée deux fois dans un même total.

---

## 7. Règles relatives aux répétitions

Les répétitions doivent être explicitement documentées.

Pour chaque protocole, il faut préciser :

- le nombre attendu ;
- le nombre exécuté ;
- le nombre exploitable ;
- les conditions de comparabilité ;
- les paramètres maintenus constants ;
- les paramètres susceptibles de varier ;
- les règles de traitement des échecs.

Les répétitions constituent une dimension expérimentale, et non un simple volume additionnel.

---

## 8. Décomposition publique minimale

Lorsqu’un volume d’observations est communiqué publiquement, il doit être accompagné, lorsque cela est pertinent, de :

- nombre de campagnes ;
- nombre de modèles ou profils ;
- nombre de cas distincts ;
- nombre de répétitions ;
- principales familles de risque ;
- période couverte.

Exemple :

> 159 733 observations instrumentées issues de plusieurs campagnes, modèles, cas et répétitions.

Le détail exact doit être disponible dans l’inventaire du corpus.

---

## 9. Comparabilité entre corpus

Deux corpus ne peuvent être comparés directement que si les différences suivantes sont documentées :

- prompts ;
- modèles ;
- paramètres ;
- juges ;
- métriques ;
- seuils ;
- langues ;
- période ;
- nombre de répétitions ;
- règles d’exclusion ;
- version du protocole.

Une comparaison reste possible en présence de différences, mais ses limites doivent être explicites.

---

## 10. Versionnage

Toute modification substantielle doit produire une nouvelle version du corpus.

Exemples :

- ajout ou suppression de cas ;
- correction de labels ;
- changement de structure ;
- modification des métadonnées critiques ;
- changement de vérité terrain ;
- exclusion d’observations ;
- ajout d’une nouvelle langue.

Les corrections mineures doivent être consignées dans un journal de modification.

---

## 11. Intégrité et traçabilité

Chaque version de corpus doit disposer :

- d’un identifiant stable ;
- d’un hash ;
- d’une date de création ;
- d’un journal de modification ;
- d’un responsable ;
- d’un lien vers le protocole ;
- d’un statut de gel.

---

## 12. Statuts du corpus

Les statuts recommandés sont :

- `DRAFT`
- `UNDER_REVIEW`
- `FROZEN`
- `DEPRECATED`
- `ARCHIVED`

Un corpus utilisé pour une validation finale doit être gelé avant l’exécution du test.

---

## 13. Limites

Un grand nombre d’observations ne garantit pas :

- la diversité réelle du corpus ;
- la qualité de la vérité terrain ;
- l’indépendance statistique des cas ;
- la représentativité ;
- la validité externe ;
- la qualité de l’instrument.

La structure du corpus doit toujours être analysée avec son volume.

---

## 14. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
