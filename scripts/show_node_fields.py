import json

with open("data/fact_runs_raw.jsonl") as f:
    first_run = json.loads(f.readline())

run_data = first_run["data"]["resultData"]["runData"]

for node_name in ["fact_prep", "fact_check", "fact_apply"]:
        output = run_data[node_name][0]["data"]["main"][0][0]["json"]
        for field, value in output.items():
            print(node_name, field, type(value).__name__, len(str(value)))