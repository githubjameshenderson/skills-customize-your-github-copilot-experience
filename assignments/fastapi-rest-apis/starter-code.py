from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Item(BaseModel):
    name: str
    description: str | None = None
    completed: bool = False


items = []


@app.get("/")
def read_root():
    # Return a welcome message for the API
    pass


@app.get("/items")
def get_items():
    # Return the list of items
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Return a single item by its ID
    pass


@app.post("/items")
def create_item(item: Item):
    # Add the item to the list and return it
    pass
