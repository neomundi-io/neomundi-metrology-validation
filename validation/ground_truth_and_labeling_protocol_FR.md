# Protocole de vérité terrain et d’annotation NeoMundi

## 1. Objet

Ce document définit la manière dont les observations NeoMundi sont évaluées, labellisées et comparées à une référence de validation.

L’objectif est de construire une vérité terrain suffisamment explicite pour mesurer les vrais positifs, faux positifs, vrais négatifs et faux négatifs des signaux NeoMundi.

---

## 2. Principe général

Un signal NeoMundi ne constitue pas automatiquement une vérité ni un verdict.

Chaque signal doit être comparé à :

- une référence objective ;
- une règle normative explicite ;
- un jugement humain structuré ;
- ou un événement cible préalablement défini.

---

## 3. Catégories de référence

### 3.1 Vérité terrain objective

Cas disposant d’une réponse vérifiable de manière indépendante.

Exemples :

- calcul mathématique ;
- date vérifiée ;
- information présente dans une source de référence ;
- réponse explicitement contenue dans le corpus ;
- règle logique déterministe.

### 3.2 Référence normative

Cas évalué par rapport à une règle déclarée.

Exemples :

- politique interne ;
- consigne utilisateur ;
- règle métier ;
- contrat de gouvernance ;
- procédure de conformité.

### 3.3 Jugement humain ou expert

Cas ne disposant pas d’une réponse binaire immédiate.

Ces cas nécessitent :

- une grille commune ;
- deux évaluateurs lorsque cela est possible ;
- une justification ;
- une procédure d’arbitrage en cas de désaccord.

### 3.4 Signal exploratoire sans vérité binaire

Cas pour lesquels aucun positif ou négatif ne peut encore être défini directement.

Exemples :

- densité informationnelle ;
- variation stylistique ;
- évolution progressive ;
- certains signaux thermodynamiques exploratoires.

Avant validation, l’événement cible doit être défini.

---

## 4. Définition de l’événement cible

Pour chaque métrique ou signal, il faut écrire une phrase précise :

> Le signal cherche à détecter…

Exemple :

> Le signal cherche à détecter une réponse contenant une erreur factuelle significative selon une référence vérifiée.

Un événement cible doit être :

- observable ;
- compréhensible ;
- reproductible ;
- suffisamment précis pour permettre une décision ;
- indépendant du signal testé.

---

## 5. Labels principaux

Les labels standards sont :

- `POSITIVE` : l’événement cible est réellement présent ;
- `NEGATIVE` : l’événement cible est absent ;
- `AMBIGUOUS` : les éléments disponibles ne permettent pas de conclure ;
- `NOT_APPLICABLE` : le cas ne relève pas de l’événement étudié ;
- `REVIEW_REQUIRED` : une expertise ou une source supplémentaire est nécessaire.

---

## 6. Matrice de classification

| Réalité | Signal NeoMundi | Classification |
|---|---|---|
| Événement présent | Alerte | Vrai positif |
| Événement absent | Alerte | Faux positif |
| Événement présent | Pas d’alerte | Faux négatif |
| Événement absent | Pas d’alerte | Vrai négatif |

Les cas ambigus ne doivent pas être artificiellement transformés en positifs ou négatifs.

---

## 7. Processus d’annotation

Pour chaque observation :

1. identifier l’événement cible ;
2. consulter la référence autorisée ;
3. attribuer un label ;
4. indiquer le niveau de confiance ;
5. rédiger une justification courte ;
6. signaler toute ambiguïté ;
7. enregistrer l’identité ou le code de l’évaluateur ;
8. dater l’annotation ;
9. enregistrer la version du guide utilisée.

---

## 8. Niveaux de confiance

- `HIGH` : conclusion directement vérifiable ;
- `MEDIUM` : conclusion solide mais comportant une part d’interprétation ;
- `LOW` : conclusion incertaine ou dépendante du contexte.

Les labels à faible confiance doivent être revus avant utilisation dans une validation finale.

---

## 9. Désaccord entre évaluateurs

En cas de désaccord :

1. conserver les deux annotations initiales ;
2. identifier la source du désaccord ;
3. vérifier si le guide est suffisamment précis ;
4. organiser un arbitrage ;
5. conserver la justification finale ;
6. ne jamais effacer les décisions initiales.

---

## 10. Accord inter-évaluateurs

Lorsque plusieurs évaluateurs interviennent, NeoMundi doit mesurer leur niveau d’accord.

Les métriques exactes seront choisies selon :

- le nombre d’évaluateurs ;
- le type de labels ;
- la taille du corpus ;
- la présence ou non de catégories ordinales.

Le résultat doit être accompagné d’une analyse des désaccords.

---

## 11. Séparation des jeux de données

Le corpus labellisé doit être séparé en :

- jeu de calibration ;
- jeu de validation ;
- jeu de test final gelé.

Les seuils ne doivent pas être ajustés sur le jeu de test final.

---

## 12. Traçabilité minimale

Chaque annotation doit contenir :

- identifiant de l’observation ;
- identifiant du cas ;
- événement cible ;
- référence utilisée ;
- label ;
- confiance ;
- justification ;
- évaluateur ;
- date ;
- version du protocole ;
- statut d’arbitrage.

---

## 13. Limites

Une annotation humaine peut être incorrecte.

Une référence peut être incomplète ou obsolète.

Un accord élevé entre évaluateurs ne prouve pas que leur décision est vraie.

La qualité de la validation dépend directement de la qualité de l’événement cible, de la référence et du guide d’annotation.

---

## 14. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Propriétaire de la décision : Sébastien
- Date de création : 27 juillet 2026
