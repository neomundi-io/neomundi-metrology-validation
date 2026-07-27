# Journal des décisions méthodologiques NeoMundi

## 1. Objet

Ce document trace les décisions méthodologiques prises dans le cadre de la définition, de la validation et de l’évolution des mesures NeoMundi.

L’objectif est de conserver l’historique des choix, de leurs justifications et de leurs impacts.

---

## 2. Principe général

Toute décision susceptible de modifier :

- une métrique ;
- une formule ;
- un seuil ;
- une interprétation ;
- un corpus ;
- un protocole ;
- une règle d’annotation ;
- une baseline ;
- un claim ;
- un niveau de preuve ;

doit être enregistrée dans ce journal.

---

## 3. Règles d’utilisation

Chaque décision doit :

- disposer d’un identifiant unique ;
- être datée ;
- préciser son statut ;
- identifier le problème traité ;
- décrire la décision prise ;
- indiquer les éléments examinés ;
- préciser les impacts ;
- identifier le responsable ;
- être reliée aux fichiers concernés ;
- indiquer si une revalidation est nécessaire.

Une décision passée ne doit pas être supprimée.

Lorsqu’elle est remplacée, elle doit être conservée avec le statut `SUPERSEDED`.

---

## 4. Statuts recommandés

- `PROPOSED` : décision proposée mais non validée ;
- `UNDER_REVIEW` : décision en cours d’examen ;
- `APPROVED` : décision validée ;
- `IMPLEMENTED` : décision appliquée ;
- `REJECTED` : proposition rejetée ;
- `SUPERSEDED` : décision remplacée par une décision plus récente ;
- `REVOKED` : décision annulée.

---

## 5. Modèle de décision

```text
DECISION_ID:
TITLE:
DATE:
STATUS:

CONTEXT:

PROBLEM:

DECISION:

RATIONALE:

EVIDENCE_REVIEWED:

ALTERNATIVES_CONSIDERED:

IMPACTED_METRICS:

IMPACTED_PROTOCOLS:

IMPACTED_CORPORA:

IMPACTED_CLAIMS:

IMPLEMENTATION_REQUIRED:

REVALIDATION_REQUIRED:

RESPONSIBLE_PERSON:

REVIEWERS:

EFFECTIVE_VERSION:

RELATED_FILES:

RELATED_EXPERIMENTS:

LIMITATIONS:

FOLLOW_UP_ACTIONS:
