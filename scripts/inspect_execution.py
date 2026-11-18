import os
import sys
import httpx

base_url = os.environ["N8N_BASE_URL"]
api_key = os.environ["N8N_API_KEY"]
execution_id = sys.argv[1]

response = httpx.get(
    f"{base_url}/api/v1/executions/{execution_id}",
    headers={"X-N8N-API-KEY": api_key},
    params={"includeData": True},
)

response.raise_for_status()
execution = response.json()

run_data = execution["data"]["resultData"]["runData"]
for node_name in run_data:
    print(node_name)