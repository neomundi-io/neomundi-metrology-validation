🇬🇧 **English version:** [README.md](./README.md) · 🇫🇷 **Version française :** [README_FR.md](./README_FR.md)

# External Audits and Methodological Contributions

This directory preserves external contributions that have participated in the methodological consolidation of the **NeoMundi Metrology Validation** program.

These contributions may notably:

- identify methodological weaknesses;
- raise validation questions;
- propose controls or experiments;
- contribute to the definition of the experimental roadmap;
- help clarify the limitations of metrics and claims;
- contribute to reproducibility and the evidence chain.

These contributions must be distinguished from scientific validation or replication.

```text
EXTERNAL CONTRIBUTION
≠
FORMAL AUDIT
≠
VALIDATION
≠
REPLICATION
```

---

## Formal audits

### Stéphane Gorius — Independent Methodological Audit

**Document:** [Independent Methodological Audit — Kimi K3](./Audit_methodologique_independant_Stéphane%20Gorius.pdf)

**Author:** Stéphane Gorius  
**Affiliation:** R&D AIzyNow  
**Version:** 1.1 final  
**Date:** July 24, 2026

The document is presented by its author as a:

> **Constructive and independent methodological audit**

It examines the public NeoMundi report dedicated to the runtime observation of Kimi K3.

The audit was conducted independently and constructively, based on the publicly accessible material available at the time of the analysis.

Its scope did not notably include full access to:

- CSV / JSON files;
- computation code;
- complete prompts;
- internal metric documentation.

This limitation is explicitly documented in the audit.

The purpose of the report is not to constitute definitive scientific validation of NeoMundi, but to identify both the solid elements of the existing framework and the methodological improvements required to move from operational instrumentation toward progressively defensible metrology.

The audit notably identifies the need to strengthen:

- operational definitions of metrics;
- construct validity;
- calibration;
- positive and negative controls;
- measurement of false positives and false negatives;
- sensitivity to known perturbations;
- analysis of repeated runs;
- separation between factuality, coherence, and compliance;
- reproducibility;
- the evidence chain;
- runtime instrumentation;
- longitudinal validation.

It notably frames the methodological progression as:

```text
operational score
↓
defined metric
↓
tested metric
↓
calibrated metric
↓
independently reproduced metric
```

Several of these recommendations have contributed to structuring the experimental roadmap of the `neomundi-metrology-validation` repository.

---

## Status of this audit

This document constitutes:

```text
EXTERNAL METHODOLOGICAL AUDIT
```

It does not constitute:

```text
SCIENTIFIC VALIDATION
```

nor:

```text
INDEPENDENT REPLICATION
```

This distinction is important.

An audit may:

- examine a method;
- identify a weakness;
- raise a question;
- propose a control;
- recommend an experiment.

Validation requires appropriate experimental data and a defined protocol.

Replication requires another person, team, or infrastructure to reproduce a result according to a documented specification.

---

## Relationship with the experimental roadmap

External methodological contributions do not directly determine NeoMundi conclusions.

They help formulate questions that should be tested.

The intended relationship is:

```text
EXTERNAL QUESTION OR CRITIQUE
        ↓
METROLOGICAL QUESTION
        ↓
EXPERIMENTAL PROTOCOL
        ↓
EXP-XXX
        ↓
RESULTS
        ↓
REVIEW
        ↓
POTENTIALLY AUTHORIZED CLAIM
```

An external recommendation therefore does not automatically become a methodological truth.

It becomes a hypothesis, question, or requirement to be tested.

---

## Other external contributions

Other researchers, engineers, practitioners, or observers may contribute to the program by providing:

- questions;
- critiques;
- objections;
- test proposals;
- baselines;
- alternative hypotheses;
- replication requests.

These contributions may be incorporated into the methodological roadmap when they help strengthen falsifiability, reproducibility, or the quality of the evidence chain.

They are attributed by name in this directory only with the explicit agreement of their author.

This rule makes it possible to clearly distinguish:

```text
external question used methodologically
```

from:

```text
officially attributed contribution
```

and from:

```text
published formal audit
```

---

## Principle

> **A useful critique is not a problem to eliminate: it can become an experiment to design.**

The purpose of this directory is to preserve the record of external contributions that participate in this transformation.
