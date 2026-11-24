import json


def node_items(run_data, node_name):
    if node_name not in run_data:
        return []
    items = run_data[node_name][0]["data"]["main"][0]
    return [item["json"] for item in items]

extracted = []
skipped = []

with open("data/fact_runs_raw.jsonl") as f:
    for line in f:
        run = json.loads(line)
        run_data = run["data"]["resultData"]["runData"]

        prep = node_items(run_data, "fact_prep")
        check = node_items(run_data, "fact_check")
        apply = node_items(run_data, "fact_apply")
        config = node_items(run_data, "init_config")
        blog = node_items(run_data, "check_publish_date")

        if not (len(prep) == len(check) == len(apply) == 1):
            skipped.append(run["id"])
            continue

        extracted.append({
            "execution_id": run["id"],
            "started_at": run["startedAt"],
            "client_id": config[0] ["client_id"],
            "language": config[0]["language"],
            "blog_id": blog[0]["blog_id"],
            "blog_items": len(blog),
            "forced_blog_id": config[0]["force_blog_id"],
            "draft": prep[0]["output"],
            "sources": prep[0]["facts_block"],
            "checker_raw": check[0]["text"],
            "checker_result": apply[0]["fact_check"],
            "final": apply[0]["output"],
            "review_note_html": apply[0]["fact_note_html"],
        })

with open("data/fact_items.jsonl", "w") as f:
    for item in extracted:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("extracted:", len(extracted))
print("skipped:", len(skipped), skipped)