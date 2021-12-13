from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
"""
バックエンドに許可させるかどうか指定できる
クレデンシャル情報 (認証ヘッダー、Cookieなど) 
特定のHTTPメソッド (POST、PUT) またはワイルドカード "*" を使用してすべて許可
特定のHTTPヘッダー、またはワイルドカード "*"を使用してすべて許可
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
