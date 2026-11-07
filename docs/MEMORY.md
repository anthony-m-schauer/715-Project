# Project Memory

## Objective and working research question

Investigate how individual attacking actions relate to disruption of compact defensive structures in international soccer. The working question asks how actions, their locations, visible defensive configurations, and preceding possession sequences relate to penetration, stretching, space creation, and disorganization.

## Proposed disruption concepts

- **Penetration:** Move the ball or a receiver beyond defensive lines.
- **Stretching:** Draw defenders wider, deeper, or forward and reduce local compactness.
- **Space creation:** Open passing lanes, gaps, or receiving opportunities for teammates.
- **Disorganization:** Alter local defensive arrangements in ways that can be exploited.

These concepts are proposed; labels and measurements have not been finalized or validated.

Penetration and exploitable space are promising initial outcomes. Stretching and disorganization remain objectives; changes between snapshots require validation of spatial and temporal comparability. Do not combine the four concepts into an unvalidated overall score. Exact features and outcomes remain open.

## Planned data and scope

StatsBomb Open Data event and 360 JSON files are the primary candidate source. Downloaded match lists contain 51 Euro 2020 (55/43), 64 World Cup 2022 (43/106), and 51 Euro 2024 (55/282) matches. One event/360 pair per tournament is available locally; coverage across the other matches remains unverified. Source URLs and downloaded file sizes are in the README. Credit StatsBomb and review its attribution terms before sharing results.

## Proposed model comparison

1. **Event baseline:** action type, ball location, and basic event attributes.
2. **Spatial model:** baseline features plus visible defender positions, spacing, and available space.
3. **Sequence-aware model:** spatial features plus recent events, tempo, and possession buildup.

The sequence-aware model uses preceding event sequences, not continuous player tracking. Compare models using defensible outcomes, consistent evaluation samples where appropriate, and leakage safeguards. Player comparisons are exploratory and depend on sufficient samples; no improvement is established.

## Method and limitations

StatsBomb 360 provides event-time snapshots of visible players, not continuous tracking. Differences in visibility limit comparisons of defensive shape and do not establish movement of the same defenders. Assess coverage, missingness, event/360 joins, usable observations, sampling bias, and measurement validity. Prevent leakage and account for related observations in evaluation; distinguish prediction and association from causation.

Local defensive density alone does not establish a low block or compact team formation. Develop, test, and validate operational definitions; use preprocessing, feature engineering, and manual examination of representative examples and edge cases. Handle ambiguous or insufficiently observed situations explicitly and distinguish local configurations from complete formations.

## Current status

Initial data feasibility has begun: the three match lists and one event/360 pair per tournament were downloaded and inspected. Event-to-360 joins were 2,974/3,610 (82.38%), 2,873/3,388 (84.80%), and 2,838/3,337 (85.05%) for Euro 2024, World Cup 2022, and Euro 2020 samples respectively. All sampled 360 frames matched an event; 28, 29, and 23 events lacked a valid location. Mean visible defenders per frame were 9.07, 6.48, and 7.35; one World Cup frame had no visible defenders. These three matches do not establish tournament-wide coverage or representative performance. No model has been trained and no disruption labels validated.

In total, 8,685 of 10,335 events (84.0%) had matching frames, including 2,353 passes and 2,122 carries. Core inspected event and 360 field types were compatible across the three samples. The 166 listed matches are candidates, not fully inspected matches.

Event IDs join to 360 `event_uuid`; event locations, pass/carry endpoints, possession and ordering fields, and visible player locations support exploratory spatial and sequence analysis. Visibility limits prevent claims of full defensive shape, unobstructed passing lanes, or continuous defender movement. `results/feasibility_actions.csv` defines positional coverage as a valid event location, matching frame, and at least one visible defender; this is not validated usefulness for a specific measure. `results/feasibility_fields.csv` records field presence and types. The existing `cs715env` remains in use; NumPy and Requests import, while Pandas and Matplotlib are absent. The script uses the standard library.

## Open questions and next priorities

- Which disruption concepts can be measured reliably from available snapshots, and how should compact defenses and outcomes be defined?
- What are the actual tournament coverage, join rates, missingness, usable sample sizes, and source restrictions?
- What evaluation splits, metrics, and feature definitions will support a fair comparison without leakage?
- Investigate coverage across additional matches, assess visibility and sampling bias, and define feasible measurements and evaluation before finalizing the sample or methodology. Resolve missing dependencies only when needed.
