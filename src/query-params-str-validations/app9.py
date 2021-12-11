from fastapi import FastAPI, Query

app = FastAPI()

# List[str]の代わりに直接listを使うことも可
# app7と同じ
@app.get("/items/")
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items
