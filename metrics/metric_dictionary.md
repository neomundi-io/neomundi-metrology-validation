# NeoMundi Metric Dictionary

## Purpose

This document defines the official NeoMundi metrics, their intended meaning, current status, interpretation limits and required validation work.

A metric must not be presented as validated until its definition, implementation, calibration and validation protocol have been documented.

---

## Methodological status vocabulary

- **Exploratory**: concept or signal under investigation
- **Defined**: measurement objective and interpretation documented
- **Implemented**: calculation exists in the NeoMundi pipeline
- **Tested**: calculation checked on controlled cases
- **Calibrated**: thresholds or interpretation ranges estimated
- **Validated**: performance measured against a documented reference
- **Replicated**: result reproduced in another campaign or environment

---

## Standard metric record

Each metric must contain:

- metric identifier;
- official name;
- version;
- current status;
- measurement objective;
- target phenomenon;
- inputs;
- formula or algorithm;
- output type;
- unit or scale;
- expected range;
- interpretation;
- thresholds;
- missing-data behaviour;
- dependencies;
- sensitivity factors;
- known limitations;
- non-claims;
- numerical example;
- validation reference;
- required validation test;
- implementation location;
- evidence location;
- decision owner;
- last review date.

---

# MET-001 — Stability Score

## Identification

- **Metric ID:** MET-001
- **Official name:** Stability Score
- **Version:** to be frozen
- **Current status:** implemented — methodological definition pending consolidation

## Definition

- **Measurement objective:** measure variation across repeated executions of the same case.
- **Target phenomenon:** response stability under a controlled repeated-execution protocol.
- **Inputs:** to be documented from the current implementation.
- **Formula or algorithm:** to be extracted and frozen from the existing code.
- **Output type:** numerical score.
- **Unit or scale:** to be confirmed.
- **Expected range:** to be confirmed.

## Interpretation

- **Interpretation:** to be formally defined.
- **Thresholds:** not yet methodologically frozen.
- **Missing-data behaviour:** to be documented.
- **Dependencies:** repetition protocol, semantic representation and aggregation method.
- **Sensitivity factors:** model, prompt, parameters, embedding model, number of repetitions and response length.

## Limitations

- Stability does not imply factual correctness.
- Stability does not imply compliance.
- A variable response may remain correct.
- A stable response may remain systematically false.

## Validation

- **Validation reference:** human-reviewed repeated-response corpus.
- **Required validation test:** intra-prompt analysis and comparison with a semantic-similarity baseline.
- **Implementation location:** to be added.
- **Evidence location:** to be added.
- **Decision owner:** Sébastien.
- **Last review date:** 2026-07-27.

---

# MET-002 — Semantic Variation Rate

## Identification

- **Metric ID:** MET-002
- **Official name:** Semantic Variation Rate
- **Version:** to be frozen
- **Current status:** implemented — methodological definition pending consolidation

## Definition

- **Measurement objective:** identify significant semantic divergence across multiple responses.
- **Target phenomenon:** variation in meaning across multiple executions of the same case.
- **Inputs:** to be documented from the current implementation.
- **Formula or algorithm:** to be extracted and frozen from the existing code.
- **Output type:** numerical rate or classification.
- **Unit or scale:** to be confirmed.
- **Expected range:** to be confirmed.

## Interpretation

- **Interpretation:** to be formally defined.
- **Thresholds:** not yet methodologically frozen.
- **Missing-data behaviour:** to be documented.
- **Dependencies:** embedding model, similarity method, clustering or thresholding method.
- **Sensitivity factors:** response length, language, paraphrase and embedding-model version.

## Limitations

- Semantic variation does not automatically constitute an error.
- Lexical variation may occur without a meaningful change in meaning.
- Similar wording may conceal factual or logical disagreement.

## Validation

- **Validation reference:** human-labelled semantic-variation corpus.
- **Required validation test:** confusion matrix against human labels.
- **Implementation location:** to be added.
- **Evidence location:** to be added.
- **Decision owner:** Sébastien.
- **Last review date:** 2026-07-27.

---

# MET-003 — Factual Risk Signal

## Identification

- **Metric ID:** MET-003
- **Official name:** Factual Risk Signal
- **Implemented field name:** `factual_hallucination_score`
- **Legacy alias:** `hallucination_score`
- **Version:** backend implementation observed on 2026-08-02 at commit `f02f7ff` — default threshold `0.5`
- **Current status:** implemented and linked to a code version — methodological calibration and validation pending

## Definition

- **Measurement objective:** produce a score associated with the degree of factual incorrectness in a response, while separating this signal from prompt instability or ambiguity.
- **Target phenomenon:** potential presence, in the evaluated response, of demonstrably false, fabricated, misleading or off-topic claims.
- **Inputs:**
  - evaluated model response;
  - associated prompt;
  - judge system prompt;
  - configured judge model;
  - judge endpoint;
  - execution parameters;
  - configured classification threshold.
- **Formula or algorithm:** evaluation by an `LLM-as-Judge` model. The judge receives the prompt and response and returns a JSON object containing, among other fields, `factual_hallucination_score`, `semantic_instability_score`, `confidence`, `reasoning` and `suspect_phrases`. The returned factual score is converted to a number, clamped to the `[0,1]` interval using `clamp01`, and rounded to four decimal places. The boolean classification is produced by comparing the score with a configurable threshold.
- **Output type:**
  - numerical `factual_hallucination_score`;
  - boolean `is_hallucinated` classification;
  - confidence score;
  - short reasoning;
  - suspect passages;
  - judge-model and latency information.
- **Unit or scale:** unitless score between `0` and `1`.
- **Expected range:** `[0,1]`.
- **Internal interpretation convention:**
  - `0` represents no factual risk detected by the judge;
  - `1` represents a response assessed by the judge as entirely false or off-topic.

## Interpretation

- **Interpretation:** the higher the score, the more strongly the judge model estimates that the response contains a significant factual error or is off-topic. The result is a risk signal and not independent proof of falsity.
- **Thresholds:** by default, the `is_hallucinated` classification is calculated when `factual_hallucination_score >= 0.5`. This threshold is implemented in the `detect_hallucination` function, but it has not yet been methodologically calibrated or validated. It can be overridden with another value when the function is called.
- **Suspect-passage extraction:** the judge prompt requests `suspect_phrases` when the factual score is greater than `0.3`. This value governs suspect-passage extraction and is not the default classification threshold.
- **Missing-data or unavailability behaviour:**
  - an empty response currently produces a factual score of `0.0`, a negative classification and a confidence of `0.0`, with the reasoning `Empty response`;
  - when no judge API key is configured or detection is unavailable, the system returns a fallback result with a factual score of `0.0`, a negative classification, a confidence of `0.0` and a fallback marker;
  - a fallback score of `0.0` must not be interpreted as confirmation that the response is factually correct.
- **Dependencies:**
  - judge-model availability and version;
  - judge endpoint and configuration;
  - evaluation system prompt;
  - JSON parser;
  - `clamp01` function;
  - classification threshold;
  - fallback logic.
- **Sensitivity factors:**
  - judge model;
  - judge-model version;
  - evaluation-prompt wording;
  - language;
  - domain;
  - response length and complexity;
  - prompt ambiguity;
  - quality of implicit or explicit references;
  - threshold configuration;
  - judge-backend availability.

## Numerical example

Illustrative example only:

- score returned by the judge: `0.72`;
- configured threshold: `0.50`;
- result: `is_hallucinated = true`.

This example does not represent a recommended, calibrated or validated threshold.

## Limitations

- The score is produced by a judge model and not by deterministic factual verification.
- The judge model may produce false positives and false negatives.
- A factual-risk signal is not proof that a response is false.
- Absence of an alert is not proof that a response is true.
- The score depends on the configuration, version and behaviour of the judge model.
- Performance may vary by domain, language and reference type.
- An empty response or judge unavailability may currently produce a fallback score of `0.0`.
- The score must not be presented as an autonomous measure of truth.
- The `0.5` threshold must not be presented as calibrated, validated or universal.
- Separation between factual risk and semantic instability depends on the judge model’s ability to distinguish these phenomena.
- Linking the metric to commit `f02f7ff` freezes the implementation observed for `EXP-001`, but does not validate its performance.

## Non-claims

- MET-003 does not certify the truth of a response.
- MET-003 is not legal, scientific or expert proof of falsity.
- MET-003 does not guarantee the absence of hallucination when the score is low.
- MET-003 is not a universal measurement independent of the judge model.
- MET-003 must not be used alone to allow or block a high-impact decision before calibration and validation.
- The `0.5` threshold is not a universal or optimal threshold.
- The `EXP-001` smoke test cannot authorize a general performance claim.

## Validation

- **Validation reference:** objective ground truth, verifiable references or independent expert review, with annotators blinded to NeoMundi scores.
- **Required validation test:**
  - positive and negative controls;
  - confusion matrix;
  - precision;
  - recall;
  - specificity;
  - false-positive rate;
  - false-negative rate;
  - error analysis;
  - comparison with an independent factual baseline;
  - analysis by domain, language and case type;
  - testing of empty-response and judge-unavailability behaviour;
  - comparison of several thresholds around the default `0.5` value.
- **Implementation location:** `govern-v3/app/core/hallucination_detector.py`
- **Main function:** `detect_hallucination`
- **Implementation commit:** `f02f7ff`
- **Existing tests identified:** `govern-v3/tests/test_core/test_hallucination.py`
- **Evidence location:** to be produced in `EXP-001` after the corpus, threshold, judge configuration and protocol have been frozen.
- **Decision owner:** Sébastien.
- **Last review date:** 2026-08-02.

---

# MET-004 — Longitudinal Drift Signal

## Identification

- **Metric ID:** MET-004
- **Official name:** Longitudinal Drift Signal
- **Version:** to be frozen
- **Current status:** measured — validation pending

## Definition

- **Measurement objective:** detect sustained change relative to a frozen baseline.
- **Target phenomenon:** longitudinal change across comparable campaigns.
- **Inputs:** to be documented.
- **Formula or algorithm:** to be documented.
- **Output type:** signal or score.
- **Unit or scale:** to be confirmed.
- **Expected range:** to be confirmed.

## Interpretation

- **Interpretation:** measured change relative to a defined baseline and protocol.
- **Thresholds:** to be calibrated.
- **Missing-data behaviour:** to be documented.
- **Dependencies:** corpus stability, versioning and campaign comparability.
- **Sensitivity factors:** model changes, provider changes, judge changes, corpus changes and sampling-method changes.

## Limitations

- A change does not automatically represent degradation.
- A one-off variation does not necessarily constitute drift.
- Drift detection does not automatically support prediction of future failure.

## Validation

- **Validation reference:** repeated campaigns on a fixed corpus.
- **Required validation test:** longitudinal comparison across multiple campaigns.
- **Implementation location:** to be added.
- **Evidence location:** to be added.
- **Decision owner:** Sébastien.
- **Last review date:** 2026-07-27.

---

# MET-005 — Delta G

## Identification

- **Metric ID:** MET-005
- **Official name:** Delta G
- **Version:** to be frozen
- **Current status:** exploratory or implemented — exact status to be confirmed

## Definition

- **Measurement objective:** to be formally specified.
- **Target phenomenon:** to be formally specified.
- **Inputs:** to be extracted from the current implementation.
- **Formula or algorithm:** to be extracted and frozen from the code.
- **Output type:** numerical value.
- **Unit or scale:** to be confirmed.
- **Expected range:** to be confirmed.

## Interpretation

- **Interpretation:** not yet frozen.
- **Thresholds:** not yet methodologically validated.
- **Missing-data behaviour:** to be documented.
- **Dependencies:** to be documented.
- **Sensitivity factors:** prompt, model, response length, tokenization and runtime configuration.

## Limitations

- A high Delta G value must not automatically be interpreted as an error.
- The metric must not be presented as thermodynamic proof without separate validation.
- No universal threshold may be claimed before multi-context calibration.

## Validation

- **Validation reference:** to be defined.
- **Required validation test:** sensitivity, ablation, controlled perturbation and baseline comparison.
- **Implementation location:** to be added.
- **Evidence location:** to be added.
- **Decision owner:** Sébastien.
- **Last review date:** 2026-07-27.

---

## Metrics to be added

The following metrics must be added after extraction from the current pipeline:

- coherence;
- compliance;
- Runtime R;
- information density;
- energy;
- latency;
- cost;
- regime classification;
- trajectory metrics;
- Oracle Law E candidate metrics.
