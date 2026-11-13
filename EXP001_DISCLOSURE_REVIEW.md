# EXP-001 — Historical disclosure and provenance review

**Review date:** 2026-11-13  
**Status:** documentation review; frozen experiment not modified.  
**Source:** [EXP-001 frozen run manifest](experiments/EXP-001/EXP-001_smoke_test_run_manifest.json).

## Verified disclosure in the published manifest

The historical run manifest records:
- a full external inference API URL containing a service/account path identifier;
- the configured judge model alias and evaluator-related environment variable names;
- judge temperature and response-format/parsing information;
- the experimental classification and suspect-phrase thresholds;
- a referenced private backend commit and internal implementation paths.

This is **implementation metadata exposure**, not proof of exposed credentials. No token or API secret value was identified in the inspected fields. The complete Git history, all attachments, and live configuration have **not** been exhaustively security-scanned.

## Interpretation and risk

The recorded URL identifies a historical service route/account path, not a documented bearer credential. Treat the provider and routing metadata as potentially sensitive infrastructure detail; do not infer an active endpoint or currently served model from an August 2026 record.

The experimental thresholds and settings are integral to interpreting and reproducing the frozen EXP-001 smoke test. They are not demonstrated to be scientifically calibrated, broadly valid or current in production.

A historical document's continued public availability must not be treated as permission to reuse confidential pilot content or internal infrastructure identifiers elsewhere.

## Decision and handling

**Preserve the frozen manifest unchanged.** Quiet redaction would break faithful historical provenance and would not remove prior public Git history. No claim is made here that an archived endpoint is a credential or an active exposure.

For future *new* public experiment packages, review full service/account paths and exact internal routing configuration for necessity. Use minimally sufficient provider/service descriptions, protocol configuration fingerprints and versioned references when they preserve reproducibility. Where an experiment strictly requires full configuration disclosure, consider authorized controlled access with a public redacted derivative clearly marked as such.

Follow-up verification, separate from this documentation PR:
1. Confirm whether the historical service/account path remains valid; do not publish the result if operationally sensitive.
2. Scan current public content and history for actual credentials, pilot confidential data and redundant internal routing detail.
3. Verify all current-deployment claims against authorized runtime evidence.
4. Assess any proposed removal against Git history, frozen hashes, scientific reproducibility and the publication rights of the artifacts.

See [public disclosure policy](PUBLIC_DISCLOSURE_POLICY.md) ([FR](PUBLIC_DISCLOSURE_POLICY.fr.md)).
