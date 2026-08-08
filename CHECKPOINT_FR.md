# CHECKPOINT — NeoMundi Metrology Validation

**Date du checkpoint : 8 août 2026**  
**Repository : `neomundi-metrology-validation`**  
**Branche : `main`**

---

# 1. État général

Le repository est consacré à la consolidation méthodologique, à la validation et à la reproductibilité des mesures NeoMundi.

L’objectif n’est pas de démontrer en une seule expérience que « NeoMundi fonctionne ».

L’objectif est de construire progressivement une **chaîne de preuves** permettant de déterminer :

- ce qui est défini ;
- ce qui est implémenté ;
- ce qui est effectivement mesuré ;
- ce qui est testé ;
- ce qui est calibré ;
- ce qui est comparé ;
- ce qui est reproduit ;
- ce qui peut être affirmé ;
- et ce qui reste hypothétique ou non démontré.

Principe général :

> **Un signal mesuré n’est pas automatiquement un verdict.**

Principe méthodologique :

> **Une affirmation NeoMundi doit gagner progressivement le droit d’être affirmée par accumulation de preuves documentées, versionnées et reproductibles.**

---

# 2. Situation au 8 août 2026

## EXP-001

**Statut : `SMOKE_TEST_TECHNICALLY_SUCCESSFUL`**

EXP-001 est clôturé.

Il ne doit plus être modifié rétrospectivement pour améliorer ses résultats.

Toute nouvelle étape expérimentale doit être réalisée dans une nouvelle expérience versionnée.

---

## EXP-002

**Statut : `NOT_STARTED`**

Aucun corpus, seuil, protocole ou claim spécifique à EXP-002 n’est encore gelé.

La définition d’EXP-002 constitue la prochaine étape.

---

# 3. Ce que cherchait EXP-001

EXP-001 visait une question volontairement simple :

> **La chaîne expérimentale permettant d’évaluer le signal de risque factuel MET-003 fonctionne-t-elle correctement sur un petit corpus contrôlé ?**

EXP-001 ne cherchait pas à démontrer :

- la performance générale de MET-003 ;
- sa validité scientifique complète ;
- l’optimalité du seuil 0.5 ;
- sa robustesse sur tous les modèles ;
- sa robustesse sur tous les domaines ;
- sa supériorité par rapport aux approches existantes.

Il s’agissait d’un **smoke test méthodologique et technique**.

---

# 4. Analogie simple

EXP-001 peut être compris comme le test d’un thermomètre.

Avant d’utiliser un thermomètre dans des situations complexes, on commence par lui présenter des températures que l’on connaît déjà.

Ici :

- certains cas contenaient volontairement une erreur factuelle ;
- d’autres étaient factuellement corrects ;
- NeoMundi ne recevait pas le label indiquant lequel était lequel ;
- NeoMundi produisait son signal ;
- une baseline indépendante produisait également une décision ;
- seulement ensuite, les résultats étaient comparés à la vérité terrain.

La logique est donc :

```text
Cas dont la vérité est connue
        ↓
Labels cachés à NeoMundi
        ↓
NeoMundi mesure
        ↓
Baseline indépendante mesure
        ↓
Ouverture de la vérité terrain
        ↓
Comparaison
        ↓
VP / FP / VN / FN
        ↓
Revue humaine
        ↓
Conclusion limitée à ce que l’expérience démontre réellement
```

---

# 5. Événement cible

EXP-001 porte sur :

```text
EVT-003
Erreur factuelle significative
```

Il s’agit de l’événement auquel la performance du signal testé doit être comparée.

Cette séparation est essentielle :

```text
événement cible ≠ métrique ≠ score ≠ décision
```

---

# 6. Signal testé

Métrique :

```text
MET-003
Signal de risque factuel
```

Champ implémenté :

```text
factual_hallucination_score
```

Champ de classification :

```text
is_hallucinated
```

Alias historique :

```text
hallucination_score
```

Version expérimentale :

```text
EXP001_MET003_v0.1
```

Implémentation :

```text
govern-v3/app/core/hallucination_detector.py
```

Fonction principale :

```text
detect_hallucination
```

Mécanisme :

```text
LLM_AS_JUDGE
```

---

# 7. Seuil EXP-001

Le seuil a été gelé avant l’exécution :

```text
factual_hallucination_score >= 0.5
```

Version :

```text
EXP001_THRESHOLD_v0.1
```

Important :

> Ce seuil est gelé pour EXP-001 mais n’est ni calibré ni démontré optimal.

Toute modification du seuil doit appartenir à une nouvelle expérience ou version méthodologique.

---

# 8. Corpus EXP-001

Corpus :

```text
experiments/EXP-001/EXP-001_smoke_test_20_cases_FR.csv
```

Identifiant :

```text
EXP001-SMOKE-20
```

Composition :

```text
20 cas
10 POSITIVE
10 NEGATIVE
10 paires correcte / incorrecte
```

Origine :

```text
SYNTHETIC
```

SHA-256 gelé :

```text
bd9ac82fd53aab35fba15ff999033f894f69775d256940f27694677720174ce1
```

Le runner refuse l’exécution si ce hash ne correspond plus.

---

# 9. Séparation des données pendant l’expérience

NeoMundi reçoit uniquement :

```text
prompt
response
```

NeoMundi ne reçoit pas :

```text
ground_truth_label
final_label
reviewer_labels
référence de vérité
classification attendue
```

Cette séparation empêche le système testé de connaître à l’avance la réponse attendue.

---

# 10. Baseline indépendante

Une baseline déterministe indépendante est utilisée.

Version :

```text
v0.1
```

Méthode :

```text
DETERMINISTIC_PROMPT_RESPONSE_RULES
```

Script :

```text
scripts/analyze_exp001_smoke_test.py
```

Analyseur :

```text
v0.2
```

La baseline reçoit uniquement :

```text
prompt
response
```

Elle ne reçoit pas :

```text
ground_truth_label
final_label
reviewer_labels
score NeoMundi
classification NeoMundi
```

La vérité terrain n’est utilisée qu’après production de la décision de baseline.

La séparation méthodologique est donc :

```text
VÉRITÉ TERRAIN
      ≠
BASELINE
      ≠
NEOMUNDI
```

---

# 11. Vérité terrain

Les labels du corpus constituent la vérité terrain gelée utilisée pour l’évaluation de ce smoke test.

Pour EXP-001 :

```text
POSITIVE
```

signifie que l’événement cible est présent.

```text
NEGATIVE
```

signifie que l’événement cible est absent.

Les labels ont été établis avant exposition aux résultats NeoMundi.

---

# 12. Environnement du juge

Les informations ont été confirmées par Manal le 8 août 2026.

Juge primaire :

```text
Provider : Infomaniak Euria
Model : mistral24b
```

Endpoint :

```text
https://api.infomaniak.com/2/ai/108205/openai/v1/chat/completions
```

Type :

```text
OpenAI-compatible /chat/completions
```

Température :

```text
0.1
```

La température est codée en dur pour la stabilité du scoring.

Le paramètre :

```text
response_format: json_object
```

n’est pas utilisé car il est rejeté par l’endpoint Euria.

Le juge reçoit l’instruction de produire du JSON libre.

Le backend tente ensuite :

1. JSON direct ;
2. JSON contenu dans un bloc de code ;
3. extraction du bloc `{...}` le plus large.

---

# 13. Fallback du juge

Fallback configuré :

```text
llama3.1:8b
```

Activation :

```text
automatique
```

Mécanisme :

```text
circuit breaker
```

Cooldown :

```text
30 secondes
```

Limite importante :

Les réponses `/v1/govern` observées pendant EXP-001 n’exposent pas explicitement si le fallback a été utilisé.

Le statut enregistré est donc :

```text
UNKNOWN_NOT_EXPOSED
```

Il est interdit de traduire cela en :

```text
NO_FALLBACK
```

---

# 14. Environnement backend documenté

Infrastructure :

```text
VM Ubuntu chez Infomaniak
```

Application :

```text
Docker
```

Image de base :

```text
python:3.11-slim
```

OS de base du conteneur :

```text
Debian
```

Déploiement :

```text
Docker Compose
```

Orchestration :

```text
Ansible
```

Commande :

```text
docker compose up -d
```

Dépendances :

```text
requirements.txt
pip
```

Service :

```text
govern-v3
```

---

# 15. API utilisée par EXP-001

Endpoint NeoMundi :

```text
POST https://api.neomundi.io/v1/govern
```

Mode :

```text
OBS
```

Authentification :

```text
X-API-Key
```

Payload :

```json
{
  "source_type": "llm",
  "mode": "OBS",
  "llm_prompt": "...",
  "llm_response": "...",
  "raw_metrics": {
    "token_count": 0,
    "latency_ms": 0
  }
}
```

La clé API n’est jamais stockée dans le repository.

Elle est stockée dans GitHub Actions comme :

```text
NEOMUNDI_API_KEY
```

Une clé dédiée à EXP-001 a été créée.

---

# 16. Runner EXP-001

Fichier :

```text
scripts/run_exp001_smoke_test.py
```

Version réussie :

```text
v0.1.1
```

Fonctions principales :

- lecture du manifeste ;
- vérification de l’autorisation ;
- vérification du SHA-256 du corpus ;
- vérification du nombre de cas ;
- vérification des éléments gelés ;
- lecture sécurisée de la clé API ;
- appel `/v1/govern` ;
- extraction du signal MET-003 ;
- classification avec le seuil gelé ;
- journalisation des erreurs ;
- traçabilité du run ;
- conservation de la réponse brute NeoMundi.

---

# 17. Workflows GitHub Actions

## Validation du runner

```text
.github/workflows/validate-exp001-runner.yml
```

Rôle :

- contrôle syntaxique ;
- import Python sans exécution ;
- aucun appel API.

---

## Exécution EXP-001

```text
.github/workflows/run-exp001-smoke-test.yml
```

Déclenchement :

```text
workflow_dispatch
```

Donc :

> aucune exécution automatique sur push.

Le run doit être lancé volontairement.

---

## Analyse post-run

```text
.github/workflows/analyze-exp001-smoke-test.yml
```

Rôle :

- récupérer l’artefact brut d’un run donné ;
- ne refaire aucun appel API ;
- générer la baseline ;
- générer les matrices de confusion ;
- produire le rapport ;
- produire les hashes.

---

# 18. Premier incident d’exécution

Une première tentative a échoué avant mesure.

Erreur :

```text
HTTP 403
Cloudflare Error 1010
browser_signature_banned
```

Cause :

La signature HTTP par défaut du client Python `urllib` a été bloquée par Cloudflare.

Conséquence :

```text
0 signal calculé
20 erreurs techniques
```

Cette tentative ne fait pas partie de la matrice de confusion du run réussi.

Correction :

Le runner `v0.1.1` utilise un `User-Agent` HTTP explicite.

Le runner a également été corrigé pour terminer avec un code d’échec si une erreur de calcul est enregistrée.

---

# 19. Run EXP-001 réussi

GitHub Run ID :

```text
31266032346
```

Run GitHub :

```text
Run EXP-001 Smoke Test #2
```

Run expérimental :

```text
EXP001-SMOKE-RUN-001
```

Résultat technique :

```text
20 cas prévus
20 cas traités
20 signaux calculés
0 signal indisponible
0 erreur de calcul
20 réponses HTTP 200
```

Statut :

```text
SUCCESS
```

---

# 20. Versions observées dans les sorties

```text
measurement_version = 3.0.0
normalizer_version = 1.0.0
runner_version = v0.1.1
github_run_id = 31266032346
github_run_attempt = 1
```

Le modèle juge configuré est documenté dans le manifeste mais n’est pas exposé explicitement dans chaque réponse `/v1/govern`.

---

# 21. Résultats NeoMundi EXP-001

Matrice de confusion :

| Résultat | Nombre |
|---|---:|
| VP | 10 |
| FP | 0 |
| VN | 10 |
| FN | 0 |
| Signal indisponible | 0 |
| Erreur de calcul | 0 |

Sur ce corpus uniquement :

```text
precision = 1.0
recall = 1.0
specificity = 1.0
F1 = 1.0
descriptive accuracy = 1.0
coverage = 1.0
```

Ces nombres décrivent **EXP-001 uniquement**.

Ils ne constituent pas une performance générale de NeoMundi.

---

# 22. Distribution des scores

## Cas POSITIVE

```text
n = 10
min = 0.9
max = 1.0
mean = 0.99
median = 1.0
```

## Cas NEGATIVE

```text
n = 10
min = 0.0
max = 0.0
mean = 0.0
median = 0.0
```

La séparation observée est complète sur ce petit corpus synthétique.

Elle ne doit pas être extrapolée.

---

# 23. Résultats de la baseline indépendante

Baseline :

```text
20 décisions
0 UNDETERMINED
```

Matrice :

| Résultat | Nombre |
|---|---:|
| VP | 10 |
| FP | 0 |
| VN | 10 |
| FN | 0 |
| Indéterminé | 0 |

La baseline et NeoMundi convergent donc sur les 20 cas.

Cette convergence est descriptive du corpus EXP-001.

Elle ne constitue pas une preuve de valeur incrémentale de NeoMundi.

---

# 24. Revue humaine post-run

Fichier :

```text
results/EXP-001/EXP-001_smoke_test_human_review_FR.md
```

Statut :

```text
HUMAN_REVIEW_COMPLETED
```

Décision :

```text
TECHNICALLY_SUCCESSFUL
```

Relecteur :

```text
Sébastien
```

Date :

```text
2026-08-08
```

La revue n’a identifié :

```text
0 faux positif
0 faux négatif
0 signal indisponible
0 erreur de calcul
0 incohérence score / classification
```

Les limites relatives au juge et au fallback ont été explicitement conservées.

---

# 25. Artefacts EXP-001

Les artefacts principaux sont :

```text
results/EXP-001/EXP-001_smoke_test_neomundi_outputs.csv
results/EXP-001/EXP-001_smoke_test_error_log.csv
results/EXP-001/EXP-001_smoke_test_baseline_outputs.csv
results/EXP-001/EXP-001_smoke_test_confusion_matrix.csv
results/EXP-001/EXP-001_smoke_test_report_FR.md
results/EXP-001/EXP-001_smoke_test_artifact_hashes.json
results/EXP-001/EXP-001_smoke_test_human_review_FR.md
```

---

# 26. Hashes finaux connus

Algorithme :

```text
SHA-256
```

Corpus :

```text
bd9ac82fd53aab35fba15ff999033f894f69775d256940f27694677720174ce1
```

Sorties NeoMundi :

```text
b2597b843859d1f07cc02321ec8083afeddae256c28688877c088d04af6bc542
```

Journal d’erreurs :

```text
e2d5b20f359b724bcc76a2fb18ededf59edb11eee9af10c2da318c6dd31ee255
```

Baseline :

```text
491a6598a1da22c15d9a775939496173fb3f4889b908ca25e01b6822eca0ea73
```

Matrice de confusion :

```text
e64d368d5a32364c63c599a4ab4555b9a26d9abbf479a07aef3f8315259d5e96
```

Rapport FR :

```text
d3a9208a30d9644961e1b71501f6429ca38f6861dbca3d7f9b4c04327acd3028
```

Le hash de la revue humaine n’était pas inclus dans le manifeste de hashes généré automatiquement par l’analyseur.

---

# 27. Ce qu’EXP-001 démontre

La formulation autorisée est :

> **EXP-001 v0.1 montre que la chaîne expérimentale utilisée pour tester MET-003 est techniquement fonctionnelle et traçable sur le corpus synthétique contrôlé de 20 cas utilisé dans ce smoke test.**

Plus simplement :

> **Le premier étage de la chaîne de validation fonctionne.**

---

# 28. Ce qu’EXP-001 ne démontre pas

EXP-001 ne permet pas d’affirmer :

- que MET-003 est scientifiquement validé ;
- que MET-003 possède une performance générale de 100 % ;
- que le seuil 0.5 est optimal ;
- que les résultats sont représentatifs de données naturelles ;
- que les résultats sont robustes à tous les modèles ;
- que les résultats sont robustes à toutes les langues ;
- que les résultats sont robustes à tous les domaines ;
- que NeoMundi est supérieur à une baseline classique ;
- que le signal possède une valeur prédictive ;
- qu’une absence d’alerte prouve la vérité ;
- qu’une alerte prouve à elle seule la fausseté ;
- qu’aucun fallback n’a été utilisé.

---

# 29. Pourquoi EXP-001 existe dans la chaîne de preuve

Les audits méthodologiques recommandent une progression du type :

```text
score produit
↓
métrique définie
↓
métrique testée
↓
métrique calibrée
↓
métrique comparée
↓
métrique reproduite
↓
métrique éventuellement validée dans un domaine défini
```

EXP-001 se situe au début de cette chaîne.

Il démontre principalement :

```text
définition
+
gel méthodologique
+
exécution contrôlée
+
capacité à produire une mesure
+
premier test positif / négatif
+
traçabilité
+
reproductibilité du pipeline
```

---

# 30. Correspondance avec les audits externes

Les audits ont notamment demandé :

- définition des événements cibles ;
- dictionnaire des métriques ;
- contrôles positifs et négatifs ;
- mesure VP / FP / VN / FN ;
- baselines ;
- revue humaine ;
- séparation calibration / validation / test ;
- gel des protocoles avant exécution ;
- reproductibilité ;
- versionnement ;
- réplication ;
- claims et non-claims ;
- validation longitudinale.

EXP-001 commence à satisfaire concrètement plusieurs de ces exigences.

Il ne les clôture pas toutes.

---

# 31. Niveaux d’échantillonnage à conserver

Cadre méthodologique de travail :

## Niveau 1 — Smoke test

Ordre de grandeur :

```text
10 positifs + 10 négatifs
```

Objectif :

```text
vérifier le pipeline
```

EXP-001 correspond à ce niveau.

---

## Niveau 2 — Première estimation expérimentale

Ordre de grandeur envisagé :

```text
environ 100 positifs + 100 négatifs
```

Objectifs :

- commencer à observer de vrais FP/FN ;
- tester des cas moins triviaux ;
- commencer à tester le seuil ;
- produire une première estimation expérimentale.

---

## Niveau 3 — Validation consolidée

Ordre de grandeur :

```text
300 à 500 positifs
+
300 à 500 négatifs
```

répartis sur plusieurs :

- modèles ;
- familles ;
- campagnes ;
- niveaux de difficulté ;
- éventuellement langues et contextes.

À terme, une affirmation forte peut nécessiter plus de 1 000 cas labellisés distribués.

---

# 32. Pourquoi EXP-001 ne doit plus être modifié

EXP-001 constitue désormais un objet historique de preuve.

Il contient :

```text
un protocole donné
+
un corpus donné
+
un seuil donné
+
une implémentation donnée
+
un environnement donné
+
un run donné
+
des résultats donnés
```

Modifier rétrospectivement ces éléments rendrait la chaîne de preuve ambiguë.

Toute amélioration doit devenir :

```text
EXP-002
EXP-003
...
```

ou une nouvelle version explicitement documentée.

---

# 33. Claims

Principe de travail à conserver :

Chaque affirmation doit être reliée à :

```text
claim
event_target
metric_or_signal
validation_reference
baseline
required_test
current_status
authorized_wording
prohibited_wording
limitations
evidence_location
methodology_version
decision_owner
```

Une affirmation peut avoir différents statuts :

```text
DEFINED
IMPLEMENTED
MEASURED
TESTED
CALIBRATED
COMPARED
REPLICATED
VALIDATED
HYPOTHETICAL
NOT_DEMONSTRATED
```

Il ne faut pas confondre ces niveaux.

---

# 34. Chaîne de preuve NeoMundi

La logique générale du programme méthodologique est :

```text
1. Définir le phénomène
      ↓
2. Définir l’événement cible
      ↓
3. Définir la métrique
      ↓
4. Définir la vérité terrain
      ↓
5. Définir une baseline
      ↓
6. Geler corpus / protocole / seuil
      ↓
7. Exécuter
      ↓
8. Produire les artefacts bruts
      ↓
9. Comparer
      ↓
10. Mesurer VP / FP / VN / FN
      ↓
11. Analyser les erreurs
      ↓
12. Revoir humainement
      ↓
13. Versionner et hasher
      ↓
14. Déterminer quels claims sont autorisés
      ↓
15. Répliquer
```

---

# 35. Principe de gouvernance méthodologique

À conserver :

> **L’humain qualifie et arbitre ; le pipeline calcule et documente.**

Le pipeline peut automatiser :

- calcul ;
- validation de structure ;
- hashing ;
- matrices de confusion ;
- rapports ;
- traçabilité ;
- comparaisons.

L’humain conserve notamment la responsabilité :

- des définitions ;
- du sens des événements cibles ;
- de la vérité terrain ;
- des ambiguïtés ;
- des claims ;
- des décisions méthodologiques ;
- des interprétations.

---

# 36. Limites actuelles identifiées

Plusieurs sujets restent ouverts.

## MET-003

- seuil non calibré ;
- corpus EXP-001 trivial ;
- dépendance à un juge LLM ;
- identité du juge non exposée par chaque sortie ;
- fallback non exposé ;
- absence de vrais cas difficiles dans EXP-001 ;
- absence de données naturelles ;
- absence de mesure de valeur incrémentale.

## Autres métriques

Le programme complet doit encore consolider notamment :

- stabilité ;
- cohérence ;
- variation sémantique ;
- ΔG ;
- densité informationnelle ;
- énergie ;
- Runtime R ;
- métriques de trajectoire ;
- autres métriques opérationnelles présentes dans NeoMundi.

---

# 37. Dictionnaire des métriques

L’un des chantiers structurants reste la construction d’un dictionnaire exécutable.

Chaque métrique devra idéalement préciser :

```text
nom
version
construit visé
événement cible
entrées
transformation / formule
échelle
bornes
sens du score
valeurs manquantes
seuil
méthode de calibration
dépendances
tests existants
validité connue
limites
exemple numérique
```

Un tiers doit progressivement pouvoir comprendre et recalculer la métrique.

---

# 38. Répétitions et longitudinal

Le programme de validation ne concerne pas seulement la factualité.

Les répétitions sont un objet métrologique central.

À terme, il faut analyser :

- variance intra-prompt ;
- cohérence des conclusions ;
- variations factuelles ;
- dispersion sémantique ;
- clusters ;
- ruptures ;
- plateaux ;
- récupération ;
- drift longitudinal.

Les baromètres hebdomadaires NeoMundi constituent déjà une base opérationnelle importante pour ce chantier.

---

# 39. Valeur incrémentale

Une question importante reste non résolue :

> **NeoMundi apporte-t-il une information utile qu’une méthode plus simple ne fournit pas ?**

À terme, comparer par exemple :

```text
baseline factuelle seule
vs
NeoMundi
```

ou :

```text
méthode classique
vs
méthode classique + NeoMundi
```

L’objectif n’est pas forcément de battre toutes les méthodes sur toutes les dimensions.

L’objectif est d’identifier précisément :

> **où la couche de mesure NeoMundi apporte une information incrémentale utile.**

---

# 40. Réplication indépendante

Une validation construite uniquement par NeoMundi n’est pas une réplication indépendante.

À terme, prévoir notamment :

- annotation en aveugle par des tiers ;
- réplication par une équipe extérieure ;
- autre environnement ;
- autre modèle ;
- éventuellement autre juge ;
- autres corpus ;
- reproduction des métriques à partir des artefacts.

Des auditeurs, chercheurs ou partenaires externes pourront intervenir à ce niveau.

---

# 41. Première question à traiter pour EXP-002

Ne pas créer EXP-002 avant d’avoir défini clairement :

> **Quelle question scientifique ou métrologique précise voulons-nous maintenant faire avancer ?**

Deux familles d’options sont possibles.

### Option A — Approfondir MET-003

Passer du smoke test à une première estimation expérimentale.

Exemple :

```text
100 POSITIVE
+
100 NEGATIVE
```

avec davantage de :

- difficultés ;
- nuances ;
- erreurs subtiles ;
- réponses partiellement exactes ;
- cas proches du seuil ;
- éventuellement données naturelles.

Questions :

- quel taux de FP ?
- quel taux de FN ?
- comment se comporte le seuil 0.5 ?
- où MET-003 échoue-t-il ?
- comment se compare-t-il à une baseline ?

### Option B — Commencer la validation d’une autre métrique

Par exemple :

- stabilité ;
- cohérence ;
- variation ;
- ΔG.

Dans ce cas, une nouvelle chaîne cible → métrique → contrôle doit être créée.

---

# 42. Recommandation de reprise

À la reprise, ne pas coder immédiatement EXP-002.

Première action :

```text
CHOISIR LA QUESTION EXP-002
```

Puis construire dans cet ordre :

```text
1. question
2. claim
3. événement cible
4. métrique
5. vérité terrain
6. baseline
7. design du corpus
8. critères de succès
9. protocole
10. gel
11. seulement ensuite exécution
```

---

# 43. Recommandation actuelle pour EXP-002

Orientation privilégiée à examiner :

> **Faire de EXP-002 la première estimation expérimentale de MET-003 sur un corpus plus difficile et suffisamment large pour commencer à observer réellement les faux positifs, faux négatifs et cas proches du seuil.**

Ordre de grandeur indicatif :

```text
100 cas POSITIVE
+
100 cas NEGATIVE
```

Cette proposition doit être discutée avant gel.

Elle n’est pas encore une décision méthodologique.

---

# 44. Ne pas oublier

À la reprise :

**NE PAS :**

- modifier EXP-001 ;
- modifier ses labels ;
- modifier son seuil ;
- présenter son résultat comme une validation générale ;
- annoncer « 100 % de précision NeoMundi » ;
- confondre succès technique et validation scientifique.

**FAIRE :**

- conserver EXP-001 comme première brique ;
- définir précisément EXP-002 ;
- continuer à accumuler les preuves ;
- relier chaque claim à son niveau de preuve ;
- publier aussi les limites et non-résultats.

---

# 45. Résumé ultra-court

```text
EXP-001 = CLOSED ✅

20 cas contrôlés
20 mesures
10 VP
10 VN
0 FP
0 FN
0 erreur
0 indisponible

Baseline indépendante : OK
Revue humaine : OK
Traçabilité : OK
Pipeline : OK

MET-003 scientifiquement validé : NON
Seuil 0.5 calibré : NON
Performance généralisable : NON

EXP-002 : NOT STARTED
```

---

# 46. Phrase de reprise

Lors de la prochaine session, reprendre avec :

> **EXP-001 est clôturé comme smoke test techniquement réussi. Nous devons maintenant définir EXP-002 sans modifier EXP-001. Commencer par choisir la question métrologique exacte que doit résoudre EXP-002, puis définir le claim, l’événement cible, la baseline, le corpus et le protocole avant toute exécution.**

---

# 47. État final du checkpoint

```text
EXP-001
STATUS = SMOKE_TEST_TECHNICALLY_SUCCESSFUL
CLOSED = TRUE

EXP-002
STATUS = NOT_STARTED

NEXT_ACTION
DEFINE_EXP_002
```
