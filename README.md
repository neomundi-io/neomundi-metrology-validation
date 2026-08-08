[Français](README.FR.md) | **English**

## Current status

### First validation step completed — EXP-001

NeoMundi has completed its first controlled metrology smoke test.

Think of it like testing a thermometer with water whose temperature is already known.

We prepared 20 simple cases:

- 10 containing a known factual error;
- 10 containing no factual error.

The correct answers were hidden from NeoMundi.

NeoMundi measured the 20 cases independently.

Then the results were compared with:

1. the frozen ground truth;
2. an independent deterministic baseline;
3. a human post-run review.

For this controlled smoke test:

- 20 / 20 cases produced a measurement;
- 0 computation errors;
- 0 unavailable signals;
- 10 true positives;
- 10 true negatives;
- 0 false positives;
- 0 false negatives.

This does **not** mean that MET-003 is scientifically validated or that NeoMundi has 100% performance in general.

It means something simpler and more important at this stage:

> **the experimental chain works, is traceable, and can now be tested on harder and larger datasets.**

The next validation stage will be conducted as a new versioned experiment rather than modifying EXP-001 retrospectively.
