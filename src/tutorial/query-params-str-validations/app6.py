from fastapi import FastAPI, Query

app = FastAPI()

# ...はpythonの特殊な単一値
# https://docs.python.org/3/library/constants.html#Ellipsis
# 必須値にする場合に使う
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
