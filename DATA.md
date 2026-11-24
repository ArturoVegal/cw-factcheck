# Dataset

## Source
Executions of the n8n writer workflow CONT_CREATION_PREVIEW_LIB
(`iVREGcd6wltugaC7`), exported through the n8n public API on 18 Nov 2026
with `scripts/export_executions.py`.

n8n keeps about 30 days of execution history. The runs from 28 Oct expire
around 27 Nov 2026, so after that the raw export is the only copy.

All times are UTC, as n8n stores them (Amsterdam = UTC+1).

## Files (in `data/`, git-ignored: they contain client text)
- `fact_runs_raw.jsonl`: the 132 full executions in which `fact_check` ran
  (126 MB). Never edited; re-extract from it if a field is missing.
- `fact_items.jsonl`: one small record per run, made by
  `scripts/extract_fact_items.py`: execution id, start time, client, article
  (`blog_id`), language, test marker, draft, sources, the model's raw answer,
  what `fact_apply` did, the final text and the review note.

## Counts (`scripts/dataset_stats.py`, 24 Nov 2026)
| | |
|---|---|
| Runs with a fact check | 132 |
| Production runs (nightly) | 46 |
| Forced test runs (`force_blog_id` filled) | 86 |
| Different clients | 22 |
| Different articles | 50 |
| Model answers that failed to parse | 0 |
| Edits proposed by the model | 805 (about 6 per article) |
| Applied automatically | 597 (74%) |
| Sent to human review | 208 (26%) |

## Which runs to use
- **Grading the model (Phase 3):** only runs from 28 Oct 23:00 UTC onwards
  (29 Oct 00:00 Amsterdam): 117 runs. The 15 earlier runs (10018–10032)
  were build tests that may have used prompt versions 1–2, which were
  replaced as far too aggressive. The prompt has not changed since
  (change logs; confirmed by Arturo).
- **Reproducing `fact_apply` (Phase 2):** its rules changed twice: on
  30 Oct (key-point fix) and on 2 Nov around 11:15 UTC (two guards on
  shortening sentence endings). Compare each run with the rules that were
  live at the time, or use only runs after 2 Nov.
- **Test runs:** forced runs are valid examples (the checker cannot tell a
  test from production), but the same article was often run several times.
  Label one run per article: the latest.

## How the article id was verified
`blog_inputs` lists all of a client's upcoming articles, so its first row is
not the article written. The id comes from `check_publish_date`, which passes
on only the article that is due. Check: in all 86 forced runs, that id equals
`force_blog_id` (0 mismatches).