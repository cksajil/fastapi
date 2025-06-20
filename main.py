from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/to_upper")
def to_upper(text: str):
    """Convert a query parameter 'text' to upper case."""
    return {"original": text, "upper": text.upper()}
