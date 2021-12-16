from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

# 複数クエリーのdefault値
@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
