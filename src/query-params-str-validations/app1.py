from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# app2でバリデーションを追加する
@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
