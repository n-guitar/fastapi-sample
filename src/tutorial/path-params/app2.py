from fastapi import FastAPI

app = FastAPI()

# 固定パスがある場合先に書かないと行けない
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
