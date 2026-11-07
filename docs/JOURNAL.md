# Research and Development Journal

Substantial work sessions are numbered sequentially; they do not represent consecutive calendar days. Append future entries as Day 2, Day 3, and so on. Do not record dates or timestamps unless requested.

## Day 1 — Project Planning and Initial Setup

**Objective:** Establish the research direction and organize the initial workspace.

**Work completed:** Documented the working question, four proposed disruption concepts, candidate StatsBomb international tournament data, and a three-model comparison. Established the data, documentation, source, and results directories; placed the project brief in `docs/`. Added the README and agent guidance, and initialized this journal and project memory.

**Findings and decisions:** The concepts and model design remain proposals, not validated measurements or findings. Event-time 360 snapshots have visibility limits and do not provide continuous tracking. Dataset coverage and feasibility remain unverified.

**Verification:** The initial directory structure was inspected after setup, and the moved brief's SHA-256 hash matched its original. The current documentation and workspace were reviewed for this entry.

**Git setup:** Initialized Git on `main`, configured the GitHub repository as `origin`, added Python, environment, secret, temporary-file, and dataset ignore rules, and retained empty project directories with placeholders. Added the repository link to the README. Git status and representative ignore rules were checked; repository ownership was corrected for the Windows account after a sandbox ownership warning. No Git user name or email was configured, and no commit or push was made.

**Dependency setup:** Selected the existing shared `cs715env` and added unpinned requirements for initial data inspection and visualization. NumPy 2.5.3 and Requests 2.34.2 imported successfully under Python 3.12.14; Pandas and Matplotlib were absent. The complete dependency set and its compatibility remain unverified. Documented activation, installation, and shared-environment precautions; no packages were installed or changed.

**Feasibility investigation:** Retrieved three official tournament match lists and one event/360 pair per tournament, then created and ran a standard-library inspection script and three CSV summaries. Lists contained 51, 64, and 51 matches; sample event-to-frame joins covered 82.38%, 84.80%, and 85.05% respectively. Every sampled frame joined an event, but some events lacked locations and visible defender counts varied. Raw-file hashes matched the values recorded at download. The VS Code terminal displayed the `cs715env` prompt; the environment's NumPy and Requests imported, while Pandas and Matplotlib were absent. No package installation or models were needed. Three matches are insufficient to establish tournament-wide coverage or validate disruption measures.

**Research refinements:** Reviewed the feasibility summaries and synchronized the research documentation around validated tactical definitions, manual review, explicit ambiguity, separate disruption outcomes, and leakage-aware model comparisons. Across the samples, 8,685 of 10,335 events had matching frames, including 2,353 passes and 2,122 carries. Local density alone does not establish a low block, and changing snapshot visibility limits defensive interpretation. The requested editable brief replacement remains outstanding because the required DOCX rendering tools were unavailable; the original PDF was retained.

**Next steps:** Assess broader match and visibility coverage, review representative cases, refine and validate measures and evaluation, and prepare the proposal. No model training or disruption labels have been produced.
