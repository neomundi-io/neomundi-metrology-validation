🇬🇧 **English version:** [README.md](./README.md) · 🇫🇷 **Version française :** [README_FR.md](./README_FR.md)

# NeoMundi Metrology Validation

Experimental program for the validation, calibration, reproducibility, and qualification of NeoMundi measurement signals.

This repository progressively documents:

- what NeoMundi measurements are intended to observe;
- how they are tested;
- under which conditions they work;
- where they fail;
- how they compare with independent references;
- and which claims the available evidence can actually support.

Core principle:

> **A measured signal is not automatically a verdict.**

---

# Current status

## First validation step completed — EXP-001

NeoMundi has completed its first controlled metrology smoke test.

It can be understood like testing a thermometer with water whose temperature is already known.

We prepared 20 simple cases:

- 10 containing a known factual error;
- 10 containing no factual error.

The correct answers were hidden from NeoMundi.

NeoMundi measured the 20 cases independently.

The results were then compared against:

1. the frozen ground truth;
2. an independent deterministic baseline;
3. a post-run human review.

For this controlled smoke test:

- 20 / 20 cases produced a measurement;
- 0 computation errors;
- 0 unavailable signals;
- 10 true positives;
- 10 true negatives;
- 0 false positives;
- 0 false negatives.

This does **not** mean that MET-003 is scientifically validated or that NeoMundi achieves 100% performance in general.

It means something simpler and more important at this stage:

> **The experimental chain works, it is traceable, and it can now be tested on harder and larger datasets.**

The next validation step will be conducted as a new versioned experiment, without retrospectively modifying EXP-001.

Status:

```text
EXP-001 = CLOSED
RESULT = SMOKE_TEST_TECHNICALLY_SUCCESSFUL

EXP-002 = NOT_STARTED
```

---

# Relationship with the research protocol

This experimental roadmap is the operational translation of the NeoMundi research protocol:

[**Research Protocol — Does AI runtime behavior constitute a distinct metrological object?**](https://zenodo.org/records/21822050)

The protocol asks the following general scientific question:

> **Do AI systems, during real operation, produce behavioral structures that are sufficiently real, reproducible, distinct, and useful to constitute an autonomous metrological object, complementary to classical metrics?**

This question cannot be credibly answered by a single experiment or a single metric.

Experiments `EXP-001` through `EXP-008` are intended to decompose this general question into smaller, falsifiable, and documentable experimental questions.

They are designed to progressively accumulate the different levels of evidence required.

| Major protocol question | Experiments contributing to it |
|---|---|
| **Is the phenomenon measurable?** | EXP-001, EXP-002, EXP-003 |
| **Are the measurements repeatable?** | EXP-004 |
| **Can they distinguish different phenomena?** | EXP-002, EXP-005, EXP-006 |
| **Do they provide information distinct from classical metrics?** | EXP-007 |
| **Can they be reproduced elsewhere?** | EXP-008 |
| **Do they hold over time?** | EXP-004 + EXP-008 |
| **Do they potentially have predictive value?** | EXP-008 and associated longitudinal experiments |
| **Do they improve a decision?** | Mainly EXP-007 |
| **Does a runtime metrological domain actually exist?** | **A cumulative conclusion from the whole program, not from a single experiment** |

The protocol distinguishes four general levels of evidence:

1. **Existence** — does the phenomenon exist beyond noise?
2. **Measurability** — are the metrics repeatable and sensitive?
3. **Metrological autonomy** — do the signals provide information distinct from classical metrics?
4. **Actionability** — does the measurement actually improve a decision?

The EXP-001 → EXP-008 roadmap is intended to progressively provide empirical evidence for each of these levels.

The relationship between the different objects is therefore:

```text
RESEARCH PROTOCOL
General scientific question
        ↓
EXPERIMENTAL ROADMAP
Decomposition into falsifiable questions
        ↓
EXP-001 → EXP-008
Versioned experiments
        ↓
RESULTS + ARTIFACTS + REPLICATIONS
Accumulation of evidence
        ↓
CLAIMS REGISTRY
Determination of what can be claimed
        ↓
CUMULATIVE CONCLUSION
Progressive determination of the validity domain
of NeoMundi runtime metrology
```

Essential principle:

> **The success of a single experiment or a specific metric is not sufficient to demonstrate the existence of a distinct runtime metrological domain.**

Conversely, the local failure of one metric does not necessarily refute the overall hypothesis.

The conclusion must emerge from the accumulation of results concerning, in particular:

- repeatability;
- sensitivity;
- discriminant validity;
- false positives and false negatives;
- calibration;
- external reproducibility;
- robustness across models and providers;
- longitudinal behavior;
- potential predictive value;
- incremental value compared with classical metrics;
- operational actionability.

---

# Origin and external methodological critiques

The roadmap does not arise solely from internal reflection.

It also builds on external audits and methodological critiques that have helped identify missing evidence, risks of misinterpretation, and the experiments required.

## Independent methodological audit — Stéphane Gorius

Stéphane Gorius’s independent report on the Kimi K3 observation report notably identified the need to strengthen:

- the operational definition of metrics;
- calibration;
- positive and negative controls;
- measurement of false positives and false negatives;
- sensitivity to known perturbations;
- use of repeated runs;
- separation between factuality, coherence, and other dimensions;
- reproducibility;
- the evidence chain;
- comparison with independent references.

This audit is preserved as an **external methodological contribution**.

It does not constitute scientific validation of NeoMundi.

It helps document the origin of some of the experimental questions in this roadmap.

Directory:

```text
external-audits/
```

Audit:

[**Constructive and Independent Methodological Audit — Stéphane Gorius**](./external-audits/Audit_methodologique_constructif_independant_NeoMundi_Kimi_K3_v1.1.pdf)

The following distinction must be preserved:

```text
EXTERNAL AUDIT
≠
VALIDATION
≠
REPLICATION
```

An audit may identify a weakness or propose an experiment.

Validation requires appropriate experimental data.

Replication requires another team or infrastructure to reproduce a result according to a documented specification.

---

# Position of this repository within the NeoMundi ecosystem

`neomundi-metrology-validation` has a distinct function from the other NeoMundi repositories.

Its main role is to progressively document and qualify the metrology used by NeoMundi.

Conceptual architecture:

```text
NeoMundi
│
├── neomundi-ai-observatory
│   │
│   └── Observes
│       Campaigns, barometers, mappings,
│       longitudinal series, and observed phenomena
│
├── neomundi-metrology-validation
│   │
│   └── Qualifies the measurement
│       Definitions, controls, calibration,
│       validation, baselines, FP/FN,
│       reproducibility, and evidence chain
│
├── runtime-interoperability-contract
│   │
│   └── Transports the signals
│       Contracts, semantics, and articulation
│       with independent infrastructures
│
└── uses / launchers / pilots
    │
    └── Use the signals
        Applications, governance,
        orchestration, and external decisions
```

In simple terms:

> **The Observatory looks at what is happening.**

> **Metrology Validation progressively verifies whether the instruments used to observe actually measure what we say they measure.**

> **The interoperability contract then allows those signals to be understood and consumed by other infrastructures.**

This separation is intentional.

```text
OBSERVATION
≠
MEASUREMENT VALIDATION
≠
INTEROPERABILITY
≠
USE OR DECISION
```

The `neomundi-metrology-validation` repository is intended to be referenced:

- from the Observatory repository;
- from the main NeoMundi organization page;
- from methodological documents whenever metric validity or qualification is discussed;
- from future experimental publications associated with the EXP series.

It constitutes the entry point to NeoMundi’s **metrological evidence chain**.

---

# How to read the roadmap

The experiments described below are not a sequence designed to artificially produce positive results.

They are a series of questions.

Each experiment may produce:

```text
positive result
limited result
ambiguous result
null result
local refutation
```

All of these outcomes are informative.

The purpose of this roadmap is to allow NeoMundi to progressively move from:

```text
We produce scores.
```

to:

```text
We know precisely
what certain measurements observe,
under which conditions they work,
where they fail,
what they add,
and which claims the available evidence supports.
```

The final scientific question remains open.

The roadmap is precisely the instrument through which we attempt to answer it.

---

# Experimental roadmap

**Version:** `v0.1`  
**Date:** August 8, 2026  
**Status:** `PROVISIONAL`

This roadmap provides direction for the validation program.

It does not constitute a frozen protocol.

Some experiments may:

- merge;
- be split;
- change order;
- be reformulated;
- produce sub-experiments;
- be replaced by a more relevant design.

General principle:

> **1 EXP = 1 metrological question precise enough to receive a documented experimental answer.**

The objective is not to artificially accumulate experiments.

The objective is to accumulate the evidence required to progressively determine what NeoMundi measurements can actually support.

---

# EXP-001 — MET-003 smoke test

**Status:** `CLOSED`

## Main question

> **Does the experimental chain used to evaluate the MET-003 factual risk signal work correctly on a small controlled corpus containing factually correct and incorrect responses?**

## Why this question?

Before actually evaluating the quality of an instrument, the entire chain must first be shown to work:

```text
case
↓
ground truth
↓
measurement
↓
classification
↓
baseline
↓
comparison
↓
confusion matrix
↓
human review
↓
artifacts
```

EXP-001 constitutes this first verification.

## Design

```text
20 cases
10 POSITIVE
10 NEGATIVE
```

The cases were deliberately simple and synthetic.

The ground truth was known before execution but hidden from the NeoMundi signal.

## Result

```text
20 cases processed
20 measurements calculated

10 true positives
10 true negatives
0 false positives
0 false negatives

0 computation errors
0 unavailable signals
```

Independent baseline:

```text
10 TP
10 TN
0 FP
0 FN
```

Human review:

```text
COMPLETED
```

## Authorized conclusion

> **The experimental chain used to test MET-003 works technically on the controlled EXP-001 corpus and produces traceable and analyzable results.**

## What EXP-001 does not demonstrate

EXP-001 does not demonstrate:

- that MET-003 is scientifically validated;
- that MET-003 has 100% general performance;
- that the `0.5` threshold is optimal;
- that MET-003 performs equally well on difficult cases;
- that MET-003 performs equally well on natural data;
- that NeoMundi provides additional value compared with existing methods.

Final status:

```text
SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

---

# EXP-002 — First experimental estimate of MET-003

**Status:** `NOT_STARTED`

## Main question

> **On a larger and more difficult frozen corpus, what is the actual ability of MET-003 to distinguish responses containing a significant factual error from responses in which that event is absent?**

## Why this question?

EXP-001 mainly verifies that the pipeline works.

EXP-002 must begin answering another question:

> **How does the signal actually behave once we stop giving it only trivial cases?**

## Indicative scale

```text
~100 POSITIVE
+
~100 NEGATIVE
```

This volume is indicative and must be confirmed before the protocol is frozen.

## Types of cases considered

The corpus should include more:

- simple facts;
- entity errors;
- date errors;
- numerical errors;
- geographical errors;
- partially correct responses;
- claims containing multiple facts;
- subtler errors;
- ambiguous cases;
- cases close to the decision boundary;
- potentially natural cases.

## Secondary questions

- how many true positives?
- how many false positives?
- how many true negatives?
- how many false negatives?
- what is the precision?
- what is the recall?
- what is the specificity?
- what is the F1 score where relevant?
- which types of errors are best detected?
- which types of errors are missed?
- which healthy responses trigger the signal artificially?
- which scores appear around the `0.5` threshold?
- are some families clearly more difficult?

## Intended progression

Move from:

```text
the pipeline works
```

to:

```text
we are beginning to understand
the actual behavior of MET-003
```

EXP-002 must not modify EXP-001.

---

# EXP-003 — Calibration, threshold, and robustness of MET-003

**Status:** `PLANNED`

## Main question

> **Can the MET-003 decision threshold be calibrated reproducibly, and to what extent does the signal remain robust when certain conditions change that should not substantially alter the factual phenomenon being observed?**

## Why this question?

The `0.5` threshold used in EXP-001 was frozen for that experiment.

It has not been demonstrated to be optimal.

EXP-003 must examine this boundary.

## Secondary questions

- is `0.5` a relevant threshold?
- is there a better precision / recall trade-off?
- what happens around the threshold?
- do results change with paraphrasing?
- with response length?
- with the judge model?
- with particular formulations?
- do the same cases remain comparable across repeated runs?
- is there a zone where abstention would be preferable?

## Possible variables

```text
threshold
judge
paraphrase
length
style
difficulty
repetition
```

## Methodological principle

The data used to calibrate a threshold must not be the same data used to measure its final performance.

```text
CALIBRATION
↓
VALIDATION
↓
FROZEN FINAL TEST
```

EXP-002 and EXP-003 may potentially be partially combined if this separation can be strictly preserved.

---

# EXP-004 — Validation of inter-repetition stability

**Status:** `PLANNED`

## Main question

> **When the same situation is executed repeatedly, do NeoMundi measurements allow the stability, variability, and behavioral changes between responses to be characterized reproducibly?**

## Why this question?

Repetition makes it possible to observe not only:

```text
what a system answers
```

but also:

```text
how its behavior varies
when the same thing is asked again
```

## Secondary questions

- do the responses reach the same conclusion?
- do they use the same facts?
- do they give the same numbers?
- do they mention the same entities?
- do some contradict one another?
- do multiple semantic clusters appear?
- what is the intra-prompt dispersion?
- what is the inter-prompt dispersion?
- can a response be stable but false?
- can a response be variable but correct?
- which variations are normal?
- which variations are significant?

## Dimensions to distinguish

```text
lexical stability
semantic stability
factual stability
decision stability
instruction-compliance stability
```

EXP-004 should help determine what the concept of stability can actually support as an interpretation.

---

# EXP-005 — Validation of coherence

**Status:** `PLANNED`

## Main question

> **Do NeoMundi signals associated with coherence respond correctly and reproducibly when known contradictions are introduced within a response or across multiple responses?**

## Why this question?

Coherence is not factuality.

```text
coherent but false
```

is not equivalent to:

```text
true but incoherent
```

Instruction compliance is yet another distinct dimension.

## Possible control cases

- explicit contradiction;
- implicit contradiction;
- referent shift;
- incompatible negation;
- conclusion incompatible with the arguments;
- contradiction between two sentences;
- contradiction across repeated responses;
- coherent but factually false response;
- factually correct but logically incoherent response.

## Secondary questions

- is local coherence correctly detected?
- is global coherence correctly detected?
- is inter-repetition coherence correctly measured?
- are implicit contradictions detected?
- does coherence remain independent from factuality?
- does coherence remain independent from compliance?

Principle:

```text
FALSE but COHERENT
≠
TRUE but INCOHERENT
```

---

# EXP-006 — Sensitivity of ΔG, variation, and associated signals

**Status:** `PLANNED`

## Main question

> **Do NeoMundi variation metrics, ΔG, and associated signals respond in the expected direction when controlled perturbations are applied, while remaining sufficiently stable when changes occur that should not alter the phenomenon being measured?**

## Why this question?

A useful metric should:

```text
move when the target phenomenon changes
```

but also:

```text
remain sufficiently stable
when an irrelevant variable changes
```

A constant value is not automatically a good metric.

A value that changes all the time is not either.

## Possible controlled perturbations

- factuality;
- contradiction;
- amount of information;
- instruction compliance;
- length;
- paraphrase;
- artificial latency;
- density;
- argumentative structure;
- runtime components.

## Secondary questions

- does the metric move in the expected direction?
- is there a dose-response relationship?
- does a stronger degradation produce a stronger signal?
- does it remain stable under an equivalent paraphrase?
- does it react artificially to length?
- to latency?
- are there saturation effects?
- quasi-constant branches?
- which nuisance variables influence the scores?
- do some metrics mix several phenomena?

## Possible methods

```text
sensitivity tests
monotonicity tests
ablation tests
saturation tests
controlled perturbations
```

---

# EXP-007 — Incremental value of NeoMundi

**Status:** `PLANNED`

## Main question

> **Do NeoMundi signals provide measurable information beyond simpler baselines, and does that information improve certain detections or decisions?**

## Why this question?

Demonstrating that a measurement works does not automatically demonstrate that it adds value.

The question must be asked:

> **Do we learn something from NeoMundi that we would not have obtained as easily otherwise?**

## Possible comparisons

```text
simple baseline
vs
NeoMundi
```

then potentially:

```text
simple baseline
vs
NeoMundi
vs
baseline + NeoMundi
```

## Examples of baselines

- simple factuality;
- semantic similarity;
- deterministic rule;
- classical drift;
- runtime rules;
- standard classifier;
- judge model alone.

## Secondary questions

- does NeoMundi improve precision?
- does it improve recall?
- does it reduce some false negatives?
- does it reduce some false positives?
- does it detect anomalies invisible to the baseline?
- does it provide earlier detection?
- does it improve a decision?
- does it provide complementary rather than redundant information?
- in which cases does it provide no improvement?

Intended transition:

```text
NeoMundi measures something
```

toward:

```text
In this specific context,
the NeoMundi measurement provides
observable incremental information.
```

A result such as:

```text
NeoMundi does not outperform the baseline
on this task
```

is also a useful scientific result and should be preserved.

---

# EXP-008 — Replication, longitudinal analysis, and predictive value

**Status:** `PLANNED`

## Main question

> **Can the results obtained in previous experiments be reproduced across other models, campaigns, environments, and over time, ideally with the involvement of an independent third party?**

## Longitudinal and predictive question

> **Do variations or drifts measured by NeoMundi precede, accompany, or reproducibly help explain a subsequent observable degradation?**

## Why this question?

A result observed once may be real but local.

To understand its validity domain, it must be tested elsewhere and over time.

## Replication dimensions

The conclusions may be tested on:

- another model;
- another provider;
- another campaign;
- another period;
- another prompt family;
- another environment;
- another judge;
- another language;
- another team.

## Longitudinal dimension

It will notably be necessary to distinguish:

```text
point variation
break
trend
plateau
recovery
drift
```

## Secondary questions

- do the conclusions hold across several models?
- across several providers?
- across several weeks or months?
- after a model update?
- in another environment?
- with another judge?
- can a third party reproduce part of the experiment?
- do results depend strongly on the NeoMundi configuration?
- do some drifts precede an increase in errors?
- a quality regression?
- an increase in costs?
- decision instability?
- increased need for human review?
- which changes trigger revalidation?

## Independent replication

An external person or team should progressively be able to:

```text
receive the protocol
↓
receive the necessary artifacts
↓
replay a subset
↓
recalculate the results
↓
document any differences
```

EXP-008 may therefore become a family of replications and longitudinal experiments rather than a single experiment.

---

# Summary view EXP-001 → EXP-008

```text
EXP-001
Does the experimental pipeline work?
        ✅
        ↓

EXP-002
Does MET-003 actually detect its target event
on more difficult cases?
        ↓

EXP-003
Can MET-003 be calibrated
and its robustness verified?
        ↓

EXP-004
Can stability and variability
be measured correctly?
        ↓

EXP-005
Can coherence
be measured correctly?
        ↓

EXP-006
Do the other metrics actually respond
to the phenomena they claim to measure?
        ↓

EXP-007
Does NeoMundi provide additional information
compared with simpler baselines?
        ↓

EXP-008
Can the results be reproduced elsewhere,
over time, and do some signals
have predictive value?
```

---

# “7-year-old” version

## EXP-001

> **Does our thermometer switch on and give the right answer on a few very easy things?**

```text
YES — completed
```

## EXP-002

> **Does it still work when we give it many more things and they become harder?**

## EXP-003

> **Where should we put the marks on the thermometer, and does it still give roughly the same measurement when conditions change a little?**

## EXP-004

> **If we ask an AI the same question several times, can we measure whether it stays the same or starts changing?**

## EXP-005

> **Can we see when an AI says two things that cannot both be true together?**

## EXP-006

> **When we deliberately damage something in a response, does the needle that is supposed to measure it actually move?**

## EXP-007

> **Does our instrument teach us something that simpler tools were not already telling us?**

## EXP-008

> **If someone else performs the same experiment, with another AI or at another time, do they find the same thing — and can some changes sometimes help us see a degradation coming?**

---

# The eight questions in one line

```text
EXP-001 — Does the chain work?

EXP-002 — Does MET-003 work on a larger set of difficult cases?

EXP-003 — Can MET-003 be calibrated and made robust?

EXP-004 — Can stability across repetitions be measured correctly?

EXP-005 — Can coherence be measured correctly?

EXP-006 — Do the other metrics actually respond to the phenomena they claim to measure?

EXP-007 — Does NeoMundi provide measurable incremental value?

EXP-008 — Are the results reproducible elsewhere and over time, and do some signals have predictive value?
```

---

# What may evolve

This roadmap is not a commitment to conduct exactly eight experiments.

For example:

```text
EXP-002 + EXP-003
```

may potentially be partially combined.

```text
EXP-004
```

may require several sub-experiments.

```text
EXP-006
```

may be split across several metrics.

```text
EXP-008
```

may become a program of replications and longitudinal studies.

The order may also evolve depending on the results.

---

# What should not change

Even if the roadmap evolves, the methodological principles should remain stable:

1. define the question before the experiment;
2. define the target event;
3. define the metric;
4. define the ground truth where possible;
5. define a relevant baseline;
6. define the corpus;
7. define the success criteria;
8. separate calibration, validation, and final testing where necessary;
9. freeze the protocol before the final test;
10. execute without modifying the target after reading the results;
11. preserve positive, negative, and ambiguous results;
12. document limitations;
13. connect each conclusion to its evidence;
14. version methodological decisions;
15. progressively seek independent replication.

---

# Relationship with NeoMundi claims

The roadmap should progressively feed a claims registry.

Each claim should allow the following questions to be answered:

```text
What are we claiming?

Which phenomenon does this claim concern?

Which metric supports it?

Which experiment tests it?

Which ground truth is used?

Which baseline is used?

What is the current evidence status?

Which wording is authorized?

Which wording is prohibited?

What are the limitations?

Where is the evidence?
```

Possible statuses include:

```text
DEFINED
IMPLEMENTED
MEASURED
TESTED
CALIBRATED
COMPARED
REPLICATED
VALIDATED
HYPOTHETICAL
NOT_DEMONSTRATED
```

The objective is for no important claim to be disconnected from its evidence chain.

---

# Simplified scientific trajectory

The experiments can be grouped into four major stages.

## Stage A — Verify

```text
EXP-001
```

Question:

> Does the chain work?

## Stage B — Measure and calibrate

```text
EXP-002
EXP-003
```

Questions:

> What performance is observed?

> How should the measurement be calibrated?

## Stage C — Validate the main constructs

```text
EXP-004
EXP-005
EXP-006
```

Question:

> Are we actually measuring stability, coherence, and variation in the way we think we are?

## Stage D — Demonstrate utility and reproducibility

```text
EXP-007
EXP-008
```

Questions:

> Is it useful compared with what already exists?

> Can it be reproduced elsewhere?

> Do some measurements have longitudinal or predictive value?

---

# Target evidence level

The roadmap should progressively move NeoMundi from:

```text
operational instrument
```

to:

```text
documented instrument
```

then:

```text
tested instrument
```

then:

```text
calibrated instrument
```

then:

```text
compared instrument
```

then:

```text
reproduced instrument
```

and, only when the evidence supports it:

```text
validated instrument
for an explicitly defined scope
```

Validation should never be treated as universal by default.

---

# Relationship with NeoMundi metrology

The goal is not to demonstrate that an isolated score is “good.”

The goal is to build a measurement layer for which we progressively understand:

- what it observes;
- how it measures it;
- its sensitivity;
- its errors;
- its limitations;
- its reproducibility;
- its validity domain;
- its incremental value;
- its longitudinal behavior;
- its potential predictive value;
- its operational usefulness.

This accumulation is what progressively allows the transition from:

```text
observable signal
```

to:

```text
defensible measurement
```

---

# Roadmap status

As of August 8, 2026:

```text
EXP-001
STATUS = CLOSED
RESULT = SMOKE_TEST_TECHNICALLY_SUCCESSFUL
```

```text
EXP-002
STATUS = NOT_STARTED
```

```text
EXP-003
STATUS = PLANNED
```

```text
EXP-004
STATUS = PLANNED
```

```text
EXP-005
STATUS = PLANNED
```

```text
EXP-006
STATUS = PLANNED
```

```text
EXP-007
STATUS = PLANNED
```

```text
EXP-008
STATUS = PLANNED
```

---

# Next action

The next action is not to immediately code EXP-002.

It is to transform the question:

> **On a larger and more difficult corpus, what is the actual ability of MET-003 to distinguish responses containing a significant factual error from responses in which that event is absent?**

into a precise experimental protocol.

Recommended order:

```text
1. question
2. claim
3. target event
4. metric
5. ground truth
6. baseline
7. corpus construction
8. annotation strategy
9. calibration / validation / test
10. acceptance criteria
11. analysis plan
12. protocol
13. freeze
14. execution
15. analysis
16. human review
17. conclusion
```

---

# Resources

## Scientific protocol

[**Does AI runtime behavior constitute a distinct metrological object?**](https://zenodo.org/records/21822050)

## External methodological audit

[**Constructive and Independent Methodological Audit — Stéphane Gorius**](./external-audits/Audit_methodologique_constructif_independant_NeoMundi_Kimi_K3_v1.1.pdf)

## Working checkpoint

[**CHECKPOINT_FR.md**](./CHECKPOINT_FR.md)

---

# Roadmap status

```text
ROADMAP_VERSION = v0.1
ROADMAP_STATUS = PROVISIONAL

EXP-001 = CLOSED
EXP-002 = NEXT
EXP-003_TO_EXP-008 = PLANNED

NEXT_ACTION = DEFINE_EXP_002
```

---

# Final principle

> **We are not trying to accumulate experiments. We are trying to accumulate the evidence required to know exactly what NeoMundi measurements allow — and do not allow — us to claim.**
