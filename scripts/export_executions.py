import os
import httpx

base_url = os.environ["N8N_BASE_URL"]
api_key = os.environ["N8N_API_KEY"]

response = httpx.get(
    f"{base_url}/api/v1/executions",
    headers={"X-N8N-API-KEY": api_key},
    params={"workflowId": "iVREGcd6wltugaC7", "limit": 5},
)
response.raise_for_status()

for execution in response.json()["data"]:
    print(execution["id"], execution["status"], execution["startedAt"])