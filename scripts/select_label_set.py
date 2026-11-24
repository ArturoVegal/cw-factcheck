import json

CUTOFF = "2026-10-28T23:00:00"

with open("data/fact_items.jsonl") as f:
    items = [json.loads(line) for line in f]

usable = [item for item in items if item["started_at"] >= CUTOFF]

latest = {}
for item in usable:
    blog_id = item["blog_id"]
    if blog_id not in latest or item["started_at"] > latest[blog_id]["started_at"]:
        latest[blog_id] = item

articles = list(latest.values())

print("usable runs:", len(usable))
print("articles:", len(articles))

def client_code(item):
    return item["blog_id"].split("_")[0]

real_runs = [item for item in usable if not item["forced_blog_id"]]

real_per_article = {}
for item in real_runs:
    real_per_article.setdefault(item["blog_id"], []).append(item)

all_articles = {item["blog_id"] for item in usable}
no_real = sorted(all_articles - set(real_per_article))
several_real = sorted(blog_id for blog_id, runs in real_per_article.items() if len(runs) > 1)

print("clients:", len({client_code(item) for item in usable}))
print("real runs:", len(real_runs))
print("articles with several real runs:", several_real)
print("articles with no real run:", no_real)

by_client = {}
for blog_id, runs in real_per_article.items():
    run = runs[0]
    by_client.setdefault(client_code(run), []).append(run)

selected = []
while len(selected) < 30:
    for client in sorted(by_client):
        if by_client[client] and len(selected) < 30:
            selected.append(by_client[client].pop(0))

with open("data/label_set.jsonl", "w") as f:
    for item in selected:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("selected:", len(selected), "from", len({client_code(item) for item in selected}), "clients")