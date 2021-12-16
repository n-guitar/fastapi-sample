from typing import Dict

from fastapi import FastAPI

app = FastAPI()

# key:value keyがint型のみ
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
