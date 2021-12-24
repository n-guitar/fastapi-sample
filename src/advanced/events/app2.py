from fastapi import FastAPI

app = FastAPI()

# app終了時に実行 ctr + c でも実行される
@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")

@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
