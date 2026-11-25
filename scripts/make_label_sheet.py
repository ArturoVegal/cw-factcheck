import csv
import json

with open("data/label_set.jsonl") as f:
    items = [json.loads(line) for line in f]

rows = []
for item in items:
    result = item["checker_result"]
    for edit in result["applied"]:
        rows.append({
            "blog_id": item["blog_id"],
            "outcome": "applied",
            "mode": edit["mode"],
            "claim": edit["removed"],
            "model_reason": edit["reason"],
            "apply_note": "",
            "verdict": "",
            "reason_code": "",
            "edit_ok": "",
            "note": "",
        })

    for edit in result["skipped"]:
        rows.append({
            "blog_id": item["blog_id"],
            "outcome": "to_review",
            "mode": "",
            "claim": edit["find"],
            "model_reason": edit["reason"],
            "apply_note": edit["why"],
            "verdict": "",
            "reason_code": "",
            "edit_ok": "",
            "note": "",
        })

with open("data/flags.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
    writer.writeheader()
    writer.writerows(rows)

print("flags to label:", len(rows), "in", len(items), "articles")