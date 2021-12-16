from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# metaデータの追加
# https://code-server-python-8000.hkm.home/openapi.json
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
