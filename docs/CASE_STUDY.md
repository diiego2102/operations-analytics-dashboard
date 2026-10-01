# Operational monitoring case study

## Decision
Prioritise which assets and providers require investigation when reading coverage or validity deteriorates. The audience is an operations manager, analyst or commercial stakeholder.

## Implementation
A deterministic generator produces 10,800 asset-days. Python validates and loads SQLite; SQL views aggregate explicit counts; a portable web dashboard connects regional indicators, 90-day trends and a review queue. The unique key and interval bounds reject inconsistent records.

## Demonstrated result
The fictional final seven-day window has 120 assets, 78,099 received of 80,640 expected intervals, 96.84896% completeness, 98.62226% validity and 308 flagged asset-days. Selecting South yields 40 assets and 100 flags. An injected South/Beta outage is visible in the historical trend. These are fixture outputs, not business impact or employer metrics.

## Tradeoffs
Weighted rates prevent misleading averages. A flag requests investigation rather than diagnosing failure. Provider comparisons are descriptive, not adjusted for region or asset mix. The presentation is a reviewed static snapshot; CI checks that its embedded data and definitions match the generated artifact.

## Evidence
See `sql/metrics.sql`, independent denominator tests, export parity tests, and the live demo linked in the README. Five tests cover the supported path. No employer code or data is included.
