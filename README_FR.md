🇫🇷 **Version française :** [README_FR.md](./README_FR.md) · 🇬🇧 **English version:** [README.md](./README.md)

# NeoMundi Metrology Validation

Programme expérimental de validation, calibration, reproductibilité et qualification des signaux de mesure NeoMundi.

Ce repository documente progressivement :

- ce que les mesures NeoMundi cherchent à observer ;
- comment elles sont testées ;
- dans quelles conditions elles fonctionnent ;
- où elles échouent ;
- comment elles se comparent à des références indépendantes ;
- et quelles affirmations les preuves disponibles permettent réellement de soutenir.

Principe central :

> **Un signal mesuré n’est pas automatiquement un verdict.**

---

# État actuel

## Première étape de validation terminée — EXP-001

NeoMundi a terminé son premier smoke test métrologique contrôlé.

On peut l’imaginer comme le test d’un thermomètre avec de l’eau dont on connaît déjà la température.

Nous avons préparé 20 cas simples :

- 10 contenant une erreur factuelle connue ;
- 10 ne contenant pas d’erreur factuelle.

Les bonnes réponses ont été cachées à NeoMundi.

NeoMundi a mesuré les 20 cas indépendamment.

Les résultats ont ensuite été comparés avec :

1. la vérité terrain gelée ;
2. une baseline déterministe indépendante ;
3. une revue humaine après exécution.

Sur ce smoke test contrôlé :

- 20 / 20 cas ont produit une mesure ;
- 0 erreur de calcul ;
- 0 signal indisponible ;
- 10 vrais positifs ;
- 10 vrais négatifs ;
- 0 faux positif ;
- 0 faux négatif.

Cela ne signifie **pas** que MET-003 est scientifiquement validé ou que NeoMundi atteint 100 % de performance en général.

Cela signifie quelque chose de plus simple et de plus important à ce stade :

> **La chaîne expérimentale fonctionne, elle est traçable, et elle peut maintenant être testée sur des corpus plus difficiles et plus larges.**

La prochaine étape de validation sera menée dans une nouvelle expérience versionnée, sans modifier rétrospectivement EXP-001.

Statut :

```text
EXP-001 = CLOSED
RESULT = SMOKE_TEST_TECHNICALLY_SUCCESSFUL

EXP-002 = NOT_STARTED
```

---

# Articulation avec le protocole de recherche

Cette roadmap expérimentale constitue la traduction opérationnelle du protocole de recherche NeoMundi :

[**Protocole de recherche — Le comportement runtime des IA constitue-t-il un objet métrologique distinct ?**](https://zenodo.org/records/21822050)

Le protocole pose la question scientifique générale suivante :

> **Les systèmes d’IA produisent-ils, pendant leur fonctionnement réel, des structures comportementales suffisamment réelles, reproductibles, distinctes et utiles pour constituer un objet métrologique autonome, complémentaire des métriques classiques ?**

Cette question ne peut pas recevoir une réponse crédible à partir d’une expérience unique ou d’une seule métrique.

Les expériences `EXP-001` à `EXP-008` ont pour fonction de décomposer cette question générale en questions expérimentales plus petites, falsifiables et documentables.

Elles doivent permettre d’accumuler progressivement les différents niveaux de preuve nécessaires.

| Grande question du protocole | Expériences qui y contribuent |
|---|---|
| **Le phénomène est-il mesurable ?** | EXP-001, EXP-002, EXP-003 |
| **Les mesures sont-elles répétables ?** | EXP-004 |
| **Peuvent-elles distinguer des phénomènes différents ?** | EXP-002, EXP-005, EXP-006 |
| **Apportent-elles une information distincte des métriques classiques ?** | EXP-007 |
| **Se reproduisent-elles ailleurs ?** | EXP-008 |
| **Tiennent-elles dans le temps ?** | EXP-004 + EXP-008 |
| **Possèdent-elles éventuellement une valeur prédictive ?** | EXP-008 et expériences longitudinales associées |
| **Améliorent-elles une décision ?** | EXP-007 principalement |
| **Le domaine métrologique runtime existe-t-il réellement ?** | **Conclusion cumulative de l’ensemble, pas d’une seule expérience** |

Le protocole distingue quatre niveaux généraux de preuve :

1. **Existence** — le phénomène existe-t-il au-delà du bruit ?
2. **Mesurabilité** — les métriques sont-elles répétables et sensibles ?
3. **Autonomie métrologique** — les signaux apportent-ils une information distincte des métriques classiques ?
4. **Actionnabilité** — la mesure améliore-t-elle effectivement une décision ?

La roadmap EXP-001 → EXP-008 doit progressivement apporter des éléments empiriques à chacun de ces niveaux.

La relation entre les différents objets est donc :

```text
PROTOCOLE DE RECHERCHE
Grande question scientifique
        ↓
ROADMAP EXPÉRIMENTALE
Décomposition en questions falsifiables
        ↓
EXP-001 → EXP-008
Expériences versionnées
        ↓
RÉSULTATS + ARTEFACTS + RÉPLICATIONS
Accumulation de preuves
        ↓
CLAIMS REGISTRY
Détermination de ce qui peut être affirmé
        ↓
CONCLUSION CUMULATIVE
Détermination progressive du domaine de validité
de la métrologie runtime NeoMundi
```

Principe essentiel :

> **Le succès d’une expérience isolée ou d’une métrique particulière ne suffit pas à démontrer l’existence d’un domaine métrologique runtime distinct.**

Inversement, l’échec local d’une métrique ne réfute pas nécessairement l’ensemble de l’hypothèse.

La conclusion devra émerger de l’accumulation des résultats concernant notamment :

- la répétabilité ;
- la sensibilité ;
- la validité discriminante ;
- les faux positifs et faux négatifs ;
- la calibration ;
- la reproductibilité externe ;
- la robustesse entre modèles et fournisseurs ;
- le comportement longitudinal ;
- la valeur prédictive éventuelle ;
- la valeur incrémentale par rapport aux métriques classiques ;
- l’actionnabilité opérationnelle.

---

# Origine et critiques méthodologiques externes

La roadmap ne part pas uniquement d’une réflexion interne.

Elle s’appuie également sur des audits et critiques méthodologiques externes ayant contribué à identifier les preuves manquantes, les risques d’interprétation et les expériences nécessaires.

## Audit méthodologique indépendant — Stéphane Gorius

Le rapport indépendant de Stéphane Gorius sur le rapport d’observation Kimi K3 a notamment identifié la nécessité de renforcer :

- la définition opérationnelle des métriques ;
- la calibration ;
- les contrôles positifs et négatifs ;
- la mesure des faux positifs et faux négatifs ;
- la sensibilité aux perturbations connues ;
- l’exploitation des répétitions ;
- la séparation entre factualité, cohérence et autres dimensions ;
- la reproductibilité ;
- la chaîne de preuve ;
- la comparaison avec des références indépendantes.

Cet audit est conservé comme **contribution méthodologique externe**.

Il ne constitue pas une validation scientifique de NeoMundi.

Il contribue à documenter l’origine de certaines questions expérimentales de cette roadmap.

Répertoire :

```text
external-audits/
```

Audit :

[**Audit méthodologique constructif et indépendant — Stéphane Gorius**](./external-audits/Audit_methodologique_constructif_independant_NeoMundi_Kimi_K3_v1.1.pdf)

La distinction suivante doit être conservée :

```text
AUDIT EXTERNE
≠
VALIDATION
≠
RÉPLICATION
```

Un audit peut identifier une faiblesse ou proposer une expérience.

Une validation nécessite des données expérimentales adaptées.

Une réplication nécessite qu’une autre équipe ou infrastructure puisse reproduire un résultat selon une spécification documentée.

---

# Position de ce repository dans l’écosystème NeoMundi

`neomundi-metrology-validation` a une fonction distincte des autres repositories NeoMundi.

Sa fonction principale est de documenter et qualifier progressivement la métrologie utilisée par NeoMundi.

Architecture conceptuelle :

```text
NeoMundi
│
├── neomundi-ai-observatory
│   │
│   └── Observe
│       Campagnes, baromètres, cartographies,
│       séries longitudinales et phénomènes observés
│
├── neomundi-metrology-validation
│   │
│   └── Qualifie la mesure
│       Définitions, contrôles, calibration,
│       validation, baselines, FP/FN,
│       reproductibilité et chaîne de preuve
│
├── runtime-interoperability-contract
│   │
│   └── Transporte les signaux
│       Contrats, sémantique et articulation
│       avec des infrastructures indépendantes
│
└── usages / launchers / pilotes
    │
    └── Utilisent les signaux
        Applications, gouvernance,
        orchestration et décisions externes
```

En formulation simple :

> **L’Observatoire regarde ce qui se passe.**

> **Metrology Validation vérifie progressivement si les instruments utilisés pour regarder mesurent réellement ce que nous disons qu’ils mesurent.**

> **Le contrat d’interopérabilité permet ensuite à ces signaux d’être compris et consommés par d’autres infrastructures.**

Cette séparation est volontaire.

```text
OBSERVATION
≠
VALIDATION DE LA MESURE
≠
INTEROPÉRABILITÉ
≠
USAGE OU DÉCISION
```

Le repository `neomundi-metrology-validation` a vocation à être référencé :

- depuis le repository de l’Observatoire ;
- depuis la page principale de l’organisation NeoMundi ;
- depuis les documents méthodologiques lorsque la validité ou la qualification des métriques est discutée ;
- depuis les futures publications expérimentales associées aux EXP.

Il constitue le point d’entrée vers la **chaîne de preuve métrologique** de NeoMundi.

---

# Principe de lecture de la roadmap

Les expériences décrites ci-dessous ne sont pas une succession destinée à produire artificiellement des résultats positifs.

Elles constituent une série de questions.

Chaque expérience peut produire :

```text
résultat positif
résultat limité
résultat ambigu
non-résultat
réfutation locale
```

Tous ces résultats sont informatifs.

La fonction de cette roadmap est de permettre à NeoMundi de passer progressivement de :

```text
Nous produisons des scores.
```

à :

```text
Nous savons précisément
ce que certaines mesures observent,
dans quelles conditions elles fonctionnent,
où elles échouent,
ce qu’elles apportent,
et quelles affirmations les preuves permettent de soutenir.
```

La question scientifique finale reste ouverte.

La roadmap est précisément l’instrument permettant d’essayer d’y répondre.

---

# Roadmap expérimentale

**Version :** `v0.1`  
**Date :** 8 août 2026  
**Statut :** `PROVISIONAL`

Cette roadmap donne une direction au programme de validation.

Elle ne constitue pas un protocole gelé.

Certaines expériences pourront :

- fusionner ;
- être scindées ;
- changer d’ordre ;
- être reformulées ;
- produire des sous-expériences ;
- être remplacées par un design plus pertinent.

Principe général :

> **1 EXP = 1 question métrologique suffisamment précise pour recevoir une réponse expérimentale documentée.**

L’objectif n’est pas d’accumuler artificiellement des expériences.

L’objectif est d’accumuler les preuves nécessaires pour déterminer progressivement ce que les mesures NeoMundi permettent réellement d’affirmer.

---

# EXP-001 — Smoke test de MET-003

**Statut :** `CLOSED`

## Question principale

> **La chaîne expérimentale permettant d’évaluer le signal de risque factuel MET-003 fonctionne-t-elle correctement sur un petit corpus contrôlé contenant des réponses factuellement correctes et incorrectes ?**

## Pourquoi cette question ?

Avant d’évaluer réellement la qualité d’un instrument, il faut vérifier que toute la chaîne fonctionne :

```text
cas
↓
vérité terrain
↓
mesure
↓
classification
↓
baseline
↓
comparaison
↓
matrice de confusion
↓
revue humaine
↓
artefacts
```

EXP-001 constitue cette première vérification.

## Design

```text
20 cas
10 POSITIVE
10 NEGATIVE
```

Les cas étaient volontairement simples et synthétiques.

La vérité terrain était connue avant l’exécution mais cachée au signal NeoMundi.

## Résultat

```text
20 cas traités
20 mesures calculées

10 vrais positifs
10 vrais négatifs
0 faux positif
0 faux négatif

0 erreur de calcul
0 signal indisponible
```

Baseline indépendante :

```text
10 VP
10 VN
0 FP
0 FN
```

Revue humaine :

```text
COMPLETED
```

## Conclusion autorisée

> **La chaîne expérimentale utilisée pour tester MET-003 fonctionne techniquement sur le corpus contrôlé d’EXP-001 et permet de produire des résultats traçables et analysables.**

## Ce qu’EXP-001 ne démontre pas

EXP-001 ne démontre pas :

- que MET-003 est scientifiquement validé ;
- que MET-003 possède une performance générale de 100 % ;
- que le seuil `0.5` est optimal ;
- que MET-003 fonctionne aussi bien sur des cas difficiles ;
- que MET-003 fonctionne aussi bien sur des données naturelles ;
- que NeoMundi apporte une valeur supplémentaire par rapport aux méthodes existantes.

Statut final :

```text
SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

---

# EXP-002 — Première estimation expérimentale de MET-003

**Statut :** `NOT_STARTED`

## Question principale

> **Sur un corpus gelé plus large et plus difficile, quelle est la capacité réelle de MET-003 à distinguer les réponses contenant une erreur factuelle significative des réponses ne contenant pas cet événement ?**

## Pourquoi cette question ?

EXP-001 vérifie principalement que le pipeline fonctionne.

EXP-002 doit commencer à répondre à une autre question :

> **Que vaut réellement le signal lorsqu’on arrête de lui donner uniquement des cas triviaux ?**

## Ordre de grandeur envisagé

```text
~100 POSITIVE
+
~100 NEGATIVE
```

Ce volume est indicatif et devra être confirmé avant gel du protocole.

## Types de cas envisagés

Le corpus devrait comporter davantage de :

- faits simples ;
- erreurs d’entité ;
- erreurs de dates ;
- erreurs numériques ;
- erreurs géographiques ;
- réponses partiellement exactes ;
- affirmations comportant plusieurs faits ;
- erreurs plus subtiles ;
- cas ambigus ;
- cas proches de la frontière de décision ;
- éventuellement cas naturels.

## Questions secondaires

- combien de vrais positifs ?
- combien de faux positifs ?
- combien de vrais négatifs ?
- combien de faux négatifs ?
- quelle est la précision ?
- quel est le rappel ?
- quelle est la spécificité ?
- quel est le F1 lorsque pertinent ?
- quels types d’erreurs sont les mieux détectés ?
- quels types d’erreurs sont manqués ?
- quelles réponses saines déclenchent artificiellement le signal ?
- quels scores apparaissent autour du seuil `0.5` ?
- certaines familles sont-elles nettement plus difficiles ?

## Résultat recherché

Passer de :

```text
le pipeline fonctionne
```

à :

```text
nous commençons à connaître
le comportement réel de MET-003
```

EXP-002 ne doit pas modifier EXP-001.

---

# EXP-003 — Calibration, seuil et robustesse de MET-003

**Statut :** `PLANNED`

## Question principale

> **Le seuil de décision de MET-003 peut-il être calibré de manière reproductible et dans quelle mesure le signal reste-t-il robuste lorsque changent certaines conditions qui ne devraient pas modifier fortement le phénomène factuel observé ?**

## Pourquoi cette question ?

Le seuil `0.5` utilisé dans EXP-001 était gelé pour l’expérience.

Il n’a pas été démontré optimal.

EXP-003 doit étudier cette frontière.

## Questions secondaires

- `0.5` est-il pertinent ?
- existe-t-il un meilleur compromis précision / rappel ?
- que se passe-t-il autour du seuil ?
- les résultats changent-ils avec une paraphrase ?
- avec la longueur ?
- avec le modèle juge ?
- avec certaines formulations ?
- les mêmes cas restent-ils comparables lors de répétitions ?
- existe-t-il une zone où une abstention serait préférable ?

## Variables possibles

```text
seuil
juge
paraphrase
longueur
style
difficulté
répétition
```

## Principe méthodologique

Les données utilisées pour calibrer un seuil ne doivent pas être les mêmes que celles servant à mesurer sa performance finale.

```text
CALIBRATION
↓
VALIDATION
↓
TEST FINAL GELÉ
```

EXP-002 et EXP-003 pourront éventuellement être regroupées si cette séparation peut être strictement préservée.

---

# EXP-004 — Validation de la stabilité inter-répétitions

**Statut :** `PLANNED`

## Question principale

> **Lorsque la même situation est exécutée plusieurs fois, les mesures NeoMundi permettent-elles de caractériser de manière reproductible la stabilité, la variabilité et les changements de comportement entre les réponses ?**

## Pourquoi cette question ?

La répétition permet d’observer non seulement :

```text
ce que répond un système
```

mais également :

```text
comment son comportement varie
lorsqu’on lui redemande la même chose
```

## Questions secondaires

- les réponses aboutissent-elles à la même conclusion ?
- utilisent-elles les mêmes faits ?
- donnent-elles les mêmes nombres ?
- citent-elles les mêmes entités ?
- certaines se contredisent-elles ?
- existe-t-il plusieurs clusters sémantiques ?
- quelle est la dispersion intra-prompt ?
- quelle est la dispersion inter-prompt ?
- une réponse peut-elle être stable mais fausse ?
- une réponse peut-elle être variable mais correcte ?
- quelles variations sont normales ?
- quelles variations sont significatives ?

## Dimensions à distinguer

```text
stabilité lexicale
stabilité sémantique
stabilité factuelle
stabilité décisionnelle
stabilité de conformité
```

EXP-004 doit contribuer à déterminer ce que la notion de stabilité peut réellement soutenir comme interprétation.

---

# EXP-005 — Validation de la cohérence

**Statut :** `PLANNED`

## Question principale

> **Les signaux NeoMundi associés à la cohérence réagissent-ils correctement et de manière reproductible lorsque des contradictions connues sont introduites dans une réponse ou entre plusieurs réponses ?**

## Pourquoi cette question ?

La cohérence n’est pas la factualité.

```text
cohérent mais faux
```

n’est pas équivalent à :

```text
vrai mais incohérent
```

La conformité à une instruction constitue encore une autre dimension.

## Cas de contrôle possibles

- contradiction explicite ;
- contradiction implicite ;
- changement de référent ;
- négation incompatible ;
- conclusion incompatible avec les arguments ;
- contradiction entre deux phrases ;
- contradiction entre plusieurs répétitions ;
- réponse cohérente mais factuellement fausse ;
- réponse factuellement correcte mais logiquement incohérente.

## Questions secondaires

- la cohérence locale est-elle correctement détectée ?
- la cohérence globale est-elle correctement détectée ?
- la cohérence inter-répétitions est-elle correctement mesurée ?
- les contradictions implicites sont-elles détectées ?
- la cohérence reste-t-elle indépendante de la factualité ?
- la cohérence reste-t-elle indépendante de la conformité ?

Principe :

```text
FAUX mais COHÉRENT
≠
VRAI mais INCOHÉRENT
```

---

# EXP-006 — Sensibilité de ΔG, variation et signaux associés

**Statut :** `PLANNED`

## Question principale

> **Les métriques NeoMundi de variation, ΔG et signaux associés réagissent-elles dans le sens attendu lorsque l’on applique des perturbations contrôlées, tout en restant suffisamment stables face aux changements qui ne devraient pas modifier le phénomène mesuré ?**

## Pourquoi cette question ?

Une métrique utile doit :

```text
bouger lorsque le phénomène ciblé change
```

mais également :

```text
rester suffisamment stable
lorsqu’un élément non pertinent change
```

Une valeur constante n’est pas automatiquement une bonne métrique.

Une valeur qui change tout le temps non plus.

## Perturbations contrôlées possibles

- factualité ;
- contradiction ;
- quantité d’information ;
- respect de la consigne ;
- longueur ;
- paraphrase ;
- latence artificielle ;
- densité ;
- structure argumentative ;
- composants runtime.

## Questions secondaires

- la métrique évolue-t-elle dans le sens attendu ?
- existe-t-il une relation dose-réponse ?
- une dégradation plus forte produit-elle un signal plus fort ?
- reste-t-elle stable face à une paraphrase équivalente ?
- réagit-elle artificiellement à la longueur ?
- à la latence ?
- existe-t-il des saturations ?
- des branches quasi constantes ?
- quelles variables nuisibles influencent les scores ?
- certaines métriques mélangent-elles plusieurs phénomènes ?

## Méthodes possibles

```text
tests de sensibilité
tests de monotonie
tests d’ablation
tests de saturation
perturbations contrôlées
```

---

# EXP-007 — Valeur incrémentale de NeoMundi

**Statut :** `PLANNED`

## Question principale

> **Les signaux NeoMundi apportent-ils une information mesurable supplémentaire par rapport à des baselines plus simples, et cette information améliore-t-elle certaines détections ou décisions ?**

## Pourquoi cette question ?

Démontrer qu’une mesure fonctionne ne démontre pas automatiquement qu’elle apporte de la valeur.

Il faut pouvoir demander :

> **Apprenons-nous quelque chose grâce à NeoMundi que nous n’aurions pas obtenu aussi facilement autrement ?**

## Comparaisons possibles

```text
baseline simple
vs
NeoMundi
```

puis éventuellement :

```text
baseline simple
vs
NeoMundi
vs
baseline + NeoMundi
```

## Exemples de baselines

- factualité simple ;
- similarité sémantique ;
- règle déterministe ;
- drift classique ;
- règles runtime ;
- classificateur standard ;
- modèle juge seul.

## Questions secondaires

- NeoMundi améliore-t-il la précision ?
- améliore-t-il le rappel ?
- réduit-il certains faux négatifs ?
- réduit-il certains faux positifs ?
- détecte-t-il des anomalies invisibles à la baseline ?
- apporte-t-il une détection plus précoce ?
- améliore-t-il une décision ?
- apporte-t-il une information complémentaire plutôt que redondante ?
- dans quels cas n’apporte-t-il aucune amélioration ?

Transition recherchée :

```text
NeoMundi mesure quelque chose
```

vers :

```text
Dans tel contexte précis,
la mesure NeoMundi apporte
une information incrémentale observable.
```

Un résultat du type :

```text
NeoMundi ne dépasse pas la baseline
sur cette tâche
```

est également un résultat scientifique utile et doit être conservé.

---

# EXP-008 — Réplication, longitudinal et valeur prédictive

**Statut :** `PLANNED`

## Question principale

> **Les résultats obtenus dans les expériences précédentes se reproduisent-ils sur d’autres modèles, d’autres campagnes, d’autres environnements et dans le temps, idéalement avec l’intervention d’un tiers indépendant ?**

## Question longitudinale et prédictive

> **Les variations ou dérives mesurées par NeoMundi précèdent-elles, accompagnent-elles ou aident-elles à expliquer de manière reproductible une dégradation observable ultérieure ?**

## Pourquoi cette question ?

Un résultat obtenu une fois peut être réel mais local.

Pour comprendre son domaine de validité, il faut essayer de le reproduire ailleurs et dans le temps.

## Dimensions de réplication

Les conclusions pourront être testées sur :

- un autre modèle ;
- un autre fournisseur ;
- une autre campagne ;
- une autre période ;
- une autre famille de prompts ;
- un autre environnement ;
- un autre juge ;
- une autre langue ;
- une autre équipe.

## Dimension longitudinale

Il faudra notamment distinguer :

```text
variation ponctuelle
rupture
tendance
plateau
récupération
drift
```

## Questions secondaires

- les conclusions tiennent-elles sur plusieurs modèles ?
- chez plusieurs fournisseurs ?
- plusieurs semaines ou plusieurs mois ?
- après une mise à jour de modèle ?
- dans un autre environnement ?
- avec un autre juge ?
- un tiers peut-il reproduire une partie de l’expérience ?
- les résultats dépendent-ils fortement de la configuration NeoMundi ?
- certaines dérives précèdent-elles une augmentation des erreurs ?
- une régression de qualité ?
- une hausse des coûts ?
- une instabilité décisionnelle ?
- un besoin accru de revue humaine ?
- quelles modifications déclenchent une revalidation ?

## Réplication indépendante

Une personne ou équipe extérieure devrait progressivement pouvoir :

```text
recevoir le protocole
↓
recevoir les artefacts nécessaires
↓
rejouer un sous-ensemble
↓
recalculer les résultats
↓
documenter les éventuels écarts
```

EXP-008 pourra donc devenir une famille de réplications et d’expériences longitudinales plutôt qu’une expérience unique.

---

# Vue synthétique EXP-001 → EXP-008

```text
EXP-001
Le pipeline expérimental fonctionne-t-il ?
        ✅
        ↓

EXP-002
MET-003 détecte-t-il réellement son événement cible
sur davantage de cas difficiles ?
        ↓

EXP-003
Peut-on calibrer MET-003
et vérifier sa robustesse ?
        ↓

EXP-004
Peut-on mesurer correctement
la stabilité et la variabilité ?
        ↓

EXP-005
Peut-on mesurer correctement
la cohérence ?
        ↓

EXP-006
Les autres métriques réagissent-elles correctement
aux phénomènes qu’elles prétendent mesurer ?
        ↓

EXP-007
NeoMundi apporte-t-il une information supplémentaire
par rapport à des baselines plus simples ?
        ↓

EXP-008
Les résultats se reproduisent-ils ailleurs,
dans le temps, et certains signaux
possèdent-ils une valeur prédictive ?
```

---

# Version « 7 ans »

## EXP-001

> **Est-ce que notre thermomètre s’allume et donne la bonne réponse sur quelques choses très faciles ?**

```text
OUI — terminé
```

## EXP-002

> **Est-ce qu’il fonctionne encore quand on lui donne beaucoup plus de choses et qu’elles deviennent plus difficiles ?**

## EXP-003

> **Où faut-il mettre les graduations du thermomètre et donne-t-il encore à peu près la même mesure lorsque les conditions changent un peu ?**

## EXP-004

> **Si on pose plusieurs fois la même question à une IA, peut-on mesurer si elle reste pareille ou si elle commence à changer ?**

## EXP-005

> **Peut-on voir quand une IA dit deux choses qui ne peuvent pas être vraies ensemble ?**

## EXP-006

> **Quand on abîme volontairement quelque chose dans une réponse, est-ce que l’aiguille qui est censée le mesurer bouge vraiment ?**

## EXP-007

> **Notre instrument nous apprend-il quelque chose que les outils plus simples ne nous disaient pas déjà ?**

## EXP-008

> **Si quelqu’un d’autre fait la même expérience, avec une autre IA ou à un autre moment, retrouve-t-il la même chose — et certains changements permettent-ils parfois de voir arriver une dégradation ?**

---

# Les huit questions en une ligne

```text
EXP-001 — Est-ce que la chaîne fonctionne ?

EXP-002 — MET-003 fonctionne-t-il sur davantage de cas difficiles ?

EXP-003 — Peut-on calibrer et rendre robuste MET-003 ?

EXP-004 — Peut-on mesurer correctement la stabilité entre répétitions ?

EXP-005 — Peut-on mesurer correctement la cohérence ?

EXP-006 — Les autres métriques réagissent-elles réellement aux phénomènes qu’elles prétendent mesurer ?

EXP-007 — NeoMundi apporte-t-il une valeur incrémentale mesurable ?

EXP-008 — Les résultats sont-ils reproductibles ailleurs et dans le temps, et certains signaux ont-ils une valeur prédictive ?
```

---

# Ce qui peut évoluer

Cette roadmap n’est pas un engagement à réaliser exactement huit expériences.

Par exemple :

```text
EXP-002 + EXP-003
```

pourront éventuellement être partiellement regroupées.

```text
EXP-004
```

pourra nécessiter plusieurs sous-expériences.

```text
EXP-006
```

pourra être scindée selon plusieurs métriques.

```text
EXP-008
```

pourra devenir un programme de réplications et d’études longitudinales.

L’ordre peut évoluer selon les résultats.

---

# Ce qui ne doit pas changer

Même si la roadmap évolue, les principes méthodologiques doivent rester stables :

1. définir la question avant l’expérience ;
2. définir l’événement cible ;
3. définir la métrique ;
4. définir la vérité terrain lorsque c’est possible ;
5. définir une baseline pertinente ;
6. définir le corpus ;
7. définir les critères de réussite ;
8. séparer calibration, validation et test final lorsque nécessaire ;
9. geler le protocole avant le test final ;
10. exécuter sans modifier la cible après lecture des résultats ;
11. conserver résultats positifs, négatifs et ambigus ;
12. documenter les limites ;
13. relier chaque conclusion à ses preuves ;
14. versionner les décisions méthodologiques ;
15. chercher progressivement la réplication indépendante.

---

# Relation avec les claims NeoMundi

La roadmap doit progressivement alimenter un registre de claims.

Chaque claim doit permettre de répondre à :

```text
Qu’affirmons-nous ?

Quel phénomène cette affirmation concerne-t-elle ?

Quelle métrique la soutient ?

Quelle expérience la teste ?

Quelle vérité terrain est utilisée ?

Quelle baseline est utilisée ?

Quel est le statut actuel de la preuve ?

Quelle formulation est autorisée ?

Quelle formulation est interdite ?

Quelles sont les limites ?

Où se trouvent les preuves ?
```

Les statuts pourront notamment être :

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

Le but est qu’aucun claim important ne soit déconnecté de sa chaîne de preuve.

---

# Trajectoire scientifique simplifiée

Les expériences peuvent être regroupées en quatre grandes étapes.

## Étape A — Vérifier

```text
EXP-001
```

Question :

> La chaîne fonctionne-t-elle ?

## Étape B — Mesurer et calibrer

```text
EXP-002
EXP-003
```

Questions :

> Quelle est la performance observée ?

> Comment calibrer correctement la mesure ?

## Étape C — Valider les principaux construits

```text
EXP-004
EXP-005
EXP-006
```

Question :

> Mesurons-nous réellement stabilité, cohérence et variation comme nous le pensons ?

## Étape D — Démontrer utilité et reproductibilité

```text
EXP-007
EXP-008
```

Questions :

> Est-ce utile par rapport à ce qui existe déjà ?

> Est-ce reproductible ailleurs ?

> Certaines mesures possèdent-elles une valeur longitudinale ou prédictive ?

---

# Niveau de preuve recherché

La roadmap doit faire progresser NeoMundi de :

```text
instrument opérationnel
```

vers :

```text
instrument documenté
```

puis :

```text
instrument testé
```

puis :

```text
instrument calibré
```

puis :

```text
instrument comparé
```

puis :

```text
instrument reproduit
```

et, seulement lorsque les preuves le permettront :

```text
instrument validé
pour un périmètre explicitement défini
```

La validation ne doit jamais être considérée comme universelle par défaut.

---

# Relation avec la métrologie NeoMundi

La finalité n’est pas de démontrer qu’un score isolé est « bon ».

La finalité est de construire une couche de mesure dont on connaît progressivement :

- ce qu’elle observe ;
- comment elle le mesure ;
- sa sensibilité ;
- ses erreurs ;
- ses limites ;
- sa reproductibilité ;
- son domaine de validité ;
- sa valeur incrémentale ;
- son comportement longitudinal ;
- sa valeur prédictive éventuelle ;
- son utilité opérationnelle.

C’est cette accumulation qui permet progressivement de passer :

```text
signal observable
```

à :

```text
mesure défendable
```

---

# Situation de la roadmap

Au 8 août 2026 :

```text
EXP-001
STATUS = CLOSED
RESULT = SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

```text
EXP-002
STATUS = NOT_STARTED
```

```text
EXP-003
STATUS = PLANNED
```

```text
EXP-004
STATUS = PLANNED
```

```text
EXP-005
STATUS = PLANNED
```

```text
EXP-006
STATUS = PLANNED
```

```text
EXP-007
STATUS = PLANNED
```

```text
EXP-008
STATUS = PLANNED
```

---

# Prochaine action

La prochaine action n’est pas de coder immédiatement EXP-002.

Elle consiste à transformer la question :

> **Sur un corpus plus large et plus difficile, quelle est la capacité réelle de MET-003 à distinguer les réponses contenant une erreur factuelle significative des réponses ne contenant pas cet événement ?**

en protocole expérimental précis.

Ordre recommandé :

```text
1. question
2. claim
3. événement cible
4. métrique
5. vérité terrain
6. baseline
7. construction du corpus
8. stratégie d’annotation
9. calibration / validation / test
10. critères d’acceptation
11. plan d’analyse
12. protocole
13. gel
14. exécution
15. analyse
16. revue humaine
17. conclusion
```

---

# Ressources

## Protocole scientifique

[**Le comportement runtime des IA constitue-t-il un objet métrologique distinct ?**](https://zenodo.org/records/21822050)

## Audit méthodologique externe

[**Audit méthodologique constructif et indépendant — Stéphane Gorius**](./external-audits/Audit_methodologique_constructif_independant_NeoMundi_Kimi_K3_v1.1.pdf)

## Checkpoint de travail

[**CHECKPOINT_FR.md**](./CHECKPOINT_FR.md)

---

# Statut de la roadmap

```text
ROADMAP_VERSION = v0.1
ROADMAP_STATUS = PROVISIONAL

EXP-001 = CLOSED
EXP-002 = NEXT
EXP-003_TO_EXP-008 = PLANNED

NEXT_ACTION = DEFINE_EXP_002
```

---

# Principe final

> **Nous ne cherchons pas à accumuler des expériences. Nous cherchons à accumuler les preuves nécessaires pour savoir exactement ce que les mesures NeoMundi permettent — et ne permettent pas — d’affirmer.**
