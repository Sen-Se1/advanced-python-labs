# =============================================================================
# STEP 1: INSTALL AND GET STARTED WITH FASTAPI
# =============================================================================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# =============================================================================
# STEP 2: BASIC GET ROUTE
# =============================================================================
@app.get("/")
def root():
    """Root endpoint - returns hello world"""
    return {"Hello": "World"}

# =============================================================================
# STEP 3: POST ROUTE FOR CREATING ITEMS
# =============================================================================
items = []

# @app.post("/items")
# def create_item(item: str):
#     """Create a new item using string parameter"""
#     items.append(item)
#     return item

# =============================================================================
# STEP 4: GET ROUTE FOR SPECIFIC ITEM
# =============================================================================
# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> str:
#     """Get a specific item by ID"""
#     item = items[item_id]
#     return item

# =============================================================================
# STEP 5: HANDLING HTTP ERRORS
# =============================================================================
# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> str:
#     """Get item with proper error handling"""
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# =============================================================================
# STEP 6: JSON REQUEST AND PATH PARAMETERS
# =============================================================================
# @app.get("/items/")
# def list_items(limit: int = 10):
#     """List items with limit parameter"""
#     return items[0:limit]

# =============================================================================
# STEP 7: PYDANTIC MODELS
# =============================================================================
class Item(BaseModel):
    """Pydantic model for items"""
    # text: str = None
    text: str
    is_done: bool = False

@app.post("/items/")
def create_item(item: Item):
    """Create item using Pydantic model"""
    items.append(item)
    return item

# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> Item:
#     """Get item using Pydantic model"""
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# =============================================================================
# STEP 9: RESPONSE MODELS
# =============================================================================
@app.get("/items/", response_model=List[Item])
def list_items(limit: int = 10):
    """List items with response model"""
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """Get item with response model"""
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
# =============================================================================
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI Server...")
    print("📚 Interactive Docs: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)