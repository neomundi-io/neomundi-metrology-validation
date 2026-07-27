# Protocole de mesure des faux positifs et faux négatifs NeoMundi

## 1. Objet

Ce document définit la manière dont NeoMundi mesure les vrais positifs, faux positifs, vrais négatifs et faux négatifs pour un signal donné.

L’objectif est d’évaluer la capacité réelle d’un signal à détecter un événement cible clairement défini.

---

## 2. Condition préalable

Aucune matrice de confusion ne doit être calculée tant que les éléments suivants ne sont pas figés :

- l’événement cible ;
- la référence de validation ;
- le signal testé ;
- le seuil appliqué ;
- le corpus utilisé ;
- les règles d’annotation ;
- les règles d’exclusion ;
- la version du protocole.

---

## 3. Définitions

### Vrai positif — VP

L’événement cible est présent et le signal NeoMundi déclenche une alerte.

### Faux positif — FP

L’événement cible est absent, mais le signal NeoMundi déclenche une alerte.

### Vrai négatif — VN

L’événement cible est absent et le signal NeoMundi ne déclenche pas d’alerte.

### Faux négatif — FN

L’événement cible est présent, mais le signal NeoMundi ne déclenche pas d’alerte.

---

## 4. Matrice de confusion

| Réalité de référence | Signal positif | Signal négatif |
|---|---:|---:|
| Événement présent | Vrai positif | Faux négatif |
| Événement absent | Faux positif | Vrai négatif |

Les cas `AMBIGUOUS`, `NOT_APPLICABLE` et `REVIEW_REQUIRED` ne doivent pas être intégrés automatiquement dans la matrice.

---

## 5. Unité d’analyse

L’unité d’analyse doit être définie avant le test.

Elle peut correspondre à :

- une observation ;
- une réponse ;
- un cas ;
- un groupe de répétitions ;
- une trajectoire longitudinale ;
- une règle appliquée ;
- un événement de gouvernance.

Les résultats ne doivent pas mélanger plusieurs unités d’analyse.

---

## 6. Signal positif et signal négatif

Pour chaque expérience, il faut définir explicitement :

### Signal positif

Condition selon laquelle NeoMundi considère que l’événement cible est détecté.

Exemple :

> Le score dépasse ou atteint le seuil versionné.

### Signal négatif

Condition selon laquelle NeoMundi considère que l’événement cible n’est pas détecté.

Exemple :

> Le score reste sous le seuil versionné.

Les valeurs manquantes ou les échecs de calcul doivent être traités séparément.

---

## 7. Jeux de données

Le protocole doit distinguer :

### Jeu de calibration

Utilisé pour explorer et ajuster les seuils.

### Jeu de validation

Utilisé pour sélectionner ou confirmer les choix méthodologiques.

### Jeu de test final

Utilisé une seule fois pour produire l’estimation finale de performance.

Le jeu de test final ne doit pas servir à ajuster les seuils.

---

## 8. Taille des échantillons

### Smoke test méthodologique

- 10 cas positifs ;
- 10 cas négatifs.

Objectif : vérifier que le pipeline fonctionne.

Ce niveau ne constitue pas une validation statistique.

### Première estimation expérimentale

- environ 100 cas positifs ;
- environ 100 cas négatifs.

Objectif : construire une première matrice de confusion et identifier les principales erreurs.

### Validation consolidée

- 300 à 500 cas positifs ;
- 300 à 500 cas négatifs ;
- plusieurs modèles ;
- plusieurs familles de cas ;
- plusieurs campagnes.

Pour soutenir une affirmation forte, un corpus plus large et diversifié peut être nécessaire.

---

## 9. Métriques principales

### Précision

Part des alertes NeoMundi correspondant réellement à un événement positif.

> Précision = VP / (VP + FP)

### Rappel ou sensibilité

Part des événements positifs réellement détectés.

> Rappel = VP / (VP + FN)

### Spécificité

Part des événements négatifs correctement laissés sans alerte.

> Spécificité = VN / (VN + FP)

### Taux de faux positifs

> Taux de faux positifs = FP / (FP + VN)

### Taux de faux négatifs

> Taux de faux négatifs = FN / (FN + VP)

### Score F1

Moyenne harmonique entre précision et rappel.

> F1 = 2 × (précision × rappel) / (précision + rappel)

### Exactitude globale

> Exactitude = (VP + VN) / (VP + FP + VN + FN)

L’exactitude globale ne doit pas être utilisée seule lorsque les classes sont déséquilibrées.

---

## 10. Intervalles d’incertitude

Les résultats doivent être accompagnés, lorsque pertinent, d’un intervalle de confiance ou d’une estimation d’incertitude.

Un taux observé sur un petit échantillon ne doit pas être présenté comme une performance stable ou universelle.

L’absence d’erreur observée ne signifie pas que le taux réel d’erreur est nul.

---

## 11. Classes déséquilibrées

Lorsque les événements positifs sont rares, il faut documenter :

- la prévalence réelle ;
- la prévalence du corpus de test ;
- la méthode d’échantillonnage ;
- l’impact sur la précision ;
- l’impact sur l’interprétation des résultats.

Un corpus équilibré est utile pour comparer les méthodes, mais il ne représente pas automatiquement la fréquence réelle des événements en production.

---

## 12. Comparaison entre méthodes

La même vérité terrain et le même jeu de test doivent être utilisés pour comparer :

- une baseline simple ;
- plusieurs baselines séparées ;
- une combinaison classique ;
- NeoMundi seul ;
- baseline plus NeoMundi.

Les seuils de chaque méthode doivent être calibrés selon une procédure équitable et documentée.

---

## 13. Analyse qualitative des erreurs

Chaque faux positif et faux négatif doit recevoir une qualification.

Catégories recommandées :

- mauvais seuil ;
- événement cible mal défini ;
- ambiguïté du corpus ;
- erreur de référence ;
- erreur d’annotation ;
- faiblesse du signal ;
- contexte manquant ;
- variation normale ;
- donnée incomplète ;
- problème d’instrumentation ;
- défaut non observable ;
- changement de modèle ou de juge.

---

## 14. Journal des erreurs

Chaque erreur analysée doit contenir :

- identifiant du cas ;
- type d’erreur ;
- événement cible ;
- vérité terrain ;
- sortie du signal ;
- seuil appliqué ;
- score éventuel ;
- cause probable ;
- niveau de confiance ;
- décision méthodologique ;
- action corrective éventuelle ;
- version concernée.

---

## 15. Ajustement des seuils

Les seuils peuvent être ajustés uniquement sur le jeu de calibration ou selon une procédure de validation prévue.

Toute modification doit être :

- justifiée ;
- versionnée ;
- datée ;
- reliée aux données utilisées ;
- inscrite dans le journal des décisions méthodologiques.

Un seuil ne doit jamais être modifié sur le jeu de test final pour améliorer artificiellement la performance.

---

## 16. Critères de réussite

Chaque expérience doit définir ses critères de réussite avant l’exécution.

Exemples :

- rappel minimal ;
- taux maximal de faux positifs ;
- amélioration par rapport à une baseline ;
- robustesse entre plusieurs modèles ;
- stabilité entre plusieurs campagnes ;
- délai de détection inférieur à la baseline.

Les critères dépendent de l’usage et du niveau de risque.

---

## 17. Résultats non concluants

Une expérience peut être classée :

- concluante ;
- partiellement concluante ;
- non concluante ;
- invalide méthodologiquement.

Un résultat non concluant ne doit pas être transformé en résultat positif par interprétation.

---

## 18. Formulations autorisées

Exemple de formulation acceptable :

> Sur le corpus de test versionné, le signal a détecté X % des événements cibles, avec Y % de faux positifs.

Exemples de formulations interdites sans validation supplémentaire :

> NeoMundi détecte toutes les erreurs.

> NeoMundi garantit l’absence de risque.

> NeoMundi prouve qu’une réponse est correcte.

---

## 19. Limites

La performance mesurée dépend notamment :

- du corpus ;
- de l’événement cible ;
- de la qualité des labels ;
- du seuil ;
- du modèle ;
- de la langue ;
- du domaine ;
- de la prévalence ;
- de la version du signal.

Une performance locale ne doit pas être généralisée sans réplication.

---

## 20. Statut du document

- Version : v0.1
- Statut : brouillon méthodologique
- Responsable de décision : Sébastien
- Date de création : 27 juillet 2026
