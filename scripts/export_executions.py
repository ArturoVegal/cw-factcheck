import os
import httpx

base_url = os.environ["N8N_BASE_URL"]
api_key = os.environ["N8N_API_KEY"]

all_executions = []
cursor = None

while True:
    params = {"workflowId": "iVREGcd6wltugaC7", "limit": 100}
    if cursor:
        params["cursor"] = cursor

    response = httpx.get(
        f"{base_url}/api/v1/executions",
        headers={"X-N8N-API-KEY": api_key},
        params=params,
    )
    response.raise_for_status()
    page = response.json()
    all_executions.extend(page["data"])
    print("fetched", len(page["data"]), "- total so far", len(all_executions))

    cursor = page.get("nextCursor")
    if not cursor:
        break

print("total executions", len(all_executions))
dates = [execution["startedAt"] for execution in all_executions]
print("oldest:", min(dates))
print("newest:", max(dates))