# EXP-001 — Protocole d’exécution du smoke test

## 1. Objet

Ce document définit les conditions et la procédure d’exécution du smoke test de 20 cas de l’expérience `EXP-001`.

Ce smoke test ne vise pas à valider scientifiquement la performance du signal de risque factuel NeoMundi.

Il sert à vérifier :

- la cohérence des fichiers d’entrée ;
- la bonne lecture du corpus ;
- le fonctionnement du pipeline d’exécution ;
- la production des sorties attendues ;
- la séparation entre vérité terrain, baseline et signal NeoMundi ;
- la compatibilité entre labels, scores et classifications ;
- le calcul de la matrice de confusion ;
- la traçabilité complète de l’expérience ;
- la reproductibilité technique du traitement.

---

## 2. Périmètre

Le smoke test contient :

- 20 cas synthétiques ;
- 10 cas `POSITIVE` ;
- 10 cas `NEGATIVE` ;
- 10 paires de réponses ;
- un événement cible unique : `EVT-003` ;
- une dimension principale : la factualité ;
- des cas fermés ;
- des réponses courtes ;
- des erreurs factuelles contrôlées ;
- une baseline déterministe indépendante.

Le corpus ne doit pas être utilisé pour soutenir une affirmation scientifique, commerciale ou générale de performance.

Une réussite sur ces 20 cas confirme uniquement que la chaîne expérimentale fonctionne sur un petit corpus synthétique contrôlé.

---

## 3. Fichiers d’entrée

L’exécution doit utiliser au minimum les fichiers suivants :

- `EXP-001_smoke_test_20_cases_FR.csv`
- `EXP-001_factuality_baseline_FR.md`
- `EXP-001_signal_selection_FR.md`
- `EXP-001_control_corpus_specification_FR.md`
- `target_events_registry_FR.md`
- `false_positive_negative_protocol_FR.md`
- `metric_dictionary_FR.md`
- `EXP-001_smoke_test_run_manifest.json`

Le script de validation utilisé avant exécution est :

```text
scripts/validate_exp001_smoke_test.py
```

Le workflow GitHub Actions associé est :

```text
.github/workflows/validate-exp001-smoke-test.yml
```

---

## 4. État actuel du corpus

À la date de la présente revue :

- les 20 cas sont présents ;
- les identifiants sont uniques ;
- les 10 cas positifs sont présents ;
- les 10 cas négatifs sont présents ;
- les valeurs autorisées sont respectées ;
- les injections sont cohérentes ;
- les références sont renseignées ;
- les références sont versionnées ;
- les valeurs provisoires de référence ont été supprimées ;
- la validation `structural` est opérationnelle ;
- la validation `documented` est opérationnelle.

Les éléments suivants ne sont pas encore finalisés :

- revue humaine ;
- attribution des splits ;
- approbation des cas ;
- calcul du hash du corpus ;
- gel du corpus ;
- gel du protocole ;
- enregistrement complet de l’environnement ;
- autorisation d’exécution.

---

## 5. Structure réelle des cas

Le schéma du corpus distingue deux dimensions différentes.

### 5.1 Origine du cas

La colonne :

```text
origin_type
```

indique l’origine générale du cas.

Pour les 20 cas du smoke test, la valeur attendue est :

```text
SYNTHETIC
```

Les 20 cas ont été construits artificiellement pour tester le pipeline.

### 5.2 Présence d’une injection

La colonne :

```text
natural_or_injected
```

indique si une erreur factuelle a été introduite dans la réponse.

Les valeurs utilisées sont :

```text
NOT_INJECTED
INJECTED
```

- `NOT_INJECTED` : réponse correcte synthétique ;
- `INJECTED` : réponse synthétique contenant une erreur factuelle contrôlée.

La valeur `CONTROLLED` ne fait pas partie du schéma actuel.

---

## 6. Validation préalable du corpus

Trois niveaux de validation sont disponibles.

### 6.1 Niveau `structural`

Commande :

```bash
python scripts/validate_exp001_smoke_test.py --stage structural
```

Ce niveau vérifie notamment :

- la présence des 20 cas ;
- la présence de 10 cas `POSITIVE` ;
- la présence de 10 cas `NEGATIVE` ;
- l’unicité des identifiants ;
- la conformité des colonnes ;
- les valeurs autorisées ;
- la cohérence entre `ground_truth_label` et `final_label` ;
- la cohérence des descriptions d’injection ;
- l’origine synthétique des cas ;
- la cohérence des statuts d’inclusion.

### 6.2 Niveau `documented`

Commande :

```bash
python scripts/validate_exp001_smoke_test.py --stage documented
```

Ce niveau exécute également les contrôles structurels et vérifie :

- la présence des références ;
- la présence des versions de référence ;
- l’absence de valeurs provisoires bloquantes ;
- la validité minimale des URL officielles ;
- la structure des références déterministes internes ;
- le versionnage des règles déterministes.

### 6.3 Niveau `frozen`

Commande :

```bash
python scripts/validate_exp001_smoke_test.py --stage frozen
```

Ce niveau doit être exécuté avant toute autorisation expérimentale.

Il vérifie notamment :

- l’attribution d’un split ;
- l’approbation de la revue humaine ;
- la présence du label du premier évaluateur ;
- la présence de son niveau de confiance ;
- la présence de sa justification ;
- la cohérence entre le label de revue et le label final ;
- la gestion des désaccords éventuels ;
- le statut d’arbitrage ;
- le statut `FROZEN` ;
- l’inclusion effective des cas.

L’exécution du smoke test est interdite tant que le niveau `frozen` échoue.

---

## 7. Revue humaine préalable

Chaque cas doit être vérifié avant le gel.

Pour les cas simples et déterministes du smoke test, une revue principale est suffisante lorsque :

- la référence est objective ;
- le fait demandé est non ambigu ;
- la réponse contient une seule affirmation centrale ;
- le label est directement justifiable ;
- aucune expertise spécialisée n’est nécessaire.

Le premier évaluateur doit renseigner :

- `reviewer_1_label`
- `reviewer_1_confidence`
- `reviewer_1_justification`
- `review_status`

Le statut attendu après validation est :

```text
APPROVED
```

Le label du premier évaluateur doit correspondre au champ :

```text
final_label
```

Une seconde revue est requise en cas de doute, d’ambiguïté ou de désaccord.

Les évaluateurs ne doivent pas avoir accès :

- au score NeoMundi ;
- à la classification NeoMundi ;
- aux passages signalés ;
- aux autres métriques NeoMundi.

---

## 8. Attribution des splits

Chaque cas doit être affecté à un split avant gel.

Valeurs autorisées :

```text
CALIBRATION
VALIDATION
FINAL_TEST
```

La valeur suivante n’est pas autorisée dans le corpus gelé :

```text
UNASSIGNED
```

Les deux éléments d’une même paire doivent rester dans le même split afin d’éviter une fuite méthodologique.

Le smoke test ne doit pas être utilisé pour ajuster définitivement le seuil de `MET-003`.

L’attribution des splits sert principalement à vérifier que le pipeline respecte la structure expérimentale prévue.

---

## 9. Signal NeoMundi évalué

Le signal étudié est :

```text
MET-003
```

Nom officiel :

```text
Signal de risque factuel
```

Nom du champ implémenté :

```text
factual_hallucination_score
```

Alias historique :

```text
hallucination_score
```

Emplacement de l’implémentation :

```text
govern-v3/app/core/hallucination_detector.py
```

Fonction principale :

```text
detect_hallucination
```

Le mécanisme repose sur une évaluation de type :

```text
LLM-as-Judge
```

Le score produit est borné dans l’intervalle :

```text
[0,1]
```

Le seuil par défaut de classification est :

```text
0.5
```

La règle par défaut est :

```text
is_hallucinated = factual_hallucination_score >= 0.5
```

Ce seuil est implémenté, mais il n’est pas encore méthodologiquement calibré ni validé.

La valeur `0.3` présente dans le prompt du juge concerne l’extraction de `suspect_phrases` et ne constitue pas le seuil principal de classification.

---

## 10. Entrée du signal NeoMundi

Pour chaque cas, le pipeline doit recevoir au minimum :

- `case_id`
- `prompt`
- `response`
- `target_event_id`
- version de la métrique ;
- version du seuil ;
- version du pipeline ;
- version du modèle juge ;
- configuration du juge ;
- date et heure d’exécution.

Le signal testé ne doit pas recevoir :

- `ground_truth_label`
- `final_label`
- les labels des évaluateurs ;
- la décision de la baseline ;
- la justification de la vérité terrain.

---

## 11. Sortie attendue du signal NeoMundi

Pour chaque cas, NeoMundi doit produire au minimum :

- identifiant du cas ;
- `factual_hallucination_score` ;
- classification booléenne ;
- classification expérimentale normalisée ;
- seuil appliqué ;
- version de la métrique ;
- version du seuil ;
- version du pipeline ;
- modèle juge utilisé ;
- niveau de confiance du juge ;
- justification technique disponible ;
- passages suspects éventuels ;
- latence ;
- statut de calcul ;
- statut de fallback ;
- erreurs éventuelles.

Les valeurs expérimentales minimales attendues sont :

```text
SIGNAL_POSITIVE
SIGNAL_NEGATIVE
SIGNAL_UNAVAILABLE
COMPUTATION_ERROR
```

Correspondance par défaut :

- `is_hallucinated = true` → `SIGNAL_POSITIVE`
- `is_hallucinated = false` → `SIGNAL_NEGATIVE`

Un résultat de fallback ne doit pas être interprété comme une réponse factuellement correcte.

---

## 12. Comportement en cas de données manquantes ou d’indisponibilité

L’implémentation observée peut retourner un score de repli à `0.0` dans plusieurs situations, notamment :

- réponse vide ;
- absence de clé API du juge ;
- indisponibilité du système de détection ;
- activation d’un fallback.

Ces résultats doivent être identifiés séparément.

Ils ne doivent pas être automatiquement convertis en :

```text
SIGNAL_NEGATIVE
```

sans examen du statut technique.

Le fichier de sortie doit donc distinguer :

- score effectivement calculé ;
- résultat de fallback ;
- signal indisponible ;
- erreur de calcul.

---

## 13. Baseline factuelle

La baseline du smoke test est :

> une baseline déterministe indépendante fondée sur une référence documentée et une règle de décision reproductible.

Aucun modèle juge n’est utilisé pour produire la décision principale de baseline sur les 20 cas.

La baseline doit produire :

```text
FACTUALLY_CORRECT
FACTUALLY_INCORRECT
UNDETERMINED
```

Correspondance attendue :

| Vérité terrain | Décision de baseline |
|---|---|
| `NEGATIVE` | `FACTUALLY_CORRECT` |
| `POSITIVE` | `FACTUALLY_INCORRECT` |

La baseline doit être exécutée sans accès aux sorties NeoMundi.

---

## 14. Séparation des trois niveaux

Trois niveaux doivent être conservés distinctement :

1. vérité terrain gelée ;
2. décision de la baseline ;
3. sortie du signal NeoMundi.

Ils ne doivent pas être fusionnés dans un même champ.

La vérité terrain correspond au label final revu et gelé.

La baseline est une méthode indépendante.

NeoMundi est le système testé.

Une configuration combinant baseline et signaux NeoMundi peut être étudiée ultérieurement comme système composite, mais elle ne doit pas être utilisée comme baseline indépendante de `MET-003`.

---

## 15. Construction de la matrice de confusion

Pour NeoMundi :

| Vérité terrain | Signal NeoMundi | Résultat |
|---|---|---|
| `POSITIVE` | `SIGNAL_POSITIVE` | VP |
| `NEGATIVE` | `SIGNAL_POSITIVE` | FP |
| `NEGATIVE` | `SIGNAL_NEGATIVE` | VN |
| `POSITIVE` | `SIGNAL_NEGATIVE` | FN |

Les cas suivants doivent être comptabilisés séparément :

```text
SIGNAL_UNAVAILABLE
COMPUTATION_ERROR
FALLBACK_RESULT
```

Ils ne doivent pas être convertis automatiquement en vrais négatifs.

---

## 16. Calculs attendus

Le script ou le rapport doit calculer :

- nombre total de cas ;
- nombre de cas traités ;
- nombre de VP ;
- nombre de FP ;
- nombre de VN ;
- nombre de FN ;
- nombre d’erreurs de calcul ;
- nombre de signaux indisponibles ;
- nombre de fallbacks ;
- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- score F1 ;
- couverture.

Sur 20 cas, ces mesures servent uniquement à vérifier le pipeline.

Elles ne doivent pas être présentées comme une estimation robuste de performance.

---

## 17. Critères de réussite technique

Le smoke test est techniquement réussi si :

- les 20 cas sont chargés ;
- aucune ligne n’est perdue ;
- aucune colonne n’est décalée ;
- chaque cas reçoit une sortie ou un statut d’erreur explicite ;
- les versions sont enregistrées ;
- le seuil appliqué est enregistré ;
- la matrice de confusion est calculable ;
- les fallbacks sont identifiés ;
- les erreurs de calcul sont explicites ;
- les résultats sont reliés aux identifiants des cas ;
- les résultats peuvent être recalculés ;
- les fichiers produits peuvent être hashés ;
- l’environnement d’exécution est documenté.

La réussite technique ne dépend pas d’un niveau minimal de performance.

---

## 18. Critères d’arrêt

Le smoke test doit être arrêté si :

- le signal accède aux labels ;
- la baseline accède aux sorties NeoMundi ;
- les cas ne sont pas revus ;
- les splits ne sont pas attribués ;
- le corpus n’est pas gelé ;
- le protocole n’est pas gelé ;
- le niveau `frozen` du validateur échoue ;
- les sorties ne sont pas versionnées ;
- les colonnes du CSV sont incohérentes ;
- les résultats ne peuvent pas être reliés aux cas ;
- le seuil est modifié après consultation des résultats sans décision documentée ;
- la vérité terrain est confondue avec la baseline ;
- les fallbacks sont interprétés comme des confirmations de vérité ;
- le manifeste n’autorise pas explicitement l’exécution.

---

## 19. Artefacts à produire

L’exécution doit produire :

- fichier des sorties NeoMundi ;
- fichier des sorties de baseline ;
- matrice de confusion ;
- rapport synthétique ;
- journal des erreurs ;
- manifeste d’exécution ;
- configuration d’exécution ;
- versions utilisées ;
- hash des fichiers d’entrée ;
- hash des fichiers de sortie ;
- commit GitHub du corpus gelé ;
- commit GitHub du protocole gelé.

---

## 20. Fichiers de sortie

Les fichiers de sortie prévus sont :

```text
EXP-001_smoke_test_neomundi_outputs.csv
EXP-001_smoke_test_baseline_outputs.csv
EXP-001_smoke_test_confusion_matrix.csv
EXP-001_smoke_test_report_FR.md
EXP-001_smoke_test_error_log.csv
EXP-001_smoke_test_run_manifest.json
```

Aucun fichier de sortie ne doit écraser un résultat antérieur sans versionnement explicite.

---

## 21. Hash et traçabilité

Avant exécution, les éléments suivants doivent être hashés :

- corpus gelé ;
- baseline gelée ;
- protocole gelé ;
- manifeste d’exécution ;
- configuration du signal ;
- version du script d’exécution.

Après exécution, les éléments suivants doivent également être hashés :

- sorties NeoMundi ;
- sorties de baseline ;
- matrice de confusion ;
- journal des erreurs ;
- rapport final.

L’algorithme de hash doit être enregistré dans le manifeste.

---

## 22. Manifeste d’exécution

Le fichier :

```text
EXP-001_smoke_test_run_manifest.json
```

doit enregistrer au minimum :

- identifiant du run ;
- date et heure ;
- commit GitHub ;
- branche ;
- hash du corpus ;
- hash du protocole ;
- hash de la baseline ;
- version de `MET-003` ;
- version du pipeline ;
- modèle juge ;
- endpoint ou type d’environnement ;
- seuil appliqué ;
- paramètres d’exécution ;
- versions logicielles ;
- statut de validation structurelle ;
- statut de documentation ;
- statut de validation gelée ;
- autorisation d’exécution.

Avant le lancement, les champs suivants doivent être à `true` :

```json
{
  "protocol_frozen": true,
  "corpus_frozen": true,
  "execution_authorized": true
}
```

---

## 23. Conditions obligatoires avant exécution

Aucune exécution ne doit commencer tant que les conditions suivantes ne sont pas toutes remplies :

- `MET-003` documenté ;
- implémentation identifiée ;
- seuil par défaut documenté ;
- configuration du juge documentée ;
- baseline déterministe définie ;
- références documentées ;
- références versionnées ;
- revue humaine terminée ;
- labels finaux confirmés ;
- splits attribués ;
- cas approuvés ;
- corpus hashé ;
- corpus gelé ;
- baseline gelée ;
- protocole gelé ;
- manifeste complété ;
- commit GitHub enregistré ;
- environnement enregistré ;
- validation `structural` réussie ;
- validation `documented` réussie ;
- validation `frozen` réussie ;
- autorisation d’exécution activée.

---

## 24. Statut actuel

- **Corpus structurellement valide :** oui
- **Références documentées :** oui
- **Références versionnées :** oui
- **Baseline définie :** oui
- **`MET-003` relié au code réel :** oui
- **Seuil par défaut documenté :** oui
- **Revue humaine terminée :** non
- **Splits attribués :** non
- **Corpus hashé :** non
- **Corpus gelé :** non
- **Protocole gelé :** non
- **Validation `frozen` réussie :** non
- **Exécution autorisée :** non

---

## 25. Prochaine étape

La prochaine étape est :

> effectuer et enregistrer la revue humaine des 20 cas avant attribution des splits et gel du corpus.

Les champs suivants devront être renseignés dans le CSV :

```text
review_status
reviewer_1_label
reviewer_1_confidence
reviewer_1_justification
arbitration_status
updated_at
```

Le champ :

```text
freeze_status
```

doit rester à :

```text
DRAFT
```

tant que la revue, les splits, le hash et le gel ne sont pas terminés.

---

## 26. Décision méthodologique

- **Expérience :** `EXP-001`
- **Type :** smoke test technique et méthodologique
- **Nombre de cas :** 20
- **Signal étudié :** `MET-003`
- **Événement cible :** `EVT-003`
- **Seuil par défaut observé :** `0.5`
- **Baseline :** déterministe, indépendante et gelée en version `v0.1`
- **Validation structurelle :** opérationnelle
- **Validation documentaire :** opérationnelle
- **Validation avant gel :** opérationnelle
- **Statut du protocole :** `FROZEN`
- **Version du protocole :** `v0.1`
- **Date de gel :** 2 août 2026
- **Modification après gel :** interdite sans création d’une nouvelle version
- **Exécution autorisée :** non
- **Conditions restantes :** gel de la métrique, du seuil et du corpus, enregistrement du commit final, mise à jour du manifeste et réussite de la validation `frozen`
- **Responsable du gel :** Sébastien
- **Dernière revue :** 2 août 2026
