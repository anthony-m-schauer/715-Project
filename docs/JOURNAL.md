# Research and Development Journal

Substantial work sessions are numbered sequentially; they do not represent consecutive calendar days. Append future entries as Day 2, Day 3, and so on. Do not record dates or timestamps unless requested.

## Day 1 — Project Planning and Initial Setup

**Objective:** Establish the research direction and organize the initial workspace.

**Work completed:** Documented the working question, four proposed disruption concepts, candidate StatsBomb international tournament data, and a three-model comparison. Established the data, documentation, source, and results directories; placed the project brief in `docs/`. Added the README and agent guidance, and initialized this journal and project memory.

**Findings and decisions:** The concepts and model design remain proposals, not validated measurements or findings. Event-time 360 snapshots have visibility limits and do not provide continuous tracking. Dataset coverage and feasibility remain unverified.

**Verification:** The initial directory structure was inspected after setup, and the moved brief's SHA-256 hash matched its original. The current documentation and workspace were reviewed for this entry.

**Git setup:** Initialized Git on `main`, configured the GitHub repository as `origin`, added Python, environment, secret, temporary-file, and dataset ignore rules, and retained empty project directories with placeholders. Added the repository link to the README. Git status and representative ignore rules were checked; repository ownership was corrected for the Windows account after a sandbox ownership warning. No Git user name or email was configured, and no commit or push was made.

**Dependency setup:** Selected the existing shared `cs715env` and added unpinned requirements for initial data inspection and visualization. NumPy 2.5.3 and Requests 2.34.2 imported successfully under Python 3.12.14; Pandas and Matplotlib were absent. The complete dependency set and its compatibility remain unverified. Documented activation, installation, and shared-environment precautions; no packages were installed or changed.

**Next steps:** Resolve missing dependencies as needed; inspect a small sample of event and 360 files; assess joins, coverage, missingness, and usable observations; and use that evidence to refine measurable outcomes and the analysis plan. No data download, analysis, or model training is documented.
