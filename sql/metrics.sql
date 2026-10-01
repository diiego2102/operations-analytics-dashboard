-- One record per synthetic asset per day; all assets expect 96 intervals/day.
CREATE VIEW daily_metrics AS
SELECT day, region, SUM(expected) AS expected, SUM(received) AS received,
       SUM(invalid) AS invalid, SUM(incident) AS incidents,
       1.0 * SUM(received) / SUM(expected) AS completeness,
       CASE WHEN SUM(received)=0 THEN NULL
            ELSE 1.0 * (SUM(received)-SUM(invalid))/SUM(received) END AS validity
FROM readings GROUP BY day, region;

CREATE VIEW recent_metrics AS
SELECT region, COUNT(DISTINCT asset_id) AS assets,
       SUM(expected) AS expected, SUM(received) AS received,
       SUM(invalid) AS invalid, SUM(incident) AS incident_days,
       1.0 * SUM(received) / SUM(expected) AS completeness,
       CASE WHEN SUM(received)=0 THEN NULL
            ELSE 1.0*(SUM(received)-SUM(invalid))/SUM(received) END AS validity
FROM readings WHERE day BETWEEN '2026-09-24' AND '2026-09-30'
GROUP BY region;

CREATE VIEW provider_metrics AS
SELECT region, provider, SUM(expected) AS expected, SUM(received) AS received,
       1.0*SUM(received)/SUM(expected) AS completeness
FROM readings WHERE day BETWEEN '2026-09-24' AND '2026-09-30'
GROUP BY region, provider;
