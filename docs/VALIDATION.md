# Validation · portfolio v0.1.0

Executed on 1 October 2026:

- `python pipeline.py`: 10,800 unique asset-days generated; 120 assets over 90 days.
- `python -m unittest discover -s tests -v`: 3 tests passed. Independent fixture validates a weighted 200/300 completeness rate and 190/200 validity rate, not an average of percentages. Constraint tests reject duplicate keys and invalid counts. The injected outage is deterministic.
- Canonical artifact validation and self-contained HTML packaging passed. Embedded data matches `artifact.json`.
- Browser verification was **structural only**: no compatible installed Chromium was available. Chart SVG extraction, filter interactions and visual layout were not verified in this environment. Semantic chart tables remain readable without JavaScript.

No production source, causal comparison or machine-learning anomaly detector is claimed. Provider and regional comparisons are descriptive synthetic examples. The HTML is a reviewed fixed export; running the pipeline regenerates CSV, SQLite and canonical JSON, not the presentation runtime.

## Portfolio v0.2.0

Five tests pass, including embedded export parity and rejection of deliberately changed data. The live GitHub Pages demo was visually inspected in Chrome. Selecting South changes monitored assets from 120 to 40, flagged asset-days from 308 to 100, and the queue from 308 to 100 records; restoring All restores the aggregate. A screenshot is included in the README. The canonical export remains a fixed snapshot; a changed artifact needs the external canonical authoring exporter via `--renderer`. Default generation verifies parity and fails on stale presentation data.
