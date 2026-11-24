# LEARNING 

## 2026-11-17 - Phase 0: decisions and repo skeleton 

**What I built:** Private repo with a scr layout, pyproject.toml, a venv, a .gitignore that keeps client data and secrets out, and one passing test. 

**Decisions:**
- Repo: private, on my personal GitHub for now; transfer once the IP question is settled.
- Host: none for Phases 0-3. Host and payer get decided when Phase 4 starts (after 4 dec).
- Model: gpt-5.1 pinned to gpt-5.1-2025-11-13, today's prompt, all node settings copied exactly. 
- Export: top priority this weeek, hard deadline 24 Nov (n8n history expires around 27 Nov).

## 2026-11-18 — Phase 1: export

**What I built:** pagination in the export script (323 executions,
oldest 19 Oct); a filter for runs where fact_check ran (132, first one
28 Oct 16:53); raw export to data/fact_runs_raw.jsonl (126 MB);
inspect_execution.py to list the node names of one run.

**Changed method:** explain + do-along first, practice separately.

**Risk found:** daytime bursts of runs on 28 Oct, 30 Oct, 2 Nov and 9 Nov
are probably test runs, possibly with older prompt versions. Check before
labelling. Back up data/ to a CW-owned location.
