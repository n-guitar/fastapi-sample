from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

# 複数クエリー
# 値のリストを受け取る
@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
