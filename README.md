# Breaking Defensive Structures

**CS715 — Programming for Machine Learning | Semester Project**

**Repository:** [GitHub](https://github.com/anthony-m-schauer/715-Project)

## Project overview

This project investigates how individual attacking actions in international soccer relate to disrupting compact defensive structures. Rather than measuring attacking value only through goals, assists, or expected goals (xG), it explores how players create the conditions for an attack to progress.

**Working research question:** How do attacking actions, their locations, visible defensive configurations, and preceding possession sequences relate to penetration, stretching, space creation, and disorganization of compact defenses?

The four forms of **defensive disruption** guide the investigation:

- **Penetration:** Moving the ball or a receiver beyond defensive lines.
- **Stretching:** Drawing defenders wider, deeper, or forward and reducing local compactness.
- **Space creation:** Opening passing lanes, gaps, or receiving opportunities for teammates.
- **Disorganization:** Altering local defensive arrangements in ways that can be exploited.

These are research concepts, **not yet finalized labels or validated measurements**. The data feasibility study will determine which can be measured reliably.

## Proposed analysis

The project will compare progressively richer models of attacking-action effectiveness:

1. **Event-based baseline:** Action type, ball location, and basic event attributes.
2. **Spatial model:** Baseline information plus visible defender positions, local spacing, and available space.
3. **Sequence-aware model:** Spatial information plus recent attacking events, tempo, and possession buildup.

The main goal is to test whether defensive context and prior actions improve predictions of measurable disruption. Player-level comparisons are a possible *exploratory application*, subject to adequate sample sizes.

**Important limitation:** StatsBomb 360 data provides event-time snapshots of *visible* players, not continuous tracking of every player. Any changes in defensive shape across snapshots must account for differences in visibility and cannot automatically be interpreted as the movement of the same defenders.

## Data sources

**Primary candidate source:** [StatsBomb Open Data](https://github.com/hudl/open-data), using its event and 360 JSON files where available.

| Competition | Competition ID | Season ID | Planned use |
|---|---:|---:|---|
| UEFA Euro 2020 | 55 | 43 | Candidate international-match dataset |
| FIFA World Cup 2022 | 43 | 106 | Candidate international-match dataset |
| UEFA Euro 2024 | 55 | 282 | Initial inspection and candidate main dataset |

These competitions are **proposed sources**, not yet a verified analysis sample. Data availability, event/360 joins, coverage, file sizes, missingness, and usable observations will be measured during feasibility work. Source download dates, relevant data issues, and any changes to the selected dataset will be documented here as the project develops. Check the source's usage terms and attribution requirements before redistributing data or outputs.

## Repository layout

```text
Project/
├── AGENTS.md           # Guidance for coding agents working in this repository
├── README.md           # Project overview and data provenance
├── docs/               # Project brief, research memory, and session journal
├── data/
│   ├── raw/            # Original downloaded data; never modify in place
│   ├── interim/        # Intermediate transformations
│   └── processed/      # Analysis-ready datasets
├── src/                # Python scripts and reusable analysis code
└── results/            # Generated tables, figures, and model outputs
```

The project brief is stored in `docs/`. The research state will be maintained in `docs/MEMORY.md`, and substantive work sessions will be summarized in `docs/JOURNAL.md`.

## Getting started

The project currently uses the existing shared Conda environment `cs715env`. Activate it and, if needed, install the project requirements:

```sh
conda activate cs715env
python -m pip install -r requirements.txt
```

Review potential effects on other class work before installing or changing packages in this shared environment. Requirements are unpinned until the full set has been tested together.

**Next steps:** Resolve missing dependencies as needed, inspect a small sample of real event and 360 files, document data quality and usable coverage, and produce the feasibility evidence for the project proposal.
