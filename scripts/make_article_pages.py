import html
import json
from pathlib import Path

out_dir = Path("data/articles")
out_dir.mkdir(exist_ok=True)

with open("data/label_set.jsonl") as f:
    items = [json.loads(line) for line in f]

for number, item in enumerate(items, start=1):
    page = (
        "<meta charset='utf-8'>"
        f"<h1>{number}. {item['blog_id']}</h1>"
        "<h2>Sources (evidence)</h2>"
        f"<pre style='white-space: pre-wrap'>{html.escape(item['sources'])}</pre>"
        "<h2>Draft (before the check)</h2>"
        f"{item['draft']}"
        "<h2>Final (after the check)</h2>"
        f"{item['final']}"
    )
    path = out_dir / f"{number:02d}_{item['blog_id']}.html"
    path.write_text(page, encoding="utf-8")

print("wrote", len(items), "files to", out_dir)