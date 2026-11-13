# Public disclosure policy — evaluator methodology and qualification

**Status:** proposed for review (2026-11-13). **Scope:** documentation and research artefacts only. This document does not attest the current production configuration.

## Purpose and boundary

NeoMundi publicly describes what each signal is intended to measure, what it cannot establish, measurement status and coverage, historical experimental conditions, calibration status and evidence that independently supports a claim. Public descriptions do **not** constitute evidence that an evaluator is scientifically validated or that a historical evaluator, model or threshold is currently deployed.

An evaluator score is not a certificate of factual truth, safety or legal compliance. Distinguish a technical smoke test, a controlled evaluation, a calibration and an independent replication.

## Disclosure classes

| Class | Appropriate examples | Publication rule |
|---|---|---|
| PUBLIC | Signal definition, direction and unit; statuses (`measured`, `not_measured`, degraded); reference methodology; aggregate limitations; dated experimental results; version/provenance schema | Publish with date, scope, demonstrated claims and non-claims |
| CONTROLLED / CASE-SPECIFIC | Pilot datasets, raw model outputs, research protocols with unreleased data, full configuration snapshots and reproducibility packs containing protected data | Confirm participant authorization, data protection and permitted redistribution first |
| PRIVATE | Credentials, tokens, internal deployment addresses, exact internal system prompts, sensitive routing settings, private datasets and non-public commercial implementation | Do not add to a public repository |

Numeric coefficients and thresholds are **not automatically secrets**. They may be essential to explain a measured value or reproduce a frozen experiment. Review their publication and rights case by case rather than deleting evidence or publishing an unverified formula. A Git commit does not become secret when removed from the default branch.

## Frozen historical artefacts

Do not retrospectively rewrite signed, hashed or frozen experimental artefacts to change their reported conditions. The `experiments/EXP-001/EXP-001_smoke_test_run_manifest.json` file is a historical record; its endpoint, configuration variable names, judge settings and thresholds **must not be represented as a current production inventory**. The recorded Infomaniak API URL contains a service/account path identifier: it is not itself an authentication key, but its full publication deserves a scoped exposure review. Any later redaction or restriction requires documenting integrity and historical provenance consequences.

For future public releases prefer provider category, service type and attested evaluator fingerprints over unnecessary full infrastructure paths. Never publish tokens or real customer material.

## Minimum evaluator disclosure

For every signal, report:
1. intended construct and observable input;
2. evaluation approach at a high level, with the difference between heuristic, embeddings and LLM-as-judge;
3. output semantics (including null/not-measured and failure modes);
4. evaluator/provenance fields actually attested, not inferred;
5. versioned calibration/qualification evidence, sample sizes, conditions and limitations;
6. dependency and non-determinism warnings, and explicit separation between historic experiments and current deployments.

Never imply that a present model or route was confirmed solely by reading historical documentation. A production-current statement requires a fresh, authorized runtime inventory.

## P0 findings (documentation review, not full secret scanning)

- The public Python SDK `docs/LIMITES.md` reproduces historical aggregation equations, coefficients and limitations from the reference implementation. Review publication necessity and historical scope before changing or republishing them.
- The public EXP-001 manifest contains a full historical inference endpoint, configuration variable names, judge temperature and experimental thresholds. Preserve the frozen record while assessing whether future releases need the full endpoint.
- The metric dictionary publishes experimental thresholds and judge response structure. Their role in reproducibility must be preserved; calibration is not thereby established.
- Evaluator provenance fingerprints may be absent for some signals; do not infer identical evaluator configurations from identical measurement version alone.

**Not established by this P0 review:** absence of credentials across all branches/history, exact current serving models, current evaluator calibration, or agreement between archived SDK examples and current production.

## Publication checklist

- [ ] Verified public/private repo visibility and exact revision
- [ ] Reviewed text, raw files, binary attachments and generated artefacts for secrets and identifying infrastructure details
- [ ] Preserved limits, null semantics and negative results
- [ ] Labeled experimental thresholds and examples with date, version and qualification status
- [ ] Checked that a current-production claim has current runtime evidence
- [ ] Checked FR/EN consistency and inbound links
- [ ] Reviewed the PR diff; no source code, prompts, production config or frozen evidence altered
