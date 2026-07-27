# EXP-001 — Protocole d’exécution du smoke test

## 1. Objet

Ce document définit la manière dont le smoke test de 20 cas doit être exécuté.

L’objectif n’est pas encore de valider scientifiquement le signal de risque factuel NeoMundi.

Ce smoke test sert à vérifier :

- la cohérence des fichiers ;
- la bonne lecture du corpus ;
- le fonctionnement du pipeline ;
- la production des sorties attendues ;
- la compatibilité entre labels, signaux et résultats ;
- le calcul correct de la matrice de confusion ;
- la traçabilité complète de l’expérience.

---

## 2. Périmètre

Le smoke test contient :

- 10 cas négatifs ;
- 10 cas positifs ;
- 20 réponses au total ;
- un événement cible unique : `EVT-003` ;
- une dimension unique : factualité ;
- des cas fermés et simples ;
- des erreurs factuelles contrôlées.

Ce corpus ne doit pas être utilisé pour soutenir une affirmation scientifique ou commerciale de performance.

---

## 3. Fichiers d’entrée

L’exécution doit utiliser :

- `EXP-001_smoke_test_20_cases_FR.csv`
- `EXP-001_factuality_baseline_FR.md`
- `EXP-001_signal_selection_FR.md`
- `target_events_registry_FR.md`
- `false_positive_negative_protocol_FR.md`

---

## 4. Vérifications préalables

Avant l’exécution, vérifier :

- que les 20 identifiants sont uniques ;
- que 10 cas sont labellisés `POSITIVE` ;
- que 10 cas sont labellisés `NEGATIVE` ;
- qu’aucun label final n’est manquant ;
- que tous les cas utilisent `EVT-003` ;
- que les références sont renseignées ou explicitement marquées comme provisoires ;
- que le fichier CSV est lisible ;
- que le nombre de colonnes est constant ;
- que les valeurs autorisées sont respectées ;
- que la version du signal testé est enregistrée.

---

## 5. Point à corriger avant exécution

Dans le fichier du smoke test, la valeur `CONTROLLED` utilisée dans la colonne `origin_type` doit être remplacée.

Les valeurs autorisées sont :

- `NATURAL`
- `INJECTED`

Pour les cas corrects construits comme références, utiliser :

- `NATURAL` si la réponse provient réellement d’une observation existante ;
- `INJECTED` ou une future catégorie versionnée si le cas a été construit artificiellement.

Aucune exécution ne doit commencer avant correction de cette incohérence.

---

## 6. Entrée du signal NeoMundi

Pour chaque cas, le pipeline doit recevoir au minimum :

- `case_id`
- `prompt`
- `response`
- `target_event_id`
- version du signal
- version du pipeline
- date d’exécution

Le label de vérité terrain ne doit pas être transmis au signal testé.

---

## 7. Sortie attendue du signal

Pour chaque cas, NeoMundi doit produire :

- identifiant du cas ;
- score éventuel ;
- classification du signal ;
- statut positif ou négatif ;
- seuil appliqué ;
- version de la métrique ;
- version du seuil ;
- statut de calcul ;
- justification technique disponible ;
- erreurs ou données manquantes.

Valeurs minimales attendues :

- `SIGNAL_POSITIVE`
- `SIGNAL_NEGATIVE`
- `SIGNAL_UNAVAILABLE`
- `COMPUTATION_ERROR`

---

## 8. Sortie attendue de la baseline

Pour chaque cas, la baseline doit produire :

- `FACTUALLY_CORRECT`
- `FACTUALLY_INCORRECT`
- `UNDETERMINED`

La baseline doit être exécutée indépendamment du signal NeoMundi.

---

## 9. Comparaisons prévues

Trois sorties doivent être conservées séparément :

1. vérité terrain ;
2. baseline ;
3. signal NeoMundi.

Le smoke test doit vérifier que ces trois niveaux ne sont pas confondus.

---

## 10. Construction de la matrice de confusion

Pour NeoMundi :

| Vérité terrain | Signal NeoMundi | Résultat |
|---|---|---|
| POSITIVE | SIGNAL_POSITIVE | VP |
| NEGATIVE | SIGNAL_POSITIVE | FP |
| NEGATIVE | SIGNAL_NEGATIVE | VN |
| POSITIVE | SIGNAL_NEGATIVE | FN |

Les cas `SIGNAL_UNAVAILABLE` et `COMPUTATION_ERROR` doivent être comptabilisés séparément.

---

## 11. Calculs attendus

Le script ou le rapport doit calculer :

- nombre de VP ;
- nombre de FP ;
- nombre de VN ;
- nombre de FN ;
- nombre d’erreurs de calcul ;
- nombre de signaux indisponibles ;
- précision ;
- rappel ;
- spécificité ;
- taux de faux positifs ;
- taux de faux négatifs ;
- F1 ;
- couverture.

Sur 20 cas, ces chiffres servent uniquement à vérifier le pipeline.

---

## 12. Critères de réussite du smoke test

Le smoke test est considéré techniquement réussi si :

- les 20 cas sont chargés ;
- aucune ligne n’est perdue ;
- aucune colonne n’est décalée ;
- chaque cas reçoit une sortie ;
- les versions sont enregistrées ;
- la matrice de confusion est calculable ;
- les erreurs de calcul sont explicites ;
- les résultats peuvent être recalculés ;
- les sorties sont reliées aux identifiants des cas.

La réussite du smoke test ne dépend pas d’un niveau minimal de performance.

---

## 13. Critères d’échec méthodologique

Le smoke test doit être arrêté si :

- le signal accède aux labels ;
- les cas positifs et négatifs ne sont pas indépendants du calcul ;
- les sorties ne sont pas versionnées ;
- les colonnes du CSV sont incohérentes ;
- les résultats ne peuvent pas être reliés aux cas ;
- un seuil est modifié après lecture des résultats sans traçabilité ;
- la vérité terrain est confondue avec la baseline.

---

## 14. Artefacts à produire

L’exécution doit produire :

- fichier des sorties NeoMundi ;
- fichier des sorties baseline ;
- matrice de confusion ;
- rapport synthétique ;
- journal des erreurs ;
- configuration d’exécution ;
- versions utilisées ;
- hash des fichiers d’entrée ;
- hash des résultats.

---

## 15. Fichiers de sortie recommandés

```text
EXP-001_smoke_test_neomundi_outputs.csv
EXP-001_smoke_test_baseline_outputs.csv
EXP-001_smoke_test_confusion_matrix.csv
EXP-001_smoke_test_report_FR.md
EXP-001_smoke_test_error_log.csv
EXP-001_smoke_test_run_manifest.json
