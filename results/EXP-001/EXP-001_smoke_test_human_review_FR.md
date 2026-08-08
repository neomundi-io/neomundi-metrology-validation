# EXP-001 — Revue humaine post-run

## 1. Identification

- **Expérience :** `EXP-001`
- **Version :** `v0.1`
- **Run :** `EXP001-SMOKE-RUN-001`
- **Métrique évaluée :** `MET-003`
- **Nom :** Signal de risque factuel
- **Seuil expérimental gelé :** `>= 0.5`
- **Runner :** `v0.1.1`
- **Analyseur :** `v0.2`
- **Baseline :** `v0.1`
- **GitHub Run ID :** `31266032346`
- **Date de la revue humaine :** `2026-08-08`
- **Relecteur principal :** Sébastien
- **Type de revue :** revue humaine post-run
- **Statut :** `COMPLETED`

---

## 2. Objet de la revue

Cette revue humaine intervient après l’exécution du smoke test `EXP-001`.

Elle vise à vérifier :

- la cohérence entre les sorties brutes NeoMundi et les classifications expérimentales ;
- les faux positifs éventuels ;
- les faux négatifs éventuels ;
- les erreurs de calcul éventuelles ;
- les signaux indisponibles éventuels ;
- la cohérence entre score et classification ;
- les éventuels résultats atypiques ;
- les informations de fallback exposées ou non exposées ;
- la cohérence entre NeoMundi, la baseline déterministe indépendante et la vérité terrain gelée.

Cette revue ne modifie pas :

- le corpus ;
- la vérité terrain ;
- les labels finaux ;
- la baseline ;
- le seuil ;
- le protocole ;
- les sorties NeoMundi brutes.

---

## 3. Artefacts examinés

Les artefacts suivants ont été examinés :

- `EXP-001_smoke_test_20_cases_FR.csv`
- `EXP-001_smoke_test_neomundi_outputs.csv`
- `EXP-001_smoke_test_error_log.csv`
- `EXP-001_smoke_test_baseline_outputs.csv`
- `EXP-001_smoke_test_confusion_matrix.csv`
- `EXP-001_smoke_test_report_FR.md`
- `EXP-001_smoke_test_artifact_hashes.json`

---

## 4. Intégrité du corpus

Le corpus gelé contient :

- **20 cas** ;
- **10 cas POSITIVE** ;
- **10 cas NEGATIVE** ;
- **10 paires correcte / incorrecte**.

Le SHA-256 vérifié du corpus est :

```text
bd9ac82fd53aab35fba15ff999033f894f69775d256940f27694677720174ce1
```

Ce hash correspond au hash gelé attendu pour `EXP-001 v0.1`.

Aucune modification du corpus n’a été constatée pendant l’exécution ou l’analyse.

**Décision :** `PASS`

---

## 5. Vérification de la séparation méthodologique

Trois niveaux distincts ont été conservés :

1. vérité terrain gelée ;
2. baseline déterministe indépendante ;
3. signal NeoMundi `MET-003`.

La baseline `v0.1` utilise :

```text
DETERMINISTIC_PROMPT_RESPONSE_RULES
```

Sa fonction de décision reçoit uniquement :

- `prompt`
- `response`

Elle ne reçoit pas :

- `ground_truth_label`
- `final_label`
- les labels des évaluateurs ;
- le score NeoMundi ;
- la classification NeoMundi.

La comparaison avec la vérité terrain intervient uniquement après production de la décision de baseline.

**Décision :** `PASS`

---

## 6. Vérification des sorties NeoMundi

Nombre de sorties NeoMundi :

```text
20 / 20
```

Statut HTTP observé :

```text
200
```

pour les 20 cas.

Statut de calcul :

```text
CALCULATED
```

pour les 20 cas.

Nombre d’erreurs de calcul :

```text
0
```

Nombre de signaux indisponibles :

```text
0
```

Le journal d’erreurs ne contient aucune ligne d’erreur.

**Décision :** `PASS`

---

## 7. Cohérence entre score et classification

Règle expérimentale gelée :

```text
is_hallucinated = factual_hallucination_score >= 0.5
```

Les 20 sorties ont été vérifiées au regard de cette règle.

### Cas classés `SIGNAL_NEGATIVE`

Les cas négatifs présentent :

```text
factual_hallucination_score = 0.0
```

et :

```text
is_hallucinated = false
experimental_signal_class = SIGNAL_NEGATIVE
```

### Cas classés `SIGNAL_POSITIVE`

Les cas positifs présentent des scores compris entre :

```text
0.9
```

et :

```text
1.0
```

avec :

```text
is_hallucinated = true
experimental_signal_class = SIGNAL_POSITIVE
```

Aucune incohérence entre score, booléen `is_hallucinated` et classification expérimentale n’a été observée.

**Décision :** `PASS`

---

## 8. Matrice de confusion NeoMundi

Résultats observés :

| Résultat | Nombre |
|---|---:|
| VP | 10 |
| FP | 0 |
| VN | 10 |
| FN | 0 |
| Signal indisponible | 0 |
| Erreur de calcul | 0 |

Aucun faux positif n’a été observé.

Aucun faux négatif n’a été observé.

**Décision :** `PASS`

---

## 9. Baseline déterministe indépendante

La baseline a produit :

```text
20 décisions calculées
```

Nombre de cas `UNDETERMINED` :

```text
0
```

Résultats observés :

| Résultat | Nombre |
|---|---:|
| VP | 10 |
| FP | 0 |
| VN | 10 |
| FN | 0 |
| Indéterminé | 0 |

La baseline et NeoMundi aboutissent à la même classification sur les 20 cas de ce corpus contrôlé.

Cette convergence ne constitue pas une preuve de généralisation.

**Décision :** `PASS`

---

## 10. Revue des faux positifs

Nombre de faux positifs NeoMundi :

```text
0
```

Aucun cas `NEGATIVE` n’a été classé `SIGNAL_POSITIVE`.

Aucune revue corrective spécifique n’est donc requise pour un faux positif dans ce run.

**Décision :** `PASS`

---

## 11. Revue des faux négatifs

Nombre de faux négatifs NeoMundi :

```text
0
```

Aucun cas `POSITIVE` n’a été classé `SIGNAL_NEGATIVE`.

Aucune revue corrective spécifique n’est donc requise pour un faux négatif dans ce run.

**Décision :** `PASS`

---

## 12. Distribution des scores

### Cas POSITIVE

- **n :** 10
- **minimum :** `0.9000`
- **maximum :** `1.0000`
- **moyenne :** `0.9900`
- **médiane :** `1.0000`

### Cas NEGATIVE

- **n :** 10
- **minimum :** `0.0000`
- **maximum :** `0.0000`
- **moyenne :** `0.0000`
- **médiane :** `0.0000`

La séparation est complète sur ce petit corpus synthétique contrôlé.

Cette observation ne doit pas être interprétée comme une propriété générale de `MET-003`.

---

## 13. Vérification des passages suspects

Les sorties brutes montrent que les cas factuellement incorrects peuvent contenir des `suspect_phrases` associées à une explication technique du signal.

Exemples observés :

- attribution de la capitale de la France à Lyon ;
- résultat `2 + 2 = 5`.

Ces passages sont cohérents avec les erreurs contrôlées présentes dans les réponses synthétiques correspondantes.

Aucune incohérence manifeste entre le passage signalé et l’erreur contrôlée du cas n’a été observée dans les sorties examinées.

**Décision :** `PASS`

---

## 14. Modèle juge

Le manifeste documente le juge configuré comme :

```text
mistral24b
```

via Infomaniak Euria.

Les sorties API du run ne fournissent toutefois pas de champ explicite permettant de confirmer directement le modèle juge utilisé pour chaque observation.

Le champ :

```text
judge_model_exposed_by_api
```

reste vide.

Par conséquent :

- le juge configuré est documenté par l’environnement d’exécution ;
- son identité n’est pas directement attestée par chaque réponse API.

Aucune conclusion plus forte ne doit être produite à partir des sorties seules.

**Décision :** `DOCUMENTED_LIMITATION`

---

## 15. Fallback

Les sorties enregistrent :

```text
fallback_status = UNKNOWN_NOT_EXPOSED
```

et :

```text
fallback_information_exposed_by_api = false
```

pour les observations examinées.

Cela signifie que l’API ne fournit pas explicitement l’information de fallback dans le contrat actuellement observé.

Il est donc interdit d’interpréter :

```text
UNKNOWN_NOT_EXPOSED
```

comme :

```text
NO_FALLBACK
```

Le run ne permet pas d’affirmer qu’aucun fallback n’a été utilisé.

**Décision :** `DOCUMENTED_LIMITATION`

---

## 16. Versionnement observé

Les sorties enregistrent :

```text
measurement_version = 3.0.0
normalizer_version = 1.0.0
runner_version = v0.1.1
github_run_id = 31266032346
github_run_attempt = 1
```

Ces informations permettent de relier les sorties à l’environnement technique utilisé pour ce run.

**Décision :** `PASS`

---

## 17. Latence observée

### Latence mesurée côté runner

- **n :** 20
- **minimum :** `20162.6610 ms`
- **maximum :** `20666.5520 ms`
- **moyenne :** `20284.8759 ms`
- **médiane :** `20186.8015 ms`

### Processing time retourné par l’API

- **n :** 20
- **minimum :** `20018.5700 ms`
- **maximum :** `20024.2700 ms`
- **moyenne :** `20020.3325 ms`
- **médiane :** `20019.9750 ms`

La latence observée est très stable autour de 20 secondes par cas.

Cette valeur est descriptive du run uniquement.

Elle ne constitue pas un benchmark de performance d’infrastructure.

**Décision :** `OBSERVED`

---

## 18. Incident technique préalable au run réussi

Une première tentative d’exécution a rencontré un blocage HTTP Cloudflare :

```text
HTTP 403
Error 1010
browser_signature_banned
```

Cette tentative n’a produit aucun signal NeoMundi exploitable.

Le runner a ensuite été corrigé afin d’utiliser un `User-Agent` HTTP explicite.

Le run réussi examiné dans la présente revue est :

```text
GitHub Run ID 31266032346
```

L’incident initial relève de la couche d’accès HTTP et non d’un résultat de `MET-003`.

Il ne doit pas être intégré à la matrice de confusion du run réussi.

Il constitue néanmoins un événement de traçabilité technique pertinent pour la reproductibilité du pipeline.

---

## 19. Hashes des artefacts finaux

Algorithme :

```text
SHA-256
```

### Corpus

```text
bd9ac82fd53aab35fba15ff999033f894f69775d256940f27694677720174ce1
```

### Sorties NeoMundi

```text
b2597b843859d1f07cc02321ec8083afeddae256c28688877c088d04af6bc542
```

### Journal d’erreurs

```text
e2d5b20f359b724bcc76a2fb18ededf59edb11eee9af10c2da318c6dd31ee255
```

### Baseline indépendante

```text
491a6598a1da22c15d9a775939496173fb3f4889b908ca25e01b6822eca0ea73
```

### Matrice de confusion

```text
e64d368d5a32364c63c599a4ab4555b9a26d9abbf479a07aef3f8315259d5e96
```

### Rapport FR

```text
d3a9208a30d9644961e1b71501f6429ca38f6861dbca3d7f9b4c04327acd3028
```

---

## 20. Conclusion de la revue humaine

La revue humaine post-run ne met en évidence :

- aucun faux positif ;
- aucun faux négatif ;
- aucune erreur de calcul ;
- aucun signal indisponible ;
- aucune incohérence entre score et classification ;
- aucune contamination observée de la baseline par les sorties NeoMundi ;
- aucune modification des éléments expérimentaux gelés.

Deux limites restent explicitement documentées :

1. le modèle juge utilisé n’est pas exposé directement dans chaque réponse API ;
2. le statut de fallback n’est pas exposé par le contrat API observé.

Ces limites n’empêchent pas de conclure à la réussite technique du smoke test.

---

## 21. Décision finale de revue

### Statut

```text
HUMAN_REVIEW_COMPLETED
```

### Décision

```text
TECHNICALLY_SUCCESSFUL
```

### Interprétation autorisée

`EXP-001 v0.1` démontre que la chaîne expérimentale est techniquement fonctionnelle et traçable sur le corpus synthétique contrôlé de 20 cas utilisé dans ce smoke test.

### Interprétations non autorisées

Cette revue ne permet pas d’affirmer :

- que `MET-003` est scientifiquement validé ;
- que `MET-003` atteint 100 % de performance en général ;
- que le seuil `0.5` est optimal ;
- que les résultats sont généralisables à des données naturelles ;
- que les résultats sont généralisables à d’autres langues, domaines ou distributions ;
- que l’absence d’un signal prouve la vérité d’une réponse ;
- qu’un signal constitue une preuve indépendante de fausseté ;
- qu’aucun fallback n’a été utilisé ;
- qu’un claim commercial général peut être dérivé de ces 20 cas.

---

## 22. Recommandation

`EXP-001 v0.1` peut être clôturé comme :

```text
SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

La prochaine étape scientifique ne doit pas consister à modifier rétrospectivement cette expérience.

Elle doit être réalisée dans une nouvelle expérience versionnée portant sur un corpus :

- plus large ;
- plus difficile ;
- moins trivial ;
- comportant des réponses ambiguës ou partiellement exactes ;
- comportant des erreurs plus subtiles ;
- comportant éventuellement des cas naturels ;
- permettant d’étudier les faux positifs, faux négatifs et zones proches du seuil.

---

## 23. Signature de revue

- **Relecteur :** Sébastien
- **Rôle :** responsable expérimental
- **Date :** 8 août 2026
- **Statut :** `COMPLETED`
