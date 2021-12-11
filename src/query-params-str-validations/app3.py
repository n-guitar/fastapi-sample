from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# minパラメータ
# 任意パラメータであるが入力した場合3文字以上
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
