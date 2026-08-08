# NeoMundi Metrology Validation — Roadmap expérimentale

**Version :** `v0.1`  
**Date :** 8 août 2026  
**Statut :** `PROVISIONAL`  
**Repository :** `neomundi-metrology-validation`

---

## 1. Objet

Cette roadmap décrit la trajectoire expérimentale envisagée pour la consolidation métrologique de NeoMundi.

Elle ne constitue pas un protocole gelé.

Elle donne une direction au programme de validation afin de savoir :

- quelles questions doivent être posées ;
- dans quel ordre elles peuvent être abordées ;
- quelles preuves doivent progressivement être accumulées ;
- quelles affirmations peuvent devenir défendables ;
- quelles limites doivent continuer à être documentées.

Certaines expériences pourront :

- fusionner ;
- être scindées ;
- changer d’ordre ;
- être reformulées ;
- être remplacées par une expérience plus pertinente ;
- produire des sous-expériences ou réplications.

Principe général :

> **1 EXP = 1 question métrologique suffisamment précise pour recevoir une réponse expérimentale documentée.**

L’objectif n’est donc pas d’accumuler artificiellement des expériences.

L’objectif est de construire le minimum d’expériences nécessaires pour établir progressivement une chaîne de preuves solide.

---

# 2. Logique générale

La progression méthodologique recherchée est :

```text
signal produit
↓
signal défini
↓
événement cible défini
↓
métrique testée
↓
métrique confrontée à une vérité terrain
↓
erreurs mesurées
↓
métrique calibrée
↓
métrique comparée à des baselines
↓
métrique testée dans plusieurs conditions
↓
résultat reproduit
↓
domaine de validité progressivement établi
```

Une expérience ne doit donc pas chercher à démontrer que :

```text
NeoMundi fonctionne
```

en général.

Elle doit répondre à une question plus petite et vérifiable.

---

# 3. EXP-001 — Smoke test de MET-003

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

Corpus :

```text
20 cas
10 POSITIVE
10 NEGATIVE
```

Cas volontairement simples et synthétiques.

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

## Statut final

```text
SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

---

# 4. EXP-002 — Première estimation expérimentale de MET-003

**Statut :** `PLANNED`

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

Ce volume est indicatif et doit être confirmé avant gel du protocole.

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
- éventuellement cas naturels issus de données réelles.

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
- certaines familles de cas sont-elles nettement plus difficiles ?

## Résultat recherché

EXP-002 doit commencer à transformer :

```text
le pipeline fonctionne
```

en :

```text
nous commençons à connaître le comportement réel de MET-003
```

## Important

EXP-002 ne doit pas modifier EXP-001.

Un nouveau corpus, un nouveau manifeste et un nouveau protocole doivent être créés.

---

# 5. EXP-003 — Calibration, seuil et robustesse de MET-003

**Statut :** `PLANNED`

## Question principale

> **Le seuil de décision de MET-003 peut-il être calibré de manière reproductible et dans quelle mesure le signal reste-t-il robuste lorsque changent certaines conditions qui ne devraient pas modifier fortement le phénomène factuel observé ?**

## Pourquoi cette question ?

Un score ne suffit pas.

Il faut savoir comment transformer ce score en décision.

Le seuil utilisé dans EXP-001 :

```text
0.5
```

était gelé pour l’expérience mais n’a pas été démontré optimal.

EXP-003 doit étudier cette frontière.

## Questions secondaires

- `0.5` est-il un seuil pertinent ?
- existe-t-il un meilleur compromis entre précision et rappel ?
- que se passe-t-il pour les scores proches du seuil ?
- les résultats changent-ils fortement avec une paraphrase ?
- les résultats changent-ils avec la longueur de la réponse ?
- les résultats changent-ils selon le modèle juge ?
- les résultats changent-ils selon certaines formulations ?
- les mêmes cas restent-ils classés de manière comparable lors de répétitions ?
- existe-t-il des zones où le système devrait s’abstenir plutôt que produire une classification ferme ?

## Variables possibles

EXP-003 pourra comparer notamment :

```text
seuil
juge
paraphrase
longueur
style
difficulté
répétition
```

## Attention méthodologique

Les données utilisées pour choisir un seuil ne doivent pas être les mêmes que celles utilisées pour annoncer sa performance finale.

Il faut préserver la séparation :

```text
CALIBRATION
↓
VALIDATION
↓
TEST FINAL GELÉ
```

## Fusion éventuelle

EXP-003 pourra partiellement fusionner avec EXP-002 si le protocole permet de conserver une séparation stricte entre calibration et test final.

Sinon, les deux expériences doivent rester séparées.

---

# 6. EXP-004 — Validation de la stabilité inter-répétitions

**Statut :** `PLANNED`

## Question principale

> **Lorsque la même situation est exécutée plusieurs fois, les mesures NeoMundi permettent-elles de caractériser de manière reproductible la stabilité, la variabilité et les changements de comportement entre les réponses ?**

## Pourquoi cette question ?

NeoMundi repose fortement sur l’observation répétée.

La répétition permet de regarder non seulement :

```text
ce que répond un système
```

mais aussi :

```text
comment son comportement varie lorsqu’on lui redemande la même chose
```

Il faut donc définir précisément ce que signifie « stabilité ».

## Questions secondaires

- les dix réponses aboutissent-elles à la même conclusion ?
- utilisent-elles les mêmes faits ?
- donnent-elles les mêmes nombres ?
- citent-elles les mêmes entités ?
- certaines se contredisent-elles ?
- existe-t-il plusieurs clusters sémantiques ?
- quelle est la dispersion intra-prompt ?
- quelle est la dispersion inter-prompt ?
- une réponse peut-elle être stable mais factuellement fausse ?
- une réponse peut-elle être variable mais néanmoins correcte ?
- quelles variations sont normales ?
- quelles variations doivent être considérées comme significatives ?

## Dimensions à distinguer

La stabilité ne doit pas devenir un concept unique mélangeant plusieurs phénomènes.

Il faudra distinguer, lorsque pertinent :

```text
stabilité lexicale
stabilité sémantique
stabilité factuelle
stabilité décisionnelle
stabilité de conformité
```

## Objectif

EXP-004 doit contribuer à déterminer ce que la métrique de stabilité peut réellement soutenir comme interprétation.

---

# 7. EXP-005 — Validation de la cohérence

**Statut :** `PLANNED`

## Question principale

> **Les signaux NeoMundi associés à la cohérence réagissent-ils correctement et de manière reproductible lorsque des contradictions connues sont introduites dans une réponse ou entre plusieurs réponses ?**

## Pourquoi cette question ?

La cohérence n’est pas la factualité.

Une réponse peut être :

```text
cohérente mais fausse
```

ou :

```text
vraie mais incohérente
```

Elle peut également être :

```text
cohérente mais non conforme à la consigne
```

Ces dimensions doivent rester distinctes.

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

## Principe à préserver

```text
FAUX mais COHÉRENT
≠
VRAI mais INCOHÉRENT
```

---

# 8. EXP-006 — Sensibilité de ΔG, variation et signaux associés

**Statut :** `PLANNED`

## Question principale

> **Les métriques NeoMundi de variation, ΔG et signaux associés réagissent-elles dans le sens attendu lorsque l’on applique des perturbations contrôlées, tout en restant suffisamment stables face aux changements qui ne devraient pas modifier le phénomène mesuré ?**

## Pourquoi cette question ?

Une métrique utile doit posséder deux propriétés :

```text
elle doit bouger lorsque le phénomène ciblé change
```

et :

```text
elle ne doit pas bouger fortement lorsque seul un élément non pertinent change
```

Une valeur constante n’est pas automatiquement une bonne métrique.

Une valeur qui change tout le temps non plus.

## Perturbations contrôlées possibles

On peut partir d’une réponse de référence puis modifier séparément :

- factualité ;
- contradiction ;
- quantité d’information ;
- respect de la consigne ;
- longueur ;
- paraphrase ;
- latence artificielle ;
- densité ;
- structure argumentative ;
- certains composants runtime.

## Questions secondaires

- la métrique évolue-t-elle dans le sens attendu ?
- existe-t-il une relation dose-réponse ?
- une dégradation plus forte produit-elle un signal plus fort ?
- la métrique reste-t-elle stable face à une paraphrase équivalente ?
- réagit-elle artificiellement à la longueur ?
- réagit-elle artificiellement à la latence ?
- existe-t-il des saturations ?
- existe-t-il des branches quasi constantes ?
- quelles variables nuisibles influencent les scores ?
- certaines métriques mélangent-elles plusieurs phénomènes ?

## Méthodes possibles

EXP-006 pourra inclure :

```text
tests de sensibilité
tests de monotonie
tests d’ablation
tests de saturation
perturbations contrôlées
```

---

# 9. EXP-007 — Valeur incrémentale de NeoMundi

**Statut :** `PLANNED`

## Question principale

> **Les signaux NeoMundi apportent-ils une information mesurable supplémentaire par rapport à des baselines plus simples, et cette information améliore-t-elle certaines détections ou décisions ?**

## Pourquoi cette question ?

Démontrer qu’une métrique fonctionne ne démontre pas automatiquement qu’elle apporte de la valeur.

Il faut pouvoir poser la question :

> **Est-ce que nous apprenons quelque chose grâce à NeoMundi que nous n’aurions pas obtenu aussi facilement autrement ?**

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

Selon la métrique étudiée :

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
- améliore-t-il la stabilité d’une décision ?
- apporte-t-il une information complémentaire plutôt que redondante ?
- dans quels cas NeoMundi n’apporte-t-il aucune amélioration ?

## Transition recherchée

EXP-007 doit permettre de passer de :

```text
NeoMundi mesure quelque chose
```

à une formulation plus exigeante :

```text
Dans tel contexte précis,
la mesure NeoMundi apporte une information incrémentale observable.
```

## Non-résultats

Un résultat du type :

```text
NeoMundi ne dépasse pas la baseline sur cette tâche
```

est un résultat scientifique utile.

Il doit être conservé et publié comme tel.

---

# 10. EXP-008 — Réplication, généralisation et longitudinal

**Statut :** `PLANNED`

## Question principale

> **Les résultats obtenus dans les expériences précédentes se reproduisent-ils sur d’autres modèles, d’autres campagnes, d’autres environnements et dans le temps, idéalement avec l’intervention d’un tiers indépendant ?**

## Pourquoi cette question ?

Un résultat obtenu une fois peut être réel mais local.

Pour comprendre son domaine de validité, il faut essayer de le reproduire ailleurs.

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

EXP-008 doit également examiner la stabilité des observations dans le temps.

Il faudra distinguer :

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
- tiennent-elles chez plusieurs fournisseurs ?
- tiennent-elles plusieurs semaines ou plusieurs mois ?
- que se passe-t-il lors d’une mise à jour de modèle ?
- les résultats survivent-ils à un changement d’environnement ?
- un autre juge retrouve-t-il une conclusion comparable ?
- un tiers peut-il reproduire une partie de l’expérience ?
- les résultats dépendent-ils fortement de la configuration NeoMundi ?
- quelles modifications nécessitent une revalidation ?

## Réplication indépendante

Une étape importante sera qu’une personne ou équipe extérieure puisse :

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

EXP-008 pourra donc devenir une famille de réplications plutôt qu’une seule exécution.

---

# 11. Vue synthétique de la trajectoire EXP-001 → EXP-008

```text
EXP-001
Le pipeline expérimental fonctionne-t-il ?
        ✅
        ↓

EXP-002
MET-003 détecte-t-il réellement son événement cible
sur davantage de cas et sur des cas plus difficiles ?
        ↓

EXP-003
Peut-on calibrer MET-003 et vérifier
sa robustesse aux conditions de mesure ?
        ↓

EXP-004
Peut-on mesurer correctement
la stabilité et la variabilité inter-répétitions ?
        ↓

EXP-005
Peut-on mesurer correctement
la cohérence sans la confondre avec factualité ou conformité ?
        ↓

EXP-006
Les autres métriques réagissent-elles correctement
aux perturbations qu’elles prétendent mesurer ?
        ↓

EXP-007
NeoMundi apporte-t-il une information supplémentaire
par rapport à des baselines plus simples ?
        ↓

EXP-008
Les résultats se reproduisent-ils
sur d’autres systèmes, ailleurs et dans le temps ?
```

---

# 12. Version « 7 ans »

## EXP-001

> **Est-ce que notre thermomètre s’allume et donne la bonne réponse sur quelques choses très faciles ?**

Statut :

```text
OUI — terminé
```

---

## EXP-002

> **Est-ce qu’il fonctionne encore quand on lui donne beaucoup plus de choses et qu’elles deviennent plus difficiles ?**

---

## EXP-003

> **Où faut-il mettre les graduations du thermomètre et donne-t-il encore à peu près la même mesure lorsque les conditions changent un peu ?**

---

## EXP-004

> **Si on pose plusieurs fois la même question à une IA, peut-on mesurer si elle reste pareille ou si elle commence à changer ?**

---

## EXP-005

> **Peut-on voir quand une IA dit deux choses qui ne peuvent pas être vraies ensemble ?**

---

## EXP-006

> **Quand on abîme volontairement quelque chose dans une réponse, est-ce que l’aiguille qui est censée le mesurer bouge vraiment ?**

---

## EXP-007

> **Notre instrument nous apprend-il quelque chose que les outils plus simples ne nous disaient pas déjà ?**

---

## EXP-008

> **Si quelqu’un d’autre fait la même expérience, avec une autre IA ou à un autre moment, retrouve-t-il la même chose ?**

---

# 13. Les huit questions en une ligne

```text
EXP-001 — Est-ce que la chaîne fonctionne ?

EXP-002 — MET-003 fonctionne-t-il sur davantage de cas difficiles ?

EXP-003 — Peut-on calibrer et rendre robuste MET-003 ?

EXP-004 — Peut-on mesurer correctement la stabilité entre répétitions ?

EXP-005 — Peut-on mesurer correctement la cohérence ?

EXP-006 — Les autres métriques réagissent-elles réellement aux phénomènes qu’elles prétendent mesurer ?

EXP-007 — NeoMundi apporte-t-il une valeur incrémentale mesurable ?

EXP-008 — Les résultats sont-ils reproductibles ailleurs et dans le temps ?
```

---

# 14. Ce qui peut bouger

Cette roadmap n’est pas un engagement à réaliser exactement huit expériences.

Il est possible que :

```text
EXP-002 + EXP-003
```

puissent partiellement être regroupées.

Il est possible que :

```text
EXP-004
```

nécessite plusieurs sous-expériences.

Il est possible que :

```text
EXP-006
```

soit divisé selon plusieurs métriques.

Il est probable que :

```text
EXP-008
```

devienne un programme de réplications comprenant plusieurs runs ou plusieurs équipes.

L’ordre peut également évoluer selon les résultats.

---

# 15. Ce qui ne doit pas bouger

Même si la roadmap évolue, les principes suivants doivent rester stables :

1. définir la question avant l’expérience ;
2. définir l’événement cible ;
3. définir la métrique ;
4. définir la vérité terrain lorsque c’est possible ;
5. définir une baseline pertinente ;
6. définir le corpus ;
7. définir les critères de réussite ;
8. pré-enregistrer ou geler le protocole avant le test final ;
9. exécuter sans modifier la cible après lecture des résultats ;
10. conserver les résultats positifs comme négatifs ;
11. documenter les limites ;
12. relier chaque conclusion aux preuves disponibles.

---

# 16. Relation avec les claims NeoMundi

La roadmap expérimentale doit progressivement alimenter un registre de claims.

Chaque claim doit pouvoir répondre aux questions :

```text
Qu’affirmons-nous ?

Quel phénomène cette affirmation concerne-t-elle ?

Quelle métrique la soutient ?

Quelle expérience la teste ?

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

# 17. Trajectoire scientifique simplifiée

Les huit expériences peuvent également être regroupées en quatre grandes étapes.

## Étape A — Vérifier

```text
EXP-001
```

Question :

> La chaîne fonctionne-t-elle ?

---

## Étape B — Mesurer et calibrer

```text
EXP-002
EXP-003
```

Questions :

> Quelle est la performance observée ?

> Comment calibrer correctement la mesure ?

---

## Étape C — Valider les principaux construits

```text
EXP-004
EXP-005
EXP-006
```

Questions :

> Mesurons-nous réellement stabilité, cohérence et variation comme nous le pensons ?

---

## Étape D — Démontrer utilité et reproductibilité

```text
EXP-007
EXP-008
```

Questions :

> Est-ce utile par rapport à ce qui existe déjà ?

> Est-ce reproductible ailleurs ?

---

# 18. Niveau de preuve recherché

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
instrument validé pour un périmètre explicitement défini
```

La validation ne doit jamais être considérée comme universelle par défaut.

---

# 19. Relation avec la métrologie NeoMundi

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
- son comportement longitudinal.

C’est cette accumulation qui permet progressivement de passer :

```text
signal observable
```

à :

```text
mesure défendable
```

---

# 20. Situation actuelle

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

# 21. Prochaine action

La prochaine action n’est pas de coder immédiatement EXP-002.

Elle consiste à transformer sa question générale :

> **Sur un corpus plus large et plus difficile, quelle est la capacité réelle de MET-003 à distinguer les réponses contenant une erreur factuelle significative des réponses ne contenant pas cet événement ?**

en protocole expérimental précis.

L’ordre recommandé est :

```text
1. claim
2. événement cible
3. métrique
4. vérité terrain
5. baseline
6. construction du corpus
7. stratégie d’annotation
8. calibration / validation / test
9. critères d’acceptation
10. plan d’analyse
11. protocole
12. gel
13. exécution
14. analyse
15. revue humaine
16. conclusion
```

---

# 22. Statut de la roadmap

```text
ROADMAP_VERSION = v0.1
ROADMAP_STATUS = PROVISIONAL

EXP-001 = CLOSED
EXP-002 = NEXT
EXP-003_TO_EXP-008 = PLANNED

NEXT_ACTION = DEFINE_EXP_002
```

---

# 23. Principe final

> **Nous ne cherchons pas à accumuler des expériences. Nous cherchons à accumuler les preuves nécessaires pour savoir exactement ce que les mesures NeoMundi permettent — et ne permettent pas — d’affirmer.**
