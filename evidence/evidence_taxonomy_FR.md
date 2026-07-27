# Taxonomie des preuves NeoMundi

## 1. Objet

Ce document définit les différents niveaux de preuve produits ou supportés par NeoMundi.

L’objectif est d’éviter de confondre :

- une donnée capturée ;
- un calcul reproduit ;
- une règle appliquée ;
- une décision de gouvernance ;
- une action réellement exécutée ;
- une preuve de vérité ou de conformité.

---

## 2. Principe général

NeoMundi produit des artefacts traçables relatifs à l’observation, au calcul et à la gouvernance.

Ces artefacts ne prouvent pas automatiquement :

- que la réponse est vraie ;
- que la décision prise est correcte ;
- que la règle appliquée est légitime ;
- que l’organisation est juridiquement conforme ;
- que le système est sûr.

Chaque artefact doit indiquer explicitement le niveau de preuve qu’il supporte.

---

# Niveau 1 — Preuve de capture

## Définition

La preuve de capture atteste qu’une interaction ou un événement a été enregistré.

Elle peut documenter :

- une requête ;
- une réponse ;
- un horodatage ;
- un identifiant ;
- un modèle ou profil ;
- des paramètres ;
- des données runtime ;
- un statut d’exécution.

## Ce qu’elle prouve

Elle prouve qu’un ensemble de données a été capturé dans un contexte déclaré.

## Ce qu’elle ne prouve pas

Elle ne prouve pas :

- que les données sont correctes ;
- que la réponse est vraie ;
- que la capture est complète ;
- que le système a respecté une règle.

## Nom anglais recommandé

`Proof of Capture`

---

# Niveau 2 — Preuve de calcul

## Définition

La preuve de calcul atteste qu’une métrique ou un algorithme versionné a été appliqué à des données identifiées.

Elle doit pouvoir documenter :

- les données d’entrée ;
- la formule ou l’algorithme ;
- la version de la métrique ;
- les paramètres ;
- le résultat ;
- les dépendances ;
- les éventuelles données manquantes.

## Ce qu’elle prouve

Elle prouve qu’un calcul déclaré a été exécuté sur des données identifiées.

## Ce qu’elle ne prouve pas

Elle ne prouve pas :

- que la métrique est scientifiquement valide ;
- que son interprétation est correcte ;
- que le résultat représente la vérité ;
- que le seuil appliqué est pertinent.

## Nom anglais recommandé

`Proof of Computation`

---

# Niveau 3 — Preuve d’application d’une règle

## Définition

La preuve d’application d’une règle atteste qu’une règle versionnée a été évaluée sur un signal ou un ensemble de données.

Elle peut documenter :

- l’identifiant de la règle ;
- la version ;
- les conditions d’entrée ;
- le signal évalué ;
- le seuil ;
- le résultat de la règle ;
- les exceptions ;
- le statut d’autorisation.

## Ce qu’elle prouve

Elle prouve qu’une règle déclarée a été appliquée selon une logique enregistrée.

## Ce qu’elle ne prouve pas

Elle ne prouve pas :

- que la règle est juste ;
- que la règle est légalement suffisante ;
- que la décision résultante est appropriée ;
- que le signal utilisé était correct.

## Nom anglais recommandé

`Proof of Rule Application`

---

# Niveau 4 — Preuve de parcours de gouvernance

## Définition

La preuve de parcours de gouvernance documente la chaîne complète ayant conduit d’une observation à une décision.

Chaîne type :

> observation → mesure → interprétation → règle → décision

Elle peut inclure :

- identifiants de trace ;
- signaux ;
- règles ;
- décisions ;
- interventions humaines ;
- exceptions ;
- validations ;
- reçus de gouvernance.

## Ce qu’elle prouve

Elle prouve qu’un processus de gouvernance déclaré a été suivi et tracé.

## Ce qu’elle ne prouve pas

Elle ne prouve pas :

- que la décision était correcte ;
- que toutes les règles nécessaires ont été appliquées ;
- que l’organisation est conforme ;
- que le résultat opérationnel a été exécuté.

## Nom anglais recommandé

`Proof of Governance Pathway`

---

# Niveau 5 — Preuve d’exécution d’une action

## Définition

La preuve d’exécution atteste qu’une action décidée a réellement été exécutée.

Exemples :

- blocage d’une requête ;
- redirection ;
- demande de revue humaine ;
- suspension d’un workflow ;
- modification d’une autorisation ;
- émission d’une alerte ;
- journalisation renforcée.

## Ce qu’elle prouve

Elle prouve qu’une action identifiable a été exécutée ou tentée.

## Ce qu’elle ne prouve pas

Elle ne prouve pas :

- que l’action était la bonne ;
- qu’elle a produit l’effet attendu ;
- qu’elle a évité un dommage ;
- qu’elle respecte toutes les obligations applicables.

## Nom anglais recommandé

`Proof of Execution`

---

# Niveau 6 — Preuve de résultat

## Définition

La preuve de résultat documente l’effet observable produit après une action.

Exemples :

- requête effectivement bloquée ;
- risque réduit ;
- anomalie corrigée ;
- workflow restauré ;
- décision humaine obtenue ;
- changement de comportement constaté.

## Ce qu’elle prouve

Elle prouve qu’un résultat observable a été enregistré après une action.

## Ce qu’elle ne prouve pas

Elle ne prouve pas automatiquement :

- que le résultat est durable ;
- que l’action est la cause unique ;
- que la décision était optimale ;
- qu’aucun autre risque ne subsiste.

## Nom anglais recommandé

`Proof of Outcome`

---

## 3. Chaîne de preuve complète

La chaîne complète peut être représentée ainsi :

> capture → calcul → règle → gouvernance → exécution → résultat

Chaque niveau doit pouvoir être relié au précédent par :

- un identifiant stable ;
- un identifiant de trace ;
- une version ;
- un horodatage ;
- un hash ;
- un journal de décision ;
- une référence à l’artefact associé.

---

## 4. Statuts de preuve

Les statuts recommandés sont :

- `NOT_AVAILABLE`
- `PARTIAL`
- `AVAILABLE`
- `VERIFIED`
- `REPRODUCED`
- `DISPUTED`
- `INVALIDATED`

Le statut doit être attribué séparément à chaque niveau de preuve.

---

## 5. Preuve et validation

Une preuve traçable n’est pas automatiquement une preuve de validité.

Il faut distinguer :

### Traçabilité

Capacité à suivre ce qui a été capturé, calculé, décidé et exécuté.

### Reproductibilité

Capacité à recalculer ou rejouer le processus.

### Validation

Capacité à démontrer que la méthode mesure correctement l’événement cible.

### Conformité

Évaluation du respect d’un cadre juridique, normatif ou contractuel.

Ces quatre notions ne doivent pas être confondues.

---

## 6. Formulation publique autorisée

Formulation recommandée :

> NeoMundi produit des preuves traçables et reproductibles d’observation, de calcul et d’exécution de la gouvernance.

Formulation prudente :

> Le niveau de preuve dépend des données capturées, des règles appliquées et des artefacts disponibles.

---

## 7. Formulations interdites sans validation supplémentaire

Ne pas affirmer :

> NeoMundi prouve qu’une réponse est vraie.

> NeoMundi prouve automatiquement la conformité juridique.

> NeoMundi garantit que la décision était correcte.

> NeoMundi garantit l’absence de risque.

> Un reçu de gouvernance constitue à lui seul une preuve complète de conformité.

---

## 8. Métadonnées minimales d’un artefact de preuve

Chaque artefact doit contenir :

- identifiant de preuve ;
- niveau de preuve ;
- identifiant d’observation ;
- identifiant de trace ;
- date ;
- source ;
- version ;
- hash ;
- statut ;
- artefact précédent ;
- artefact suivant éventuel ;
- responsable ;
- limites ;
- emplacement de stockage.

---

## 9. Limites

Une chaîne de preuve peut être complète mais reposer sur :

- une mauvaise métrique ;
- une mauvaise règle ;
- une mauvaise référence ;
- une décision humaine incorrecte ;
- des données incomplètes.

La qualité d’une preuve dépend à la fois de sa traçabilité et de la validité des éléments qu’elle relie.

---

## 10. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
