# Dictionnaire des métriques NeoMundi

## Objet

Ce document définit les métriques officielles NeoMundi, leur signification, leur état d’avancement, leurs limites d’interprétation et les validations nécessaires.

Une métrique ne doit pas être présentée comme validée tant que sa définition, son implémentation, sa calibration et son protocole de validation ne sont pas documentés.

---

## Statuts méthodologiques

- **Exploratoire** : concept ou signal en cours d’étude
- **Défini** : objectif et interprétation documentés
- **Implémenté** : calcul présent dans le pipeline NeoMundi
- **Testé** : calcul vérifié sur des cas contrôlés
- **Calibré** : seuils ou plages d’interprétation estimés
- **Validé** : performance mesurée contre une référence documentée
- **Répliqué** : résultat reproduit sur une autre campagne ou dans un autre environnement

---

## Fiche standard d’une métrique

Chaque métrique doit contenir :

- identifiant ;
- nom officiel ;
- version ;
- statut actuel ;
- objectif de mesure ;
- phénomène cible ;
- données d’entrée ;
- formule ou algorithme ;
- type de sortie ;
- unité ou échelle ;
- plage attendue ;
- interprétation ;
- seuils ;
- comportement en cas de données manquantes ;
- dépendances ;
- facteurs de sensibilité ;
- limites connues ;
- non-claims ;
- exemple numérique ;
- référence de validation ;
- test de validation requis ;
- emplacement de l’implémentation ;
- emplacement des preuves ;
- responsable de décision ;
- date de dernière revue.

---

# MET-001 — Score de stabilité

## Identification

- **Identifiant :** MET-001
- **Nom officiel :** Score de stabilité
- **Version :** à figer
- **Statut actuel :** implémenté — définition méthodologique à consolider

## Définition

- **Objectif :** mesurer les variations entre plusieurs exécutions d’un même cas.
- **Phénomène cible :** stabilité des réponses dans un protocole d’exécutions répétées.
- **Entrées :** à documenter depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code existant.
- **Type de sortie :** score numérique.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** à définir formellement.
- **Seuils :** non encore figés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** protocole de répétition, représentation sémantique et méthode d’agrégation.
- **Sensibilité :** modèle, prompt, paramètres, modèle d’embedding, nombre de répétitions et longueur des réponses.

## Limites

- La stabilité ne garantit pas la vérité.
- La stabilité ne garantit pas la conformité.
- Une réponse variable peut rester correcte.
- Une réponse stable peut rester systématiquement fausse.

## Validation

- **Référence :** corpus de réponses répétées revu humainement.
- **Test requis :** analyse intra-prompt et comparaison avec une baseline de similarité sémantique.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-002 — Taux de variation sémantique

## Identification

- **Identifiant :** MET-002
- **Nom officiel :** Taux de variation sémantique
- **Version :** à figer
- **Statut actuel :** implémenté — définition méthodologique à consolider

## Définition

- **Objectif :** identifier une divergence sémantique significative entre plusieurs réponses.
- **Phénomène cible :** variation du sens entre plusieurs exécutions d’un même cas.
- **Entrées :** à documenter depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code existant.
- **Type de sortie :** taux numérique ou classification.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** à définir formellement.
- **Seuils :** non encore figés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** modèle d’embedding, méthode de similarité, clustering ou seuil.
- **Sensibilité :** longueur, langue, paraphrase et version du modèle d’embedding.

## Limites

- Une variation sémantique ne constitue pas automatiquement une erreur.
- Une variation lexicale peut exister sans variation réelle du sens.
- Une formulation proche peut masquer un désaccord factuel ou logique.

## Validation

- **Référence :** corpus de variations sémantiques labellisé humainement.
- **Test requis :** matrice de confusion contre les labels humains.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-003 — Signal de risque factuel

## Identification

- **Identifiant :** MET-003
- **Nom officiel :** Signal de risque factuel
- **Version :** à figer
- **Statut actuel :** exploratoire ou implémenté — à confirmer

## Définition

- **Objectif :** produire un signal associé à une erreur factuelle potentiellement significative.
- **Phénomène cible :** événement factuel défini contre une référence objective ou experte.
- **Entrées :** à documenter.
- **Formule ou algorithme :** à documenter.
- **Type de sortie :** signal, score ou classification.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** signal de risque nécessitant une validation contextuelle.
- **Seuils :** non encore validés.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** source de référence, configuration du juge et méthode de classification.
- **Sensibilité :** domaine, langue, qualité de la source, modèle juge et formulation du prompt.

## Limites

- Un signal de risque factuel ne prouve pas qu’une réponse est fausse.
- L’absence d’alerte ne prouve pas qu’une réponse est vraie.
- La performance peut varier selon les domaines et les types de références.

## Validation

- **Référence :** vérité terrain objective ou revue experte indépendante.
- **Test requis :** contrôles positifs et négatifs avec matrice de confusion.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-004 — Signal de dérive longitudinale

## Identification

- **Identifiant :** MET-004
- **Nom officiel :** Signal de dérive longitudinale
- **Version :** à figer
- **Statut actuel :** mesuré — validation à réaliser

## Définition

- **Objectif :** détecter un changement durable par rapport à une baseline gelée.
- **Phénomène cible :** évolution longitudinale entre plusieurs campagnes comparables.
- **Entrées :** à documenter.
- **Formule ou algorithme :** à documenter.
- **Type de sortie :** signal ou score.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** changement mesuré par rapport à une baseline et à un protocole définis.
- **Seuils :** à calibrer.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** stabilité du corpus, versionnage et comparabilité des campagnes.
- **Sensibilité :** changement de modèle, fournisseur, juge, corpus ou méthode d’échantillonnage.

## Limites

- Un changement ne représente pas automatiquement une dégradation.
- Une variation ponctuelle ne constitue pas nécessairement une dérive.
- La détection d’une dérive ne permet pas automatiquement de prédire une défaillance future.

## Validation

- **Référence :** campagnes répétées sur corpus fixe.
- **Test requis :** comparaison longitudinale sur plusieurs campagnes.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

# MET-005 — Delta G

## Identification

- **Identifiant :** MET-005
- **Nom officiel :** Delta G
- **Version :** à figer
- **Statut actuel :** exploratoire ou implémenté — statut exact à confirmer

## Définition

- **Objectif :** à spécifier formellement.
- **Phénomène cible :** à spécifier formellement.
- **Entrées :** à extraire depuis l’implémentation actuelle.
- **Formule ou algorithme :** à extraire et à figer depuis le code.
- **Type de sortie :** valeur numérique.
- **Unité ou échelle :** à confirmer.
- **Plage attendue :** à confirmer.

## Interprétation

- **Interprétation :** non encore figée.
- **Seuils :** non encore validés méthodologiquement.
- **Données manquantes :** comportement à documenter.
- **Dépendances :** à documenter.
- **Sensibilité :** prompt, modèle, longueur, tokenisation et configuration runtime.

## Limites

- Une valeur élevée de Delta G ne doit pas être interprétée automatiquement comme une erreur.
- La métrique ne doit pas être présentée comme une preuve thermodynamique sans validation séparée.
- Aucun seuil universel ne doit être revendiqué avant calibration multi-contextes.

## Validation

- **Référence :** à définir.
- **Test requis :** sensibilité, ablation, perturbations contrôlées et comparaison à des baselines.
- **Implémentation :** à renseigner.
- **Preuves :** à renseigner.
- **Responsable :** Sébastien.
- **Dernière revue :** 27 juillet 2026.

---

## Métriques à ajouter

Les métriques suivantes devront être ajoutées après extraction depuis le pipeline actuel :

- cohérence ;
- conformité ;
- Runtime R ;
- densité informationnelle ;
- énergie ;
- latence ;
- coût ;
- classification des régimes ;
- métriques de trajectoire ;
- métriques candidates Oracle Law E.
