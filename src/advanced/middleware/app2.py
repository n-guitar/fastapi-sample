from fastapi import FastAPI

from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# 許可するホストヘッダーを強制する
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.hkm.home"]
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
