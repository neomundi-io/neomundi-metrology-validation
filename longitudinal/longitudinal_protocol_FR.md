# Protocole longitudinal NeoMundi

## 1. Objet

Ce document définit la manière dont NeoMundi mesure, compare et interprète les évolutions d’un système d’intelligence artificielle dans le temps.

L’objectif est de distinguer une variation ponctuelle, un bruit normal, une rupture, une tendance durable et une dérive confirmée.

---

## 2. Principe général

Une évolution longitudinale ne peut être interprétée que si les campagnes comparées sont suffisamment comparables.

La comparaison doit reposer sur :

- une baseline identifiée ;
- un corpus fixe ou explicitement versionné ;
- des métriques versionnées ;
- des conditions d’exécution documentées ;
- un nombre de répétitions défini ;
- des règles de confirmation établies avant l’analyse.

---

## 3. Unité d’analyse

L’unité longitudinale peut être :

- une observation ;
- un cas répété ;
- un prompt ;
- un profil ou modèle ;
- une famille de risque ;
- une métrique ;
- une campagne ;
- une trajectoire complète.

L’unité utilisée doit être précisée dans chaque étude.

---

## 4. Baseline longitudinale

La baseline constitue le point de référence initial.

Elle doit contenir :

- l’identifiant de la campagne ;
- la période ;
- le corpus ;
- les modèles ou profils ;
- les paramètres ;
- les répétitions ;
- les métriques ;
- les seuils ;
- les juges ;
- les exclusions ;
- les versions ;
- les limites connues.

Une baseline ne doit pas être modifiée rétroactivement sans création d’une nouvelle version.

---

## 5. Corpus fixe et corpus renouvelé

### Corpus fixe

Ensemble de cas conservé entre les campagnes.

Objectif :

- mesurer les changements sur une base comparable ;
- détecter une rupture ;
- suivre une trajectoire ;
- réduire l’effet du changement de corpus.

### Corpus renouvelé

Ensemble de cas ajouté ou remplacé au fil du temps.

Objectif :

- maintenir la représentativité ;
- introduire de nouveaux usages ;
- éviter un protocole trop figé ;
- étudier la généralisation.

Les résultats du corpus fixe et du corpus renouvelé doivent être distingués.

---

## 6. Fréquence des campagnes

La fréquence doit être définie selon l’objectif.

Exemples :

- contrôle hebdomadaire ;
- cartographie mensuelle ;
- revalidation trimestrielle ;
- campagne déclenchée par un changement majeur ;
- étude ponctuelle renforcée.

Une fréquence élevée augmente la sensibilité aux fluctuations ponctuelles et ne garantit pas une meilleure interprétation.

---

## 7. Nombre de répétitions

Le nombre de répétitions doit être défini avant l’exécution.

Il doit permettre d’étudier :

- la variabilité intra-cas ;
- la stabilité des conclusions ;
- les distributions ;
- les réponses rares ;
- les changements de régime.

Une modification du nombre de répétitions doit être explicitement documentée avant toute comparaison.

---

## 8. Catégories d’évolution

### Bruit

Variation limitée, attendue et compatible avec le fonctionnement normal du système ou de la mesure.

### Variation ponctuelle

Changement observé sur une campagne unique sans confirmation ultérieure.

### Rupture

Changement important apparaissant entre deux campagnes comparables.

### Tendance

Évolution progressive observée sur plusieurs campagnes successives.

### Plateau

Maintien d’un niveau relativement stable après une évolution.

### Récupération ou retour à la normale

Retour vers la baseline ou vers une plage considérée comme normale après une déviation.

### Dérive confirmée

Changement persistant dépassant les critères de confirmation définis.

---

## 9. Conditions de confirmation d’une dérive

Une dérive ne doit être déclarée que si les conditions prévues sont satisfaites.

Ces conditions peuvent inclure :

- dépassement d’un seuil ;
- persistance sur plusieurs campagnes ;
- présence sur plusieurs répétitions ;
- cohérence entre plusieurs métriques ;
- absence d’explication technique ;
- reproductibilité du signal ;
- confirmation par une revue humaine.

Les critères exacts doivent être définis pour chaque métrique.

---

## 10. Causes alternatives à examiner

Avant de conclure à une dérive du système, vérifier :

- changement de modèle ;
- mise à jour du fournisseur ;
- modification des paramètres ;
- changement du corpus ;
- changement de prompt ;
- changement de juge ;
- changement de seuil ;
- changement du modèle d’embedding ;
- erreur d’instrumentation ;
- données manquantes ;
- différence de volume ;
- incident réseau ou infrastructure ;
- modification du pipeline.

Une dérive apparente peut provenir de l’instrument ou du protocole.

---

## 11. Comparabilité des campagnes

Deux campagnes sont directement comparables lorsque les éléments essentiels sont identiques ou suffisamment contrôlés.

Doivent être comparés :

- corpus ;
- prompts ;
- modèles ;
- paramètres ;
- répétitions ;
- langues ;
- métriques ;
- juges ;
- seuils ;
- versions du pipeline ;
- règles d’exclusion ;
- période d’exécution.

Toute différence doit être documentée.

---

## 12. Analyse intra-prompt

Chaque groupe de répétitions doit pouvoir être analysé séparément.

L’analyse peut examiner :

- réponses identiques ;
- conclusions identiques ;
- conclusions divergentes ;
- clusters sémantiques ;
- contradictions ;
- variations factuelles ;
- dispersion des scores ;
- cas rares ;
- transitions entre régimes.

Les moyennes globales ne doivent pas remplacer l’analyse au niveau des cas.

---

## 13. Analyse des distributions

Pour chaque métrique longitudinale, il faut examiner lorsque pertinent :

- moyenne ;
- médiane ;
- dispersion ;
- quantiles validés ;
- valeurs extrêmes ;
- distribution complète ;
- asymétrie ;
- sous-groupes ;
- évolution des régimes.

Une moyenne stable peut masquer une modification importante de la distribution.

---

## 14. Analyse par sous-groupes

Les évolutions doivent être examinées selon :

- modèle ou profil ;
- cas ;
- prompt ;
- famille de risque ;
- langue ;
- type de vérité terrain ;
- longueur de réponse ;
- classe de signal ;
- statut de complétude.

Un changement global peut provenir d’un sous-groupe limité.

---

## 15. Seuils longitudinaux

Chaque seuil doit préciser :

- la métrique concernée ;
- la baseline ;
- la méthode de calcul ;
- la plage normale ;
- le niveau d’alerte ;
- le nombre de confirmations requis ;
- les conditions d’annulation ;
- la version ;
- le responsable de décision.

Les seuils exploratoires doivent être distingués des seuils calibrés ou validés.

---

## 16. Contrôle qualité hebdomadaire

Chaque baromètre peut inclure un petit ensemble fixe comprenant :

- contrôles positifs ;
- contrôles négatifs ;
- cas limites ;
- tests de complétude ;
- vérification des juges ;
- contrôle des versions ;
- contrôle des calculs.

Ce contrôle vise à détecter une régression méthodologique ou technique.

Il ne constitue pas une nouvelle validation complète de l’instrument.

---

## 17. Déclencheurs d’investigation

Une investigation peut être déclenchée lorsqu’apparaît :

- une hausse ou baisse importante ;
- une rupture entre deux campagnes ;
- une persistance inhabituelle ;
- une divergence entre métriques ;
- une modification de la distribution ;
- une multiplication des cas incomplets ;
- un changement de comportement d’un juge ;
- un changement localisé sur une famille de cas.

Le déclenchement d’une investigation ne constitue pas un verdict.

---

## 18. Déclencheurs de revalidation

Une revalidation méthodologique doit être envisagée lorsque :

- une métrique change ;
- une formule change ;
- un seuil change ;
- un juge change ;
- une nouvelle langue est introduite ;
- une nouvelle famille de risque est ajoutée ;
- le corpus change substantiellement ;
- l’architecture du pipeline change ;
- une anomalie majeure est observée ;
- une version majeure de NeoMundi est publiée.

---

## 19. Registre longitudinal minimal

Chaque résultat longitudinal doit contenir :

- identifiant de trajectoire ;
- baseline ;
- campagnes comparées ;
- métrique ;
- valeurs observées ;
- incertitude ;
- seuils ;
- statut ;
- causes alternatives examinées ;
- interprétation ;
- limites ;
- décision ;
- date ;
- version méthodologique.

---

## 20. Statuts recommandés

- `NORMAL`
- `VARIATION_PONCTUELLE`
- `A_SURVEILLER`
- `RUPTURE_POTENTIELLE`
- `TENDANCE`
- `PLATEAU`
- `RECUPERATION`
- `DERIVE_CONFIRMEE`
- `NON_INTERPRETABLE`

Ces statuts doivent rester des classifications méthodologiques et non des verdicts automatiques sur la qualité du modèle.

---

## 21. Formulations autorisées

Exemple acceptable :

> Une variation a été observée sur cette campagne par rapport à la baseline. Elle nécessite une confirmation sur les campagnes suivantes.

Exemple acceptable après confirmation :

> Un changement persistant a été observé sur plusieurs campagnes comparables selon le protocole versionné.

Formulations interdites sans preuve supplémentaire :

> Le modèle se dégrade définitivement.

> NeoMundi prédit une future défaillance.

> Cette variation prouve que le modèle est dangereux.

---

## 22. Limites

Une observation longitudinale dépend :

- de la stabilité du protocole ;
- de la qualité de la baseline ;
- de la comparabilité des campagnes ;
- du nombre de répétitions ;
- des changements externes ;
- de la qualité de l’instrumentation.

Une dérive détectée n’indique pas automatiquement sa cause, sa gravité ou son impact opérationnel.

---

## 23. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
