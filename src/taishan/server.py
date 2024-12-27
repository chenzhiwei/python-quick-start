import os
from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.authentication import AuthenticationMiddleware

from taishan.auth import AuthBackend

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)
app.add_middleware(
    AuthenticationMiddleware,
    AuthBackend(),
)


@app.get("/")
def read_root():
    return {"msg": "Hello world!"}


@app.get("/redirect")
def read_redirect():
    return RedirectResponse("/static/", 302)


@app.get("/redirect/")
def read_redirectf():
    return RedirectResponse("/static/", 302)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def run():
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.mount("/static", StaticFiles(directory=static_dir), "static")
    uvicorn.run(app=app, host="", port=8080)
