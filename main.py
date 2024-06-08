from unittest.mock import Base
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

# get path
@app.get("/")
def read_root():
    return {"Hello": "World"}

# uvicorn main:app --reload to run or fastapi dev main.py - this one's better

# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
# must be inputed into cmd terminal
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    


# inserting '/docs#/' at the end of the url will show you document of your file, as well give access to a .Json file 
    

