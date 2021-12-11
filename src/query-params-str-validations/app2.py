from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# パラメータのデフォルト値として使用し、パラメータmax_lengthを50に設定
# Noneにしておくと任意パラメータとできる
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
