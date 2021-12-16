# staticは実利用するときに実施としスキップする
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
