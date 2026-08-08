🇫🇷 **Version française :** [README_FR.md](./README_FR.md) · 🇬🇧 **English version:** [README.md](./README.md)

# Audits et contributions méthodologiques externes

Ce répertoire conserve les contributions externes ayant participé à la consolidation méthodologique du programme **NeoMundi Metrology Validation**.

Ces contributions peuvent notamment :

- identifier des fragilités méthodologiques ;
- poser des questions de validation ;
- proposer des contrôles ou expériences ;
- contribuer à la définition de la roadmap expérimentale ;
- aider à préciser les limites des métriques et des claims ;
- contribuer à la reproductibilité et à la chaîne de preuve.

Ces contributions doivent être distinguées d’une validation ou d’une réplication scientifique.

```text
CONTRIBUTION EXTERNE
≠
AUDIT FORMEL
≠
VALIDATION
≠
RÉPLICATION
```

---

## Audits formels

### Stéphane Gorius — Audit méthodologique indépendant

**Document :** [Audit méthodologique indépendant — Kimi K3](./Audit_methodologique_independant_Stéphane%20Gorius.pdf)

**Auteur :** Stéphane Gorius  
**Affiliation :** R&D AIzyNow  
**Version :** 1.1 finale  
**Date :** 24 juillet 2026

Le document est présenté par son auteur comme un :

> **Audit méthodologique constructif et indépendant**

Il examine le rapport public NeoMundi consacré à l’observation runtime de Kimi K3.

L’audit a été réalisé dans une démarche indépendante et constructive, sur la base des éléments publiquement accessibles au moment de son analyse.

Son périmètre ne comprenait notamment pas l’accès complet :

- aux fichiers CSV / JSON ;
- au code de calcul ;
- aux prompts complets ;
- à la documentation interne des métriques.

Cette limitation est explicitement documentée dans l’audit.

L’objectif du rapport n’est pas de constituer une validation scientifique définitive de NeoMundi, mais d’identifier les éléments solides du dispositif ainsi que les renforcements méthodologiques nécessaires pour passer d’une instrumentation opérationnelle à une métrologie progressivement défendable.

L’audit identifie notamment la nécessité de renforcer :

- la définition opérationnelle des métriques ;
- la validité des construits ;
- la calibration ;
- les contrôles positifs et négatifs ;
- la mesure des faux positifs et faux négatifs ;
- la sensibilité aux perturbations connues ;
- l’exploitation des répétitions ;
- la séparation entre factualité, cohérence et conformité ;
- la reproductibilité ;
- la chaîne de preuve ;
- l’instrumentation runtime ;
- la validation longitudinale.

Il formule notamment comme objectif méthodologique le passage progressif :

```text
score opérationnel
↓
métrique définie
↓
métrique testée
↓
métrique calibrée
↓
métrique reproduite indépendamment
```

Plusieurs de ces recommandations ont contribué à structurer la roadmap expérimentale du repository `neomundi-metrology-validation`.

---

## Statut de cet audit

Ce document constitue :

```text
AUDIT MÉTHODOLOGIQUE EXTERNE
```

Il ne constitue pas :

```text
VALIDATION SCIENTIFIQUE
```

ni :

```text
RÉPLICATION INDÉPENDANTE
```

La distinction est importante.

Un audit peut :

- examiner une méthode ;
- identifier une faiblesse ;
- soulever une question ;
- proposer un contrôle ;
- recommander une expérience.

Une validation nécessite des données expérimentales adaptées et un protocole défini.

Une réplication nécessite qu’une autre personne, équipe ou infrastructure puisse reproduire un résultat selon une spécification documentée.

---

## Relation avec la roadmap expérimentale

Les contributions méthodologiques externes ne déterminent pas directement les conclusions de NeoMundi.

Elles contribuent à formuler les questions qui doivent être testées.

La relation recherchée est :

```text
QUESTION OU CRITIQUE EXTERNE
        ↓
QUESTION MÉTROLOGIQUE
        ↓
PROTOCOLE EXPÉRIMENTAL
        ↓
EXP-XXX
        ↓
RÉSULTATS
        ↓
REVUE
        ↓
CLAIM ÉVENTUELLEMENT AUTORISÉ
```

Une recommandation externe ne devient donc pas automatiquement une vérité méthodologique.

Elle devient une hypothèse, une question ou une exigence à tester.

---

## Autres contributions externes

D’autres chercheurs, ingénieurs, praticiens ou observateurs peuvent contribuer au programme en formulant :

- des questions ;
- des critiques ;
- des objections ;
- des propositions de tests ;
- des baselines ;
- des hypothèses alternatives ;
- des demandes de réplication.

Ces contributions peuvent être intégrées à la roadmap méthodologique lorsqu’elles permettent de renforcer la falsifiabilité, la reproductibilité ou la qualité de la chaîne de preuve.

Elles ne sont attribuées nominativement dans ce répertoire qu’avec l’accord explicite de leur auteur.

Cette règle permet de distinguer clairement :

```text
question externe utilisée méthodologiquement
```

de :

```text
contribution officiellement attribuée
```

et de :

```text
audit formel publié
```

---

## Principe

> **Une critique utile n’est pas un problème à éliminer : elle peut devenir une expérience à concevoir.**

Le rôle de ce répertoire est de conserver la trace des contributions externes qui participent à cette transformation.
