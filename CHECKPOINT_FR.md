# NeoMundi Metrology Validation — Point d’arrêt et plan de reprise

## 1. Objet

Ce document indique :

- ce qui a été réalisé ;
- où le chantier s’arrête ;
- la dépendance actuellement bloquante ;
- la première étape exacte à reprendre ;
- ce qui reste à faire avant l’exécution ;
- ce qui restera à faire après l’exécution ;
- les conditions de la revue humaine des résultats.

Il constitue le point d’entrée opérationnel pour reprendre le travail sans perdre le fil.

---

## 2. Point d’arrêt

Date du point d’arrêt :

> 2 août 2026

Le chantier s’arrête après le gel méthodologique du smoke test `EXP-001 v0.1` et avant l’enregistrement complet de l’environnement réel du juge factuel.

À ce stade :

- le corpus de 20 cas est gelé ;
- le corpus a passé les validations automatiques ;
- le hash SHA-256 définitif du corpus est enregistré ;
- la baseline déterministe indépendante est gelée ;
- le protocole d’exécution est gelé ;
- le signal `MET-003` est relié à son implémentation backend ;
- le seuil expérimental `0.5` est gelé pour `EXP-001 v0.1` ;
- le commit backend interne `f02f7ff` est enregistré ;
- l’ancre du repository expérimental `7b29408` est enregistrée ;
- la revue humaine des 20 cas est terminée ;
- aucun run NeoMundi n’a encore été exécuté dans ce repository ;
- aucune matrice de confusion réelle n’a encore été calculée ;
- aucune revue humaine des résultats n’a encore été réalisée ;
- aucune affirmation générale de performance n’est autorisée ;
- l’exécution reste interdite tant que l’environnement du juge n’est pas complètement documenté.

---

## 3. Dépendance actuellement bloquante

Le juge principal utilisé par le backend est Euria auto-hébergé.

Le code confirme que la configuration du juge principal est injectée par les variables d’environnement suivantes :

```text
JUDGE_BASE_URL
JUDGE_MODEL
JUDGE_API_KEY
```

Le code confirme également l’existence d’un mécanisme de secours utilisant notamment :

```text
HALLUCINATION_JUDGE_FALLBACK_BASE_URL
HALLUCINATION_JUDGE_FALLBACK_MODEL
HALLUCINATION_JUDGE_FALLBACK_API_KEY
```

Le modèle de secours par défaut observé dans le code est :

```text
llama3.1:8b
```

Les valeurs réellement utilisées sur le serveur ne sont pas stockées dans le repository GitHub.

La reprise dépend donc de la confirmation par Manal des éléments non secrets suivants :

```text
JUDGE_BASE_URL
JUDGE_MODEL
HALLUCINATION_JUDGE_FALLBACK_MODEL
```

Aucune clé API ne doit être copiée dans le repository ou dans le manifeste.

---

## 4. Ce qui a été réalisé

### 4.1 Structure générale du repository

Les éléments suivants sont présents :

- `README.md`
- `ROADMAP.md`
- `CHECKPOINT_FR.md`
- dossiers méthodologiques ;
- dossiers d’expériences ;
- dossiers de résultats ;
- dossier de scripts ;
- workflow GitHub Actions ;
- scripts de validation et de hash.

---

### 4.2 Fondations méthodologiques

Les documents suivants ont été créés ou consolidés :

- définition de l’unité d’observation NeoMundi ;
- protocole de structuration du corpus ;
- registre des claims et non-claims ;
- dictionnaire des métriques en français ;
- dictionnaire des métriques en anglais ;
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

### 4.3 Implémentation de MET-003

Le signal sélectionné est :

```text
MET-003 — Signal de risque factuel
```

Champ principal :

```text
factual_hallucination_score
```

Classification associée :

```text
is_hallucinated
```

Alias historique :

```text
hallucination_score
```

Implémentation observée :

```text
govern-v3/app/core/hallucination_detector.py
```

Fonction principale :

```text
detect_hallucination
```

Commit backend interne :

```text
f02f7ff
```

Visibilité du repository backend :

```text
PRIVATE
```

Le commit `f02f7ff` constitue une ancre d’audit interne.

Il ne constitue pas une preuve publique autonome.

---

### 4.4 Seuil expérimental

Le seuil de classification retenu pour `EXP-001 v0.1` est :

```text
0.5
```

Règle :

```text
is_hallucinated = factual_hallucination_score >= 0.5
```

Ce seuil est :

- gelé pour le smoke test ;
- non calibré ;
- non validé ;
- non universel ;
- non optimal par défaut ;
- interdit de modification après consultation des résultats sans création d’une nouvelle version expérimentale.

Le seuil `0.3` observé dans le prompt du juge concerne l’extraction des passages suspects et non la classification principale.

---

### 4.5 Baseline

La baseline retenue est :

> une baseline déterministe indépendante fondée sur une référence factuelle documentée et versionnée.

Elle :

- n’utilise aucun modèle juge pour sa décision principale ;
- ne reçoit aucun score NeoMundi ;
- ne reçoit aucun autre signal runtime ;
- produit les classes :
  - `FACTUALLY_CORRECT`
  - `FACTUALLY_INCORRECT`
  - `UNDETERMINED`

Version :

```text
v0.1
```

Statut :

```text
FROZEN
```

---

### 4.6 Corpus du smoke test

Fichier :

```text
experiments/EXP-001/EXP-001_smoke_test_20_cases_FR.csv
```

Composition :

- 20 cas synthétiques ;
- 10 cas positifs ;
- 10 cas négatifs ;
- 10 paires correcte/incorrecte ;
- cas fermés simples ;
- réponses courtes ;
- références documentées ;
- références versionnées ;
- labels revus humainement.

Répartition :

- `CALIBRATION` : 12 cas ;
- `VALIDATION` : 4 cas ;
- `FINAL_TEST` : 4 cas.

Statut :

```text
FROZEN
```

Version :

```text
v0.1
```

---

### 4.7 Revue humaine des cas

La revue humaine des 20 cas est terminée.

Résultat :

- 20 cas approuvés ;
- 0 cas rejeté ;
- 0 cas exclu ;
- aucun arbitrage requis ;
- labels finaux cohérents avec les labels de vérité terrain ;
- revue réalisée avant toute production de résultats NeoMundi.

Cette revue humaine concerne le corpus.

Elle est distincte de la future revue humaine des résultats du run.

---

### 4.8 Validation automatique

Le workflow suivant est opérationnel :

```text
Validation EXP-001 Smoke Test
```

Étapes validées :

- validation structurelle ;
- validation documentaire ;
- validation du statut gelé ;
- calcul du hash SHA-256.

Dernier run de gel observé :

```text
workflow run #9
```

Statut :

```text
SUCCESS
```

---

### 4.9 Hash définitif du corpus gelé

Algorithme :

```text
SHA-256
```

Hash :

```text
bd9ac82fd53aab35fba15ff999033f894f69775d256940f27694677720174ce1
```

Taille :

```text
14458 octets
```

Script utilisé :

```text
scripts/hash_exp001_corpus.py
```

Environnement de calcul :

```text
GitHub Actions
```

---

### 4.10 Protocole d’exécution

Le protocole d’exécution du smoke test est gelé.

Version :

```text
v0.1
```

Statut :

```text
FROZEN
```

L’exécution n’est pas automatiquement autorisée par le seul gel du protocole.

---

### 4.11 Sélection du signal

Le document de sélection du signal est gelé avec :

- métrique : `MET-003` ;
- événement cible : `EVT-003` ;
- champ : `factual_hallucination_score` ;
- classification : `is_hallucinated` ;
- seuil : `0.5` ;
- opérateur : `>=` ;
- commit backend interne : `f02f7ff` ;
- baseline : déterministe indépendante ;
- corpus : `EXP-001_smoke_test_20_cases_FR.csv`.

Statut :

```text
FROZEN
```

---

### 4.12 Manifeste

Le manifeste du run a été consolidé dans :

```text
experiments/EXP-001/EXP-001_smoke_test_run_manifest.json
```

Il contient notamment :

- le signal gelé ;
- le seuil gelé ;
- la baseline gelée ;
- le protocole gelé ;
- le corpus gelé ;
- le hash du corpus ;
- le commit backend interne ;
- l’ancre du repository expérimental ;
- les résultats des validations automatiques ;
- les blocages restants ;
- l’interdiction actuelle d’exécution.

Statut actuel :

```text
FROZEN_PENDING_ENVIRONMENT
```

---

### 4.13 Ancre du repository expérimental

Repository :

```text
neomundi-metrology-validation
```

Branche :

```text
main
```

Commit d’ancrage :

```text
7b29408
```

Rôle :

```text
EXPERIMENTAL_REPOSITORY_AUDIT_ANCHOR
```

Le commit `7b29408` constitue l’ancre du repository après :

- gel de la métrique ;
- gel du seuil ;
- gel de la baseline ;
- gel du protocole ;
- gel du corpus ;
- mise à jour initiale du manifeste.

Les mises à jour ultérieures du manifeste ne doivent pas modifier les éléments expérimentaux gelés.

---

## 5. Ce qui n’a pas encore été réalisé

Les éléments suivants restent ouverts :

- confirmer les valeurs réelles de `JUDGE_BASE_URL` et `JUDGE_MODEL` ;
- confirmer le modèle de secours réellement configuré ;
- documenter l’endpoint sans enregistrer de secret ;
- documenter le système d’exploitation d’exécution ;
- documenter le mode de lancement ;
- documenter les dépendances Python utilisées pour le run ;
- vérifier si la température du juge est explicitement configurée ;
- vérifier le format de réponse demandé au juge ;
- compléter la section environnement du manifeste ;
- autoriser formellement l’exécution ;
- préparer ou finaliser le script d’exécution du smoke test ;
- exécuter les 20 cas ;
- produire les sorties NeoMundi ;
- produire les sorties de la baseline ;
- produire la matrice de confusion ;
- produire le journal des erreurs ;
- calculer les métriques ;
- réaliser la revue humaine des résultats ;
- décider s’il faut corriger la chaîne ou poursuivre vers un corpus plus large.

---

## 6. Première étape exacte à la reprise

La reprise doit commencer uniquement après la réponse de Manal.

Informations attendues :

```text
JUDGE_BASE_URL
JUDGE_MODEL
HALLUCINATION_JUDGE_FALLBACK_MODEL
```

Informations complémentaires utiles :

```text
type d’endpoint
température du juge
format de réponse
système d’exploitation du serveur
méthode de déploiement ou d’exécution
fichier de dépendances utilisé
```

Aucune clé API ne doit être demandée ou enregistrée.

Première action à la reprise :

> Mettre à jour la section `environment` du manifeste avec les valeurs confirmées par Manal.

---

## 7. Deuxième étape à la reprise

Après mise à jour de l’environnement :

> Vérifier que toutes les conditions préalables à l’exécution sont satisfaites.

Les points suivants devront être vrais :

```json
{
  "metric_frozen": true,
  "threshold_frozen": true,
  "baseline_frozen": true,
  "protocol_frozen": true,
  "corpus_frozen": true,
  "frozen_validation_passed": true,
  "repository_freeze_anchor_recorded": true,
  "environment_recorded": true
}
```

L’exécution devra rester interdite tant qu’un champ d’environnement important reste :

```text
TO_BE_RECORDED
TO_BE_DEFINED
```

---

## 8. Troisième étape à la reprise

Lorsque l’environnement est complet :

> Autoriser explicitement le smoke test.

Le manifeste devra être mis à jour avec :

```json
{
  "execution_authorized": true,
  "authorized_by": "Sebastien",
  "authorization_date": "DATE_ET_HEURE_UTC"
}
```

Le statut du run pourra alors passer de :

```text
FROZEN_PENDING_ENVIRONMENT
```

à :

```text
AUTHORIZED_FOR_EXECUTION
```

Cette autorisation devra intervenir avant la première exécution.

---

## 9. Quatrième étape à la reprise

Préparer et vérifier le runner du smoke test.

Le runner devra :

1. lire le corpus gelé ;
2. vérifier le hash avant exécution ;
3. refuser de démarrer si le hash diffère ;
4. envoyer uniquement le prompt et la réponse au signal testé ;
5. ne jamais envoyer le label de vérité terrain à NeoMundi ;
6. enregistrer le score `factual_hallucination_score` ;
7. enregistrer `is_hallucinated` ;
8. enregistrer les informations de fallback ;
9. enregistrer les erreurs ;
10. produire un fichier de sortie séparé ;
11. ne pas modifier le corpus source.

---

## 10. Cinquième étape à la reprise

Exécuter le smoke test de 20 cas.

Sorties attendues :

```text
results/EXP-001/EXP-001_smoke_test_neomundi_outputs.csv
results/EXP-001/EXP-001_smoke_test_baseline_outputs.csv
results/EXP-001/EXP-001_smoke_test_confusion_matrix.csv
results/EXP-001/EXP-001_smoke_test_error_log.csv
results/EXP-001/EXP-001_smoke_test_report_FR.md
```

Le run doit conserver :

- la date et l’heure ;
- la version du juge ;
- le modèle ;
- l’endpoint non secret ;
- le système d’exploitation ;
- le commit backend ;
- l’ancre du repository expérimental ;
- le hash du corpus ;
- le seuil ;
- les erreurs ;
- les fallbacks ;
- la latence si disponible.

---

## 11. Revue humaine des résultats

La revue humaine des résultats intervient après l’exécution.

Elle ne doit pas modifier rétroactivement :

- le corpus ;
- les labels ;
- la baseline ;
- le seuil ;
- le protocole ;
- les sorties brutes.

Elle devra vérifier :

- les faux positifs ;
- les faux négatifs ;
- les résultats de fallback ;
- les erreurs de calcul ;
- les réponses où le juge semble avoir mal interprété le prompt ;
- la cohérence entre score et classification ;
- les cas où un score `0.0` provient d’une indisponibilité ;
- les écarts entre NeoMundi et la baseline.

Les observations humaines devront être conservées dans un fichier séparé.

La revue ne doit pas servir à corriger silencieusement les résultats du run.

---

## 12. Résultats à calculer

Le smoke test devra produire :

- vrais positifs ;
- faux positifs ;
- vrais négatifs ;
- faux négatifs ;
- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- score F1 ;
- couverture ;
- nombre de fallbacks ;
- nombre d’erreurs ;
- nombre de résultats indisponibles.

Compte tenu de la taille de 20 cas, ces résultats ne devront pas être présentés comme statistiquement généralisables.

---

## 13. Décision après le smoke test

Trois décisions sont possibles.

### 13.1 Chaîne fonctionnelle

Si :

- les entrées sont correctement lues ;
- les sorties sont correctement produites ;
- les erreurs sont traçables ;
- les labels restent cachés ;
- la matrice de confusion est calculable ;
- les fallbacks sont correctement identifiés ;

alors le smoke test peut être déclaré techniquement réussi.

Cela n’implique pas que `MET-003` est validé.

---

### 13.2 Chaîne fonctionnelle avec corrections nécessaires

Si le run fonctionne mais révèle :

- une ambiguïté de sortie ;
- une confusion entre `0.0` réel et `0.0` de fallback ;
- une information manquante ;
- une erreur de mapping ;
- une mauvaise gestion des statuts ;

alors la chaîne devra être corrigée avant un nouveau run versionné.

---

### 13.3 Chaîne non exploitable

Si :

- les sorties ne sont pas reproductibles ;
- les erreurs ne sont pas identifiables ;
- les labels ont contaminé l’évaluation ;
- le modèle juge n’est pas versionnable ;
- le fallback masque les indisponibilités ;

alors le run devra être arrêté et classé comme non exploitable.

---

## 14. Conditions avant toute exécution

Aucune exécution ne doit commencer tant que les éléments suivants ne sont pas finalisés :

- métrique gelée ;
- seuil gelé ;
- baseline gelée ;
- protocole gelé ;
- corpus gelé ;
- hash enregistré ;
- validation `frozen` réussie ;
- commit backend enregistré ;
- ancre du repository expérimental enregistrée ;
- environnement du juge enregistré ;
- dépendances documentées ;
- autorisation explicite activée.

Le manifeste doit notamment contenir :

```json
{
  "metric_frozen": true,
  "threshold_frozen": true,
  "baseline_frozen": true,
  "protocol_frozen": true,
  "corpus_frozen": true,
  "frozen_validation_passed": true,
  "repository_freeze_anchor_recorded": true,
  "environment_recorded": true,
  "execution_authorized": true
}
```

---

## 15. Éléments à ne plus modifier

Sans création d’une nouvelle version, il est interdit de modifier :

- `EXP-001_smoke_test_20_cases_FR.csv`
- le hash du corpus ;
- `EXP-001_factuality_baseline_FR.md`
- `EXP-001_smoke_test_execution_protocol_FR.md`
- `EXP-001_signal_selection_FR.md`
- le seuil `0.5` ;
- l’opérateur `>=` ;
- l’identifiant `MET-003` ;
- l’événement cible `EVT-003` ;
- le commit backend `f02f7ff`.

Toute modification exige :

- une nouvelle version ;
- une justification ;
- un nouveau hash si le corpus change ;
- une nouvelle validation ;
- une nouvelle autorisation d’exécution.

---

## 16. Non-claims maintenus

À ce stade :

- `MET-003` n’est pas validé scientifiquement ;
- le seuil `0.5` n’est pas calibré ;
- le smoke test ne mesure pas une performance généralisable ;
- le corpus de 20 cas ne représente pas une prévalence réelle ;
- l’absence d’alerte ne prouve pas qu’une réponse est vraie ;
- une alerte ne constitue pas une preuve indépendante de fausseté ;
- le commit privé du backend ne constitue pas une preuve publique autonome ;
- aucun claim commercial général ne peut être produit à partir de ce smoke test.

---

## 17. Résumé opérationnel

### Réalisé

```text
Métrique documentée : oui
Implémentation identifiée : oui
Commit backend enregistré : oui
Seuil documenté : oui
Seuil gelé : oui
Baseline définie : oui
Baseline gelée : oui
Références documentées : oui
Revue humaine des cas terminée : oui
Splits attribués : oui
Corpus gelé : oui
Hash enregistré : oui
Validation frozen réussie : oui
Protocole gelé : oui
Ancre du repository enregistrée : oui
```

### En attente

```text
JUDGE_BASE_URL confirmé : non
JUDGE_MODEL confirmé : non
Fallback confirmé : non
Environnement enregistré : non
Dépendances enregistrées : non
Exécution autorisée : non
Run exécuté : non
Matrice de confusion produite : non
Revue humaine des résultats réalisée : non
```

---

## 18. Première phrase à utiliser à la reprise

> Manal a confirmé la configuration réelle du juge. Nous devons maintenant mettre à jour l’environnement du manifeste EXP-001 sans modifier les éléments déjà gelés.

---

## 19. Statut final du checkpoint

- **Expérience :** `EXP-001`
- **Version :** `v0.1`
- **Type :** smoke test technique et méthodologique
- **Statut :** `FROZEN_PENDING_ENVIRONMENT`
- **Blocage actuel :** confirmation de la configuration serveur du juge principal et du fallback
- **Prochaine action :** mise à jour de la section environnement du manifeste
- **Exécution autorisée :** non
- **Revue humaine des cas :** terminée
- **Revue humaine des résultats :** non commencée
- **Responsable :** Sébastien
- **Date du checkpoint :** 2 août 2026
