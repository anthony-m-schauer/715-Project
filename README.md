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

These are research concepts, **not yet finalized labels or validated measurements**. Penetration and exploitable space are promising initial outcomes. Stretching and disorganization remain objectives, but changes between snapshots require validated temporal and spatial comparability. Do not combine the concepts into an unvalidated overall score.

Local density alone does not establish a low block or compact team formation. Develop and validate operational definitions, use preprocessing and feature engineering, and manually review representative and edge cases. Handle ambiguous or insufficiently observed situations explicitly, and distinguish local configurations from whole-team formations.

## Proposed analysis

The project will compare progressively richer models of attacking-action effectiveness:

1. **Event-based baseline:** Action type, ball location, and basic event attributes.
2. **Spatial model:** Baseline information plus visible defender positions, local spacing, and available space.
3. **Sequence-aware model:** Spatial information plus recent attacking events, tempo, and possession buildup.

The sequence-aware approach uses event sequences, not continuous tracking. Compare models using defensible outcomes, consistent evaluation samples where appropriate, and safeguards against data leakage. Player-level comparisons are a possible *exploratory application*, subject to adequate sample sizes.

**Important limitation:** StatsBomb 360 data provides event-time snapshots of *visible* players, not continuous tracking of every player. Any changes in defensive shape across snapshots must account for differences in visibility and cannot automatically be interpreted as the movement of the same defenders.

## Data sources

**Primary candidate source:** [StatsBomb Open Data](https://github.com/hudl/open-data), using its event and 360 JSON files where available.

| Competition | Competition ID | Season ID | Planned use |
|---|---:|---:|---|
| UEFA Euro 2020 | 55 | 43 | Candidate international-match dataset |
| FIFA World Cup 2022 | 43 | 106 | Candidate international-match dataset |
| UEFA Euro 2024 | 55 | 282 | Initial inspection and candidate main dataset |

The following original JSON files were downloaded on 2026-11-07 from the [official StatsBomb Open Data repository](https://github.com/hudl/open-data), under `data/raw/statsbomb/`. Match lists are verified; only one match per tournament has been inspected. Sizes are bytes.

| Tournament | Match list (bytes; listed matches) | Sample match | Event file (bytes) | 360 file (bytes) |
|---|---|---|---:|---:|
| Euro 2024 | [55/282.json](https://raw.githubusercontent.com/hudl/open-data/master/data/matches/55/282.json) (93,280; 51) | Portugal–Czech Republic, 3930166 | [events](https://raw.githubusercontent.com/hudl/open-data/master/data/events/3930166.json) (3,146,279) | [360](https://raw.githubusercontent.com/hudl/open-data/master/data/three-sixty/3930166.json) (7,720,490) |
| World Cup 2022 | [43/106.json](https://raw.githubusercontent.com/hudl/open-data/master/data/matches/43/106.json) (119,132; 64) | Canada–Morocco, 3857276 | [events](https://raw.githubusercontent.com/hudl/open-data/master/data/events/3857276.json) (2,811,450) | [360](https://raw.githubusercontent.com/hudl/open-data/master/data/three-sixty/3857276.json) (5,743,429) |
| Euro 2020 | [55/43.json](https://raw.githubusercontent.com/hudl/open-data/master/data/matches/55/43.json) (93,844; 51) | Ukraine–North Macedonia, 3788758 | [events](https://raw.githubusercontent.com/hudl/open-data/master/data/events/3788758.json) (2,882,230) | [360](https://raw.githubusercontent.com/hudl/open-data/master/data/three-sixty/3788758.json) (6,250,243) |

Run `python src/feasibility.py` from the project root to regenerate the summary, action coverage, and field inventory CSVs in `results/`. These samples do not establish event or 360 coverage across all 166 listed matches. The official repository asks published research to credit StatsBomb and use its logo; review its terms before sharing outputs.

Across the three inspected matches, 8,685 of 10,335 events (84.0%) join to a 360 frame, including 2,353 passes and 2,122 carries. Core inspected event and 360 fields have compatible types across the samples. Some events lack frames or locations, and visible defender counts vary. These observations support further investigation; they do not validate tactical labels or establish full-tournament data quality.

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

The project brief is `docs/CompSci 715 Project Brief.pdf`. The research state will be maintained in `docs/MEMORY.md`, and substantive work sessions will be summarized in `docs/JOURNAL.md`.

## Getting started

The project currently uses the existing shared Conda environment `cs715env`. Activate it and, if needed, install the project requirements:

```sh
conda activate cs715env
python -m pip install -r requirements.txt
```

Review potential effects on other class work before installing or changing packages in this shared environment. Requirements are unpinned until the full set has been tested together.

**Next steps:** Investigate broader coverage and representative examples, refine and validate feasible measures, and prepare the project proposal. Resolve missing dependencies when needed.
