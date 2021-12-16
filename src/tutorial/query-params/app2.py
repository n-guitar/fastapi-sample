from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# Optionalを使うことで必須ではなくNoneを許す任意パラメータにできる
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
