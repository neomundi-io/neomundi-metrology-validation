# NeoMundi Metric Dictionary

## Purpose

This document defines the official NeoMundi metrics, their intended meaning, calculation status, interpretation limits and validation requirements.

A metric must not be presented as validated until its definition, implementation, calibration and validation status are documented.

---

## Metric status vocabulary

- **Exploratory**: concept or signal under investigation
- **Defined**: purpose and interpretation are documented
- **Implemented**: calculation exists in the NeoMundi pipeline
- **Tested**: calculation has been checked on controlled cases
- **Calibrated**: thresholds or interpretation ranges have been estimated
- **Validated**: performance has been measured against a documented reference
- **Replicated**: results have been reproduced on another campaign or environment

---

## Standard metric record

Each metric must contain:

- Metric ID
- Official name
- Version
- Current status
- Measurement objective
- Target phenomenon
- Inputs
- Formula or algorithm
- Output type
- Unit or scale
- Expected range
- Interpretation
- Thresholds
- Missing-data behaviour
- Dependencies
- Sensitivity factors
- Known limitations
- Non-claims
- Numerical example
- Validation reference
- Required validation test
- Implementation location
- Evidence location
- Decision owner
- Last review date

---

# MET-001 — Stability Score

## Identification

- **Metric ID:** MET-001
- **Official name:** Stability Score
- **Version:** To be frozen
- **Current status:** Implemented — methodological definition pending consolidation

## Definition

- **Measurement objective:** Measure variation across repeated executions of the same case.
- **Target phenomenon:** Response stability under a controlled repeated-execution protocol.
- **Inputs:** To be documented from the current implementation.
- **Formula or algorithm:** To be extracted and frozen from the current code.
- **Output type:** Numerical score.
- **Unit or scale:** To be confirmed.
- **Expected range:** To be confirmed.

## Interpretation

- **Interpretation:** To be formally defined.
- **Thresholds:** Not yet methodologically frozen.
- **Missing-data behaviour:** To be documented.
- **Dependencies:** Repetition protocol, semantic representation and aggregation method.
- **Sensitivity factors:** Model, prompt, parameters, embedding model, number of repetitions and response length.

## Limitations

- Stability does not imply factual correctness.
- Stability does not imply compliance.
- A variable response may remain correct.
- A stable response may remain systematically false.

## Validation

- **Validation reference:** Human-reviewed repeated-response corpus.
- **Required validation test:** Intra-prompt analysis and comparison with a semantic-similarity baseline.
- **Implementation location:** To be added.
- **Evidence location:** To be added.
- **Decision owner:** Sébastien
- **Last review date:** 2026-07-27

---

# MET-002 — Semantic Variation Rate

## Identification

- **Metric ID:** MET-002
- **Official name:** Semantic Variation Rate
- **Version:** To be frozen
- **Current status:** Implemented — methodological definition pending consolidation

## Definition

- **Measurement objective:** Identify meaningful semantic divergence across repeated responses.
- **Target phenomenon:** Semantic variation between executions of the same case.
- **Inputs:** To be documented from the current implementation.
- **Formula or algorithm:** To be extracted and frozen from the current code.
- **Output type:** Numerical rate or classification.
- **Unit or scale:** To be confirmed.
- **Expected range:** To be confirmed.

## Interpretation

- **Interpretation:** To be formally defined.
- **Thresholds:** Not yet methodologically frozen.
- **Missing-data behaviour:** To be documented.
- **Dependencies:** Embedding model, similarity method, clustering or thresholding method.
- **Sensitivity factors:** Response length, language, paraphrase and embedding version.

## Limitations

- Semantic variation does not automatically indicate an error.
- Lexical variation may occur without meaningful semantic variation.
- Similar wording may conceal factual or logical disagreement.

## Validation

- **Validation reference:** Human-labelled semantic-variation corpus.
- **Required validation test:** Confusion matrix against labelled cases.
- **Implementation location:** To be added.
- **Evidence location:** To be added.
- **Decision owner:** Sébastien
- **Last review date:** 2026-07-27

---

# MET-003 — Factual Risk Signal

## Identification

- **Metric ID:** MET-003
- **Official name:** Factual Risk Signal
- **Version:** To be frozen
- **Current status:** Exploratory or implemented — status to be confirmed

## Definition

- **Measurement objective:** Produce a signal associated with a possible significant factual error.
- **Target phenomenon:** Factual-risk event defined against an objective or expert-validated reference.
- **Inputs:** To be documented.
- **Formula or algorithm:** To be documented.
- **Output type:** Signal, score or classification.
- **Unit or scale:** To be confirmed.
- **Expected range:** To be confirmed.

## Interpretation

- **Interpretation:** Risk signal requiring contextual validation.
- **Thresholds:** Not yet validated.
- **Missing-data behaviour:** To be documented.
- **Dependencies:** Reference source, judge configuration and classification method.
- **Sensitivity factors:** Domain, language, source quality, judge model and prompt design.

## Limitations

- A factual-risk signal is not proof that a response is false.
- Absence of an alert is not proof that a response is true.
- Performance may vary by domain and reference type.

## Validation

- **Validation reference:** Objective ground truth or independent expert review.
- **Required validation test:** Positive and negative control study with confusion matrix.
- **Implementation location:** To be added.
- **Evidence location:** To be added.
- **Decision owner:** Sébastien
- **Last review date:** 2026-07-27

---

# MET-004 — Longitudinal Drift Signal

## Identification

- **Metric ID:** MET-004
- **Official name:** Longitudinal Drift Signal
- **Version:** To be frozen
- **Current status:** Measured — validation pending

## Definition

- **Measurement objective:** Detect sustained changes relative to a frozen baseline.
- **Target phenomenon:** Longitudinal change across comparable campaigns.
- **Inputs:** To be documented.
- **Formula or algorithm:** To be documented.
- **Output type:** Signal or score.
- **Unit or scale:** To be confirmed.
- **Expected range:** To be confirmed.

## Interpretation

- **Interpretation:** Change relative to a defined baseline and protocol.
- **Thresholds:** To be calibrated.
- **Missing-data behaviour:** To be documented.
- **Dependencies:** Stable corpus, protocol versioning and campaign comparability.
- **Sensitivity factors:** Model updates, provider changes, judge changes, corpus changes and sampling variation.

## Limitations

- A change does not automatically represent degradation.
- A one-off variation is not necessarily a drift.
- Drift detection does not imply prediction of future failure.

## Validation

- **Validation reference:** Repeated fixed-corpus campaigns.
- **Required validation test:** Multi-campaign longitudinal comparison.
- **Implementation location:** To be added.
- **Evidence location:** To be added.
- **Decision owner:** Sébastien
- **Last review date:** 2026-07-27

---

# MET-005 — Delta G

## Identification

- **Metric ID:** MET-005
- **Official name:** Delta G
- **Version:** To be frozen
- **Current status:** Exploratory or implemented — exact status to be confirmed

## Definition

- **Measurement objective:** To be formally specified.
- **Target phenomenon:** To be formally specified.
- **Inputs:** To be extracted from the current implementation.
- **Formula or algorithm:** To be extracted and frozen from the current code.
- **Output type:** Numerical value.
- **Unit or scale:** To be confirmed.
- **Expected range:** To be confirmed.

## Interpretation

- **Interpretation:** Not yet frozen.
- **Thresholds:** Not yet methodologically validated.
- **Missing-data behaviour:** To be documented.
- **Dependencies:** To be documented.
- **Sensitivity factors:** Prompt, model, response length, tokenization and runtime configuration.

## Limitations

- A high Delta G value must not automatically be interpreted as an error.
- The metric must not be presented as thermodynamic proof without separate validation.
- Universal thresholds must not be claimed before cross-context calibration.

## Validation

- **Validation reference:** To be defined.
- **Required validation test:** Sensitivity, ablation, controlled perturbation and baseline comparison.
- **Implementation location:** To be added.
- **Evidence location:** To be added.
- **Decision owner:** Sébastien
- **Last review date:** 2026-07-27

---

## Pending metrics

The following metrics must be added after extraction from the current pipeline:

- Coherence
- Compliance
- Runtime R
- Information Density
- Energy
- Latency
- Cost
- Regime Classification
- Trajectory Metrics
- Oracle Law E Candidate Metrics
