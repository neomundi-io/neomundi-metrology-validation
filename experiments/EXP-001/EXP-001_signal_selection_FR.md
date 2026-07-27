# EXP-001 — Sélection du premier signal à valider

## 1. Décision

Le premier signal sélectionné pour l’expérience EXP-001 est :

> Signal de risque factuel NeoMundi

---

## 2. Identifiants associés

- **Claim :** CLM-003
- **Métrique ou signal :** MET-003
- **Événement cible :** EVT-003
- **Dimension principale :** factualité

---

## 3. Question de recherche

> Le signal de risque factuel NeoMundi permet-il de détecter une erreur factuelle significative avec une performance supérieure ou complémentaire à une baseline simple de factualité ?

---

## 4. Événement cible

L’événement cible est :

> La présence dans une réponse d’une affirmation factuelle incorrecte susceptible de modifier significativement la compréhension, la décision ou l’usage.

---

## 5. Pourquoi ce signal est prioritaire

Ce signal est retenu en premier car :

- la factualité peut souvent être comparée à une référence objective ;
- les contrôles positifs et négatifs peuvent être construits clairement ;
- les faux positifs et faux négatifs peuvent être définis sans ambiguïté excessive ;
- une baseline simple peut être mise en place ;
- le résultat sera facilement compréhensible par un tiers ;
- la validation répond directement aux audits méthodologiques reçus.

---

## 6. Baseline initiale envisagée

La baseline devra être simple et indépendante de la combinaison NeoMundi.

Candidats :

- juge de factualité unique ;
- comparaison à une réponse de référence ;
- règle déterministe sur les cas fermés ;
- score de factualité sans signaux NeoMundi additionnels.

La baseline exacte devra être choisie et versionnée avant l’exécution.

---

## 7. Unité d’analyse envisagée

L’unité d’analyse retenue provisoirement est :

> une réponse individuelle comparée à une référence de validation.

Cette unité devra être confirmée avant le gel du protocole.

---

## 8. Corpus initial envisagé

Première estimation expérimentale :

- 100 cas positifs ;
- 100 cas négatifs ;
- cas ambigus séparés ;
- mélange de cas naturels et de défauts contrôlés ;
- plusieurs familles factuelles ;
- plusieurs modèles ou profils lorsque possible.

---

## 9. Résultats attendus

L’expérience devra produire :

- une matrice de confusion ;
- la précision ;
- le rappel ;
- la spécificité ;
- le taux de faux positifs ;
- le taux de faux négatifs ;
- le score F1 ;
- une comparaison avec la baseline ;
- une analyse qualitative des erreurs.

---

## 10. Limites

Cette expérience ne permettra pas de conclure que NeoMundi détecte toutes les erreurs factuelles.

Elle mesurera une performance locale :

- sur un corpus défini ;
- avec une référence définie ;
- avec une version précise du signal ;
- dans un protocole gelé.

---

## 11. Décision méthodologique

- **Signal retenu :** risque factuel
- **Statut :** APPROVED FOR PROTOCOL DESIGN
- **Exécution autorisée :** non
- **Prochaine étape :** définir précisément la baseline de factualité
- **Responsable :** Sébastien
- **Date :** 27 juillet 2026
