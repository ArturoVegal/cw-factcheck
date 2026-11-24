# Labelling rules

Applies to `data/flags.csv` (precision) and the recall sample (later).
Judge against the sources **as stored in the execution** (`sources` in
`data/label_set.jsonl`), never the live website: it may have changed since.

## What counts as evidence
- **Supported** = traceable to a **website quote** or the **intake text**.
- A brief line counts only if it is labelled as coming from one of those
  ("Van de website" / "Uit het intakeformulier") **and** you can find it there.
- Other brief lines are **not** evidence: the topic suggester has put facts
  into briefs that the website does not contain (GF93).

## Verdict (one per row)
| Verdict | Use when | Reason codes |
|---|---|---|
| `unsupported` | a specific claim about company, products, market, people, health or numbers that the evidence does not back | `invented` / `exaggerated` / `wrong_number` |
| `supported` | the evidence backs it | `in_sources` |
| `out_of_scope` | not a factual claim in the six categories (advice, opinion, transition) | `common_knowledge` / `not_a_claim` |
| `unclear` | cannot decide from the evidence: always write a note | — |

For precision: `unsupported` = checker right; `supported` and `out_of_scope`
= false alarm; `unclear` is left out of the score but counted.

## Other columns
- **Shortenings:** judge only the part that was **removed**.
- **Too-wide cut:** if an edit removes an invented claim plus a supported part,
  the verdict is `unsupported` (the checker was right) and the note says `over_cut`.
- **`edit_ok`** (`applied` rows only): `yes` if the sentence is still correct
  after the cut, `no` if the grammar broke.
- **`note`:** required for every `unclear` and every borderline call.

## Examples
Illustrative, to be replaced with real ones from the first labelling session.
- `unsupported` / `invented`: "We deliver within 48 hours." The website
  mentions no delivery time.
- `unsupported` / `wrong_number`: "Over 500 projects completed." The website
  says 300.
- `supported` / `in_sources`: "Showroom in Ridderkerk." Literally on the website.
- `out_of_scope` / `common_knowledge`: "Concrete tiles last longer than
  wooden decking." General, not about the client.
- `out_of_scope` / `not_a_claim`: "Read on to find out which suits you best."

## Consistency checks
- A few days after labelling, re-label 20 random rows without looking at the
  first labels. More than ~3 differences means the rules need sharpening.
- More than ~10% `unclear` means the same: tighten the rules rather than
  using the escape hatch.

## Recall sample (to do)
10 of the 30 drafts: label **every** claim in the six categories, whether the
checker flagged it or not.