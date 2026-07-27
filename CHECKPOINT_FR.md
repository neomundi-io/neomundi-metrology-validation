# NeoMundi Metrology Validation — Point d’arrêt et plan de reprise

## 1. Objet

Ce document indique :

- ce qui a été réalisé ;
- où le chantier s’arrête ;
- la première étape à reprendre ;
- ce qui reste à faire ;
- les conditions avant toute exécution méthodologique.

Il constitue le point d’entrée opérationnel pour reprendre le travail sans perdre le fil.

---

## 2. Point d’arrêt

Date du point d’arrêt :

> 27 juillet 2026

Le chantier s’arrête après la création de l’architecture méthodologique initiale du repository et avant l’exécution réelle du premier smoke test.

À ce stade :

- aucun test de performance NeoMundi n’a été exécuté dans ce repo ;
- aucune matrice de confusion réelle n’a été calculée ;
- aucun claim scientifique nouveau n’est autorisé ;
- le protocole EXP-001 n’est pas encore gelé ;
- la métrique réelle `MET-003` n’est pas encore reliée à son implémentation ;
- la baseline factuelle exécutable n’est pas encore choisie définitivement ;
- les références des 20 cas doivent encore être documentées ;
- la revue humaine n’a pas encore commencé.

---

## 3. Ce qui a été réalisé

### 3.1 Structure générale du repository

Les éléments suivants ont été créés :

- `README.md`
- `ROADMAP.md`
- `CHECKPOINT_FR.md`
- dossiers méthodologiques ;
- dossiers d’expériences ;
- dossiers de résultats ;
- dossier de scripts ;
- workflow GitHub Actions.

---

### 3.2 Fondations méthodologiques

Les documents suivants ont été créés :

- définition de l’unité d’observation NeoMundi ;
- protocole de structuration du corpus ;
- registre des claims et non-claims ;
- dictionnaire initial des métriques ;
- séparation des dimensions d’évaluation ;
- registre des événements cibles ;
- protocole de vérité terrain et d’annotation ;
- protocole de revue humaine ;
- protocole de mesure des faux positifs et faux négatifs ;
- protocole des jeux de contrôle ;
- protocole d’accord inter-évaluateurs ;
- protocole de comparaison aux baselines ;
- protocole longitudinal ;
- taxonomie des niveaux de preuve ;
- journal des décisions méthodologiques ;
- modèle standard d’expérience.

---

### 3.3 EXP-001

L’expérience `EXP-001` a été initialisée avec :

- un protocole général ;
- la sélection du signal de risque factuel ;
- l’association aux identifiants :
  - `CLM-003`
  - `MET-003`
  - `EVT-003`
- une baseline factuelle provisoire ;
- une spécification du corpus de contrôle ;
- un registre maître des cas ;
- un smoke test de 20 cas synthétiques ;
- 10 cas positifs ;
- 10 cas négatifs ;
- un protocole d’exécution ;
- un manifeste d’exécution ;
- un schéma de sortie NeoMundi ;
- un schéma de sortie baseline ;
- un schéma de matrice de confusion ;
- un journal des erreurs ;
- un modèle de rapport final.

---

### 3.4 Automatisation

Les éléments suivants ont été créés :

- script de validation structurelle du smoke test ;
- workflow GitHub Actions ;
- contrôle automatique du nombre de cas ;
- contrôle des identifiants ;
- contrôle des labels ;
- contrôle des valeurs autorisées ;
- contrôle de la cohérence des cas injectés.

---

## 4. Ce qui n’est pas encore fait

Les éléments suivants restent ouverts :

- vérifier que GitHub Actions retourne une coche verte ;
- corriger toute erreur détectée par le workflow ;
- extraire la définition exacte de `MET-003` depuis le code réel ;
- documenter la formule ou la logique du signal ;
- documenter les entrées et sorties ;
- documenter le seuil ;
- versionner l’implémentation ;
- choisir la baseline factuelle exécutable ;
- compléter les références des 20 cas ;
- vérifier les labels des 20 cas ;
- organiser la revue humaine si nécessaire ;
- produire le hash du corpus ;
- geler le corpus ;
- geler le protocole ;
- autoriser l’exécution ;
- exécuter le smoke test ;
- calculer la matrice de confusion ;
- analyser les erreurs ;
- décider s’il faut corriger ou poursuivre.

---

## 5. Première étape à la reprise

La prochaine session doit commencer par :

> Vérifier le workflow GitHub Actions `Validation EXP-001 Smoke Test`.

Actions :

1. ouvrir l’onglet `Actions` ;
2. ouvrir le dernier run ;
3. vérifier s’il est vert ou rouge ;
4. lire les logs ;
5. corriger le script ou le CSV si nécessaire ;
6. relancer la validation ;
7. ne continuer qu’après obtention d’une validation structurelle réussie.

---

## 6. Deuxième étape à la reprise

Après validation structurelle du CSV :

> Relier `MET-003` à l’implémentation réelle NeoMundi.

Il faudra retrouver et documenter :

- le fichier de code ;
- la fonction ou classe concernée ;
- les entrées ;
- la logique exacte ;
- les sorties ;
- les dépendances ;
- le seuil ;
- la gestion des erreurs ;
- la gestion des données manquantes ;
- la version du pipeline.

Le dictionnaire des métriques devra alors être mis à jour.

---

## 7. Troisième étape à la reprise

Définir la baseline factuelle réellement exécutable.

Choix possibles :

- règle déterministe ;
- comparaison à une référence ;
- modèle juge ;
- revue humaine ;
- combinaison versionnée.

La baseline doit rester indépendante des signaux NeoMundi.

---

## 8. Quatrième étape à la reprise

Compléter les 20 cas du smoke test.

Champs à finaliser :

- `reference_location`
- `reference_version`
- `model_or_profile`
- `provider`
- `split`
- `review_status`
- labels des évaluateurs si nécessaires ;
- statut d’arbitrage ;
- statut de gel.

Les valeurs provisoires comme :

- `TO_BE_DOCUMENTED`
- `TO_BE_DEFINED`
- `UNASSIGNED`
- `NOT_REVIEWED`

doivent être traitées avant le gel.

---

## 9. Cinquième étape à la reprise

Réaliser la revue humaine nécessaire.

Pour les cas déterministes simples :

- vérification directe ;
- justification ;
- validation du label.

Pour les cas nécessitant une interprétation :

- deux évaluateurs indépendants si possible ;
- aveuglement aux scores NeoMundi ;
- conservation des désaccords ;
- arbitrage documenté ;
- mesure de l’accord inter-évaluateurs.

---

## 10. Conditions avant exécution

Aucune exécution ne doit commencer tant que les éléments suivants ne sont pas finalisés :

- métrique réelle documentée ;
- seuil défini ;
- baseline définie ;
- références complétées ;
- corpus validé ;
- corpus hashé ;
- protocole gelé ;
- corpus gelé ;
- commit GitHub enregistré ;
- environnement enregistré ;
- autorisation d’exécution activée.

Dans le manifeste, les champs suivants devront passer à `true` :

```json
"protocol_frozen": true,
"corpus_frozen": true,
"execution_authorized": true
