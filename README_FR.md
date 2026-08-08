🇫🇷 **Version française :** [README_FR.md](./README_FR.md) · 🇬🇧 **English version:** [README.md](./README.md)

## État actuel

### Première étape de validation terminée — EXP-001

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

> **la chaîne expérimentale fonctionne, elle est traçable, et elle peut maintenant être testée sur des corpus plus difficiles et plus larges.**

La prochaine étape de validation sera menée dans une nouvelle expérience versionnée, sans modifier rétrospectivement EXP-001.

---

## 2. Articulation avec le protocole de recherche

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

## 3. Origine et critiques méthodologiques externes

La roadmap ne part pas uniquement d’une réflexion interne.

Elle s’appuie également sur des audits et critiques méthodologiques externes ayant contribué à identifier les preuves manquantes, les risques d’interprétation et les expériences nécessaires.

### Audit méthodologique indépendant — Stéphane Gorius

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

Cet audit doit être conservé comme **contribution méthodologique externe**.

Il ne constitue pas une validation scientifique de NeoMundi.

Il contribue à documenter l’origine de certaines questions expérimentales de cette roadmap.

Emplacement recommandé dans le repository :

```text
external-audits/
├── README.md
└── Audit_methodologique_constructif_independant_NeoMundi_Kimi_K3_v1.1.pdf
```

Le dossier `external-audits/` doit clairement distinguer :

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

## 4. Position de ce repository dans l’écosystème NeoMundi

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

Elle permet de distinguer :

```text
OBSERVATION
≠
VALIDATION DE LA MESURE
≠
INTEROPÉRABILITÉ
≠
USAGE OU DÉCISION
```

Le repository `neomundi-metrology-validation` a donc vocation à être référencé :

- depuis le repository de l’Observatoire ;
- depuis la page principale de l’organisation NeoMundi ;
- depuis les documents méthodologiques lorsque la validité ou la qualification des métriques est discutée ;
- depuis les futures publications expérimentales associées aux EXP.

Il constitue le point d’entrée vers la **chaîne de preuve métrologique** de NeoMundi.

---

## 5. Principe de lecture de la roadmap

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

