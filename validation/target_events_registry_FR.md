# Registre des événements cibles NeoMundi

## 1. Objet

Ce document définit ce que chaque signal NeoMundi cherche précisément à détecter.

Un signal ne peut pas être validé tant que son événement cible n’est pas formulé de manière observable, indépendante et testable.

---

## 2. Principe général

Pour chaque signal, il faut compléter la phrase :

> Ce signal cherche à détecter…

L’événement cible doit être :

- observable ;
- compréhensible ;
- reproductible ;
- indépendant du signal testé ;
- suffisamment précis pour permettre une annotation ;
- compatible avec une référence de validation.

---

## 3. Structure standard

Chaque événement cible doit contenir :

- identifiant ;
- nom ;
- dimension principale ;
- formulation opérationnelle ;
- unité d’analyse ;
- condition positive ;
- condition négative ;
- cas ambigus ;
- référence de validation ;
- signal associé ;
- seuil éventuel ;
- limites ;
- statut ;
- responsable de décision.

---

# EVT-001 — Instabilité inter-répétitions

## Identification

- **Identifiant :** EVT-001
- **Dimension :** stabilité
- **Signal associé :** score de stabilité
- **Statut :** à définir précisément

## Formulation opérationnelle

> Présence d’une variation significative entre plusieurs réponses produites pour un même cas dans des conditions définies comme comparables.

## Condition positive

L’événement est présent lorsque les répétitions présentent une divergence supérieure au seuil défini selon la méthode gelée.

## Condition négative

L’événement est absent lorsque les répétitions restent dans la plage de variation considérée comme normale.

## Cas ambigus

- variations uniquement stylistiques ;
- différences de longueur sans changement de sens ;
- réponses différentes mais toutes correctes ;
- données runtime incomplètes.

## Référence de validation

Revue humaine intra-prompt et comparaison à une baseline de similarité.

## Limites

L’instabilité ne signifie pas automatiquement erreur ou danger.

---

# EVT-002 — Variation sémantique significative

## Identification

- **Identifiant :** EVT-002
- **Dimension :** variation sémantique
- **Signal associé :** taux de variation sémantique
- **Statut :** à définir précisément

## Formulation opérationnelle

> Présence d’une différence de sens significative entre plusieurs réponses produites pour un même cas.

## Condition positive

Les réponses conduisent à des conclusions, informations ou recommandations substantiellement différentes.

## Condition négative

Les réponses conservent le même sens malgré des différences de formulation.

## Cas ambigus

- paraphrase ;
- différence de niveau de détail ;
- omission secondaire ;
- changement de ton ;
- variation lexicale sans changement de conclusion.

## Référence de validation

Annotation humaine selon une grille sémantique explicite.

## Limites

Une variation sémantique peut être acceptable et ne constitue pas automatiquement une erreur.

---

# EVT-003 — Erreur factuelle significative

## Identification

- **Identifiant :** EVT-003
- **Dimension :** factualité
- **Signal associé :** signal de risque factuel
- **Statut :** à figer

## Formulation opérationnelle

> Présence dans la réponse d’une affirmation factuelle incorrecte susceptible de modifier significativement la compréhension, la décision ou l’usage.

## Condition positive

Au moins une affirmation significative contredit une référence vérifiée.

## Condition négative

Aucune affirmation significative ne contredit la référence autorisée.

## Cas ambigus

- source incertaine ;
- fait évolutif ;
- désaccord entre références ;
- approximation acceptable ;
- information invérifiable ;
- question ouverte.

## Référence de validation

Vérité terrain objective ou revue experte documentée.

## Limites

Le caractère significatif dépend du contexte d’usage et doit être défini dans le protocole.

---

# EVT-004 — Violation d’instruction

## Identification

- **Identifiant :** EVT-004
- **Dimension :** respect des instructions
- **Signal associé :** signal de conformité aux instructions
- **Statut :** à documenter

## Formulation opérationnelle

> Non-respect d’une contrainte explicite contenue dans la requête.

## Condition positive

Une ou plusieurs consignes obligatoires ne sont pas respectées.

## Condition négative

Toutes les consignes obligatoires sont respectées.

## Cas ambigus

- consigne contradictoire ;
- consigne impossible ;
- consigne implicite ;
- conflit entre plusieurs instructions ;
- formulation insuffisamment précise.

## Référence de validation

Liste gelée des contraintes présentes dans le prompt.

## Limites

Le respect des instructions ne garantit ni la factualité ni la sécurité de la réponse.

---

# EVT-005 — Violation d’une règle déclarée

## Identification

- **Identifiant :** EVT-005
- **Dimension :** conformité
- **Signal associé :** règle runtime ou gouvernance
- **Statut :** à documenter

## Formulation opérationnelle

> Non-respect d’une règle métier, opérationnelle ou de gouvernance explicitement définie.

## Condition positive

La réponse ou l’action enfreint au moins une règle applicable.

## Condition négative

La réponse ou l’action respecte toutes les règles applicables évaluées.

## Cas ambigus

- règle incomplète ;
- règles contradictoires ;
- exception non documentée ;
- contexte insuffisant ;
- règle non applicable au cas.

## Référence de validation

Règle versionnée et traduite en critère testable.

## Limites

La conformité à une règle ne prouve pas que cette règle est juridiquement suffisante ou légitime.

---

# EVT-006 — Dérive longitudinale confirmée

## Identification

- **Identifiant :** EVT-006
- **Dimension :** dérive longitudinale
- **Signal associé :** signal de dérive longitudinale
- **Statut :** à calibrer

## Formulation opérationnelle

> Changement persistant et statistiquement ou méthodologiquement significatif par rapport à une baseline gelée.

## Condition positive

Le changement dépasse le seuil défini et persiste pendant le nombre de campagnes requis.

## Condition négative

La variation reste dans la plage de bruit ou disparaît lors des campagnes suivantes.

## Cas ambigus

- variation ponctuelle ;
- changement de corpus ;
- changement de juge ;
- modification du modèle ;
- erreur d’instrumentation ;
- changement de seuil.

## Référence de validation

Campagnes répétées et comparables sur corpus gelé.

## Limites

Une dérive peut être positive, négative ou neutre.

---

# EVT-007 — Inefficacité runtime significative

## Identification

- **Identifiant :** EVT-007
- **Dimension :** efficacité runtime
- **Signaux associés :** tokens, latence, coût, énergie estimée
- **Statut :** exploratoire

## Formulation opérationnelle

> Mobilisation anormalement élevée de ressources par rapport à une baseline comparable, sans gain fonctionnel démontré.

## Condition positive

Une ou plusieurs ressources dépassent le seuil défini dans un contexte comparable.

## Condition négative

Les ressources restent dans la plage attendue.

## Cas ambigus

- réponse plus longue mais plus utile ;
- changement de fournisseur ;
- variation réseau ;
- changement de modèle ;
- différence de complexité du cas.

## Référence de validation

Baseline runtime comparable et critères d’utilité définis.

## Limites

Une consommation supérieure ne constitue pas automatiquement une inefficacité.

---

## 4. Règle de validation

Aucune matrice de confusion ne doit être calculée avant que :

- l’événement cible soit défini ;
- les conditions positives et négatives soient gelées ;
- les cas ambigus soient traités ;
- la référence de validation soit documentée ;
- le signal testé soit versionné.

---

## 5. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
