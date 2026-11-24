import json

with open("data/fact_items.jsonl") as f:
    items = [json.loads(line) for line in f]

changed = [item for item in items if item["final"] != item["draft"]]
unique_drafts = {item["draft"] for item in items}

print("items:", len(items))
print("changed by fact_apply:", len(changed))
print("unique drafts:", len(unique_drafts))
print("checker_result fields:", list(items[0]["checker_result"].keys()))

parse_failed = [item for item in items if not item["checker_result"]["parse_ok"]]
proposed_total = sum(item["checker_result"]["proposed"] for item in items)
applied_total = sum(item["checker_result"]["applied_count"] for item in items)
skipped_total = sum(item["checker_result"]["skipped_count"] for item in items)

print("model answer unreadable:", len(parse_failed))
print("edits proposed:", proposed_total)
print("edits applied:", applied_total)
print("edits skipped (to review):", skipped_total)
first_applied = changed[0]["checker_result"]["applied"][0]
print("one applied edit is a:", type(first_applied).__name__)
if isinstance(first_applied, dict):
    print("with fields:", list(first_applied.keys()))

print("clients:", len({item["client_id"] for item in items}))
print("articles (blog_id):", len({item["blog_id"] for item in items}))
print("forced runs:", sum(1 for item in items if item["forced_blog_id"]))
print("max blog_inputs rows:", max(item["blog_items"] for item in items))

mismatch = [item for item in items if item["forced_blog_id"] and item["forced_blog_id"] != item["blog_id"]]
print("forced runs where blog_id differs:", len(mismatch))