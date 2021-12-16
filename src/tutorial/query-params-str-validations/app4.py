from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# 正規表現の追加
"""
^: は、これ以降の文字で始まり、これより以前には文字はない
fixedquery: は、正確なfixedqueryを持っている。
$: で終わる場合、fixedquery以降には文字はなし
"""
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
