import json

with open("data/fact_runs_raw.jsonl") as f:
    first_run = json.loads(f.readline())

run_data = first_run["data"]["resultData"]["runData"]

for node_name, runs in run_data.items():
    main = runs[0].get("data", {}).get("main") or [[]]
    items = main[0] or []
    if len(items) == 1 and "blog_id" in items[0]["json"]:
        print(node_name)