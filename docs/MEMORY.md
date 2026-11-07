# Project Memory

## Objective and working research question

Investigate how individual attacking actions relate to disruption of compact defensive structures in international soccer. The working question asks how actions, their locations, visible defensive configurations, and preceding possession sequences relate to penetration, stretching, space creation, and disorganization.

## Proposed disruption concepts

- **Penetration:** Move the ball or a receiver beyond defensive lines.
- **Stretching:** Draw defenders wider, deeper, or forward and reduce local compactness.
- **Space creation:** Open passing lanes, gaps, or receiving opportunities for teammates.
- **Disorganization:** Alter local defensive arrangements in ways that can be exploited.

These concepts are proposed; labels and measurements have not been finalized or validated.

## Planned data and scope

StatsBomb Open Data event and 360 JSON files are the primary candidate source. Proposed international tournaments are Euro 2020 (competition 55, season 43), World Cup 2022 (43, 106), and Euro 2024 (55, 282), with Euro 2024 planned for initial inspection and as a candidate main dataset. Availability and the analysis sample are unverified. Check source terms and attribution before redistribution.

## Proposed model comparison

1. **Event baseline:** action type, ball location, and basic event attributes.
2. **Spatial model:** baseline features plus visible defender positions, spacing, and available space.
3. **Sequence-aware model:** spatial features plus recent events, tempo, and possession buildup.

The intended comparison tests whether spatial and sequence context improves prediction of measurable disruption. Player comparisons are exploratory and depend on sufficient samples; no improvement is established.

## Method and limitations

StatsBomb 360 provides event-time snapshots of visible players, not continuous tracking. Differences in visibility limit comparisons of defensive shape and do not establish movement of the same defenders. Assess coverage, missingness, event/360 joins, usable observations, sampling bias, and measurement validity. Prevent leakage and account for related observations in evaluation; distinguish prediction and association from causation.

## Current status

The project is at planning and initial workspace setup. The brief, README, and agent instructions describe the intended research and directory structure. No datasets, analyses, trained models, or verified findings are documented. The existing shared `cs715env` is the current environment; initial requirements are unpinned and have not been tested together. Pandas and Matplotlib are missing from that environment.

## Open questions and next priorities

- Which disruption concepts can be measured reliably from available snapshots, and how should compact defenses and outcomes be defined?
- What are the actual tournament coverage, join rates, missingness, usable sample sizes, and source restrictions?
- What evaluation splits, metrics, and feature definitions will support a fair comparison without leakage?
- Resolve missing dependencies as needed, inspect a small event and 360 sample, document data quality and coverage, and develop feasibility evidence before finalizing methods or the sample.
