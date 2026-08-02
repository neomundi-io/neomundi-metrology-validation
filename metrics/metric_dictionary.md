# MET-003 — Factual Risk Signal

## Identification

- **Metric ID:** MET-003
- **Official name:** Factual Risk Signal
- **Implemented field name:** `factual_hallucination_score`
- **Legacy alias:** `hallucination_score`
- **Version:** Backend implementation observed on 2026-08-02 — default threshold `0.5`; pipeline version and commit to be frozen
- **Current status:** Implemented — methodological calibration and validation pending

## Definition

- **Measurement objective:** Produce a score associated with the degree of factual incorrectness in a response, while separating this signal from prompt instability or ambiguity.
- **Target phenomenon:** Potential presence, in the evaluated response, of demonstrably false, fabricated, misleading or off-topic claims.
- **Inputs:**
  - evaluated model response;
  - associated prompt;
  - judge system prompt;
  - configured judge model;
  - judge endpoint;
  - execution parameters;
  - configured classification threshold.
- **Formula or algorithm:** Evaluation by an `LLM-as-Judge` model. The judge receives the prompt and response and returns a JSON object containing, among other fields, `factual_hallucination_score`, `semantic_instability_score`, `confidence`, `reasoning` and `suspect_phrases`. The returned factual score is converted to a number, clamped to the `[0,1]` interval using `clamp01`, and rounded to four decimal places. The boolean classification is produced by comparing the score with a configurable threshold.
- **Output type:**
  - numerical `factual_hallucination_score`;
  - boolean `is_hallucinated` classification;
  - confidence score;
  - short reasoning;
  - suspect passages;
  - judge-model and latency information.
- **Unit or scale:** Unitless score between `0` and `1`.
- **Expected range:** `[0,1]`.
- **Internal interpretation convention:**
  - `0` represents no factual risk detected by the judge;
  - `1` represents a response assessed by the judge as entirely false or off-topic.

## Interpretation

- **Interpretation:** The higher the score, the more strongly the judge model estimates that the response contains a significant factual error or is off-topic. The result is a risk signal and not independent proof of falsity.
- **Thresholds:** By default, the `is_hallucinated` classification is calculated when `factual_hallucination_score >= 0.5`. This threshold is implemented in the `detect_hallucination` function, but it has not yet been methodologically calibrated or validated. It can be overridden with another value when the function is called.
- **Suspect-phrase extraction:** The judge prompt requests `suspect_phrases` when the factual score is greater than `0.3`. This value governs suspect-passage extraction and is not the default classification threshold.
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

This example does not represent a recommended or validated threshold.

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

## Non-claims

- MET-003 does not certify the truth of a response.
- MET-003 is not legal, scientific or expert proof of falsity.
- MET-003 does not guarantee the absence of hallucination when the score is low.
- MET-003 is not a universal measurement independent of the judge model.
- MET-003 must not be used alone to allow or block a high-impact decision before calibration and validation.

## Validation

- **Validation reference:** Objective ground truth, verifiable references or independent expert review, with annotators blinded to NeoMundi scores.
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
- **Existing tests identified:** `govern-v3/tests/test_core/test_hallucination.py`
- **Evidence location:** To be produced in `EXP-001` after the corpus, threshold, judge configuration and protocol have been frozen.
- **Decision owner:** Sébastien
- **Last review date:** 2026-08-02

---
