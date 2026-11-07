# Agent Instructions — CS715 Soccer Research Project

## 1. Project and authority
- This repository supports a machine learning research project on how individual attacking actions disrupt compact defensive structures in international soccer.
- The research considers penetration, defensive stretching, space creation, and disorganization. These are research concepts, not yet validated measurements.
- The project owner makes research and scope decisions. Agents implement assigned tasks, investigate evidence, and raise questions or concerns; they do not independently redefine the project.
- The project brief `docs/CompSci 715 Project Brief.pdf` provides fuller research context. Distinguish proposed methods from findings confirmed with data.

## 2. Repository orientation
- `README.md`: project overview, setup information, and data sources/provenance.
- `docs/MEMORY.md`: current accepted decisions, findings, limitations, and unresolved questions.
- `docs/JOURNAL.md`: concise chronological summaries of substantive work, including unsuccessful or abandoned approaches.
- `data/raw/`: original downloaded source files; `data/interim/`: intermediate transformations; `data/processed/`: analysis-ready datasets.
- `src/`: Python scripts and reusable code; `results/`: generated figures, tables, and other research outputs.
- At the start of a **new agent conversation**, read this file, `docs/MEMORY.md`, and the recent relevant entries in `docs/JOURNAL.md`. Consult the README, project brief, and code as needed for the task. Do not reread everything before every message in an ongoing conversation.

## 3. Scope, preparation, and approval
- Before a substantial change, inspect relevant existing files and prior decisions. Identify the requested outcome, affected components, and how completion will be checked.
- For nontrivial or multi-file tasks, use a short plan or checklist. Check the actual requirements rather than implementing only the first plausible or easiest interpretation.
- Carry out normal implementation decisions within the assigned scope. Do not add unrelated features, infrastructure, or documentation.
- Ask for approval before changing the research question, accepted definitions or methodology, canonical data sources, or existing validated results; also ask before destructive operations or significant restructuring.
- Preserve unrelated work. Do not make Git commits or rewrite history unless explicitly requested.

## 4. Data integrity and provenance
- Treat existing files in `data/raw/` as immutable: do not edit, overwrite, or delete them. New source downloads may be added there with distinct names.
- Store cleaning and transformations in `data/interim/` or `data/processed/`. Keep the processing steps reproducible from the original data.
- Document important dataset sources, URLs, dates accessed/downloaded, versions or coverage, and known restrictions in the README. Record checksums when useful for verifying original files.
- Never invent, silently substitute, or misrepresent data, labels, measurements, sources, or citations. Report missing or unusable data plainly.

## 5. Development and analytical practice
- The project currently uses the existing shared Conda environment `cs715env`. Consult and maintain `requirements.txt` as project dependencies change; justify additions with actual project needs.
- Verify dependency changes and their potential effects on other class work in the shared environment. Suggest appropriate dependency updates rather than silently changing the environment.
- Prefer clear, maintainable Python that fits the task and existing project conventions. Avoid unnecessary abstractions, dependencies, or scaffolding.
- Keep exploratory code and provisional outputs distinguishable from accepted implementations and findings. Do not silently replace validated work with an unverified experiment.
- Consider data quality, missingness, sampling bias, reproducibility, and train/test leakage whenever relevant. Do not confuse association, prediction, and causation.
- For positional snapshots, do not claim continuous tracking or individual defender movement without evidence. Account for incomplete visibility when interpreting defensive structure.
- Validate tactical definitions with representative examples and edge cases; do not infer a low block from local density alone, and explicitly handle ambiguous or insufficiently observed situations.
- When exploring alternatives, record meaningful failures and limitations rather than hiding them.

## 6. Verification and completeness
- After making code or data-processing changes, run appropriate available checks and inspect their actual outputs. Verify important counts, joins, assumptions, and sample records when relevant.
- For ML experiments, document evaluation setup and metrics; preserve seeds, splits, and parameters when needed for reproducibility. Avoid evaluating closely related observations as though they were independent.
- Before finishing, compare the result against every part of the assigned task. Review the relevant existing implementation for missed dependencies, edge cases, or oversimplifications.
- Report what changed, what was tested, the observed outcome, and what remains uncertain or incomplete. Never state that a check passed unless it was performed.

## 7. Memory, journal, and handoff
- Append a short numbered work-session summary to `docs/JOURNAL.md` after a substantive session (Day 1, Day 2, etc.; these are sessions, not calendar days): goal, meaningful changes or experiments, validation/results, issues or rejected attempts, and next steps. Do not record dates or timestamps unless requested, or log every command or trivial edit.
- Update `docs/MEMORY.md` when an important decision, verified finding, limitation, or project status changes. Keep it concise and current; do not promote hypotheses to facts.
- Preserve useful history in the journal even when an approach is abandoned. If prior notes conflict with new evidence, flag the conflict and seek resolution rather than silently replacing conclusions.
- End substantive tasks with a clear handoff suitable for the project owner and a future fresh agent session.
- The course requires honest disclosure of material AI assistance in the final report; do not obscure AI contributions. A separate AI-usage log is not required.

## 8. Skills and process improvement
- Check for relevant existing project skills when a task calls for a repeatable procedure; follow them where applicable.
- Suggest creating or revising a skill when a workflow recurs or would benefit from a consistent checklist (for example, dataset intake or model evaluation). Do not create skills without approval.
- Propose changes to these instructions when a recurring failure or new project need justifies them; do not expand the rules speculatively.
