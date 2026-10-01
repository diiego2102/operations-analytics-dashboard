# Validation · portfolio v0.1.0

Executed on 1 October 2026:

- `python pipeline.py`: 10,800 unique asset-days generated; 120 assets over 90 days.
- `python -m unittest discover -s tests -v`: 3 tests passed. Independent fixture validates a weighted 200/300 completeness rate and 190/200 validity rate, not an average of percentages. Constraint tests reject duplicate keys and invalid counts. The injected outage is deterministic.
- Canonical artifact validation and self-contained HTML packaging passed. Embedded data matches `artifact.json`.
- Browser verification was **structural only**: no compatible installed Chromium was available. Chart SVG extraction, filter interactions and visual layout were not verified in this environment. Semantic chart tables remain readable without JavaScript.

No production source, causal comparison or machine-learning anomaly detector is claimed. Provider and regional comparisons are descriptive synthetic examples. The HTML is a reviewed fixed export; running the pipeline regenerates CSV, SQLite and canonical JSON, not the presentation runtime.
