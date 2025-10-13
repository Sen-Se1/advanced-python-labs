from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# =============================================================================
# 1. FASTAPI SETUP AND BASIC ROUTE
# =============================================================================
print("=" * 50)
print("FASTAPI TUTORIAL - TODO LIST APPLICATION")
print("=" * 50)

# Create FastAPI app instance
app = FastAPI(title="Todo API", version="1.0.0")

# In-memory storage for items
items = []

# =============================================================================
# 2. BASIC ROUTES
# =============================================================================

@app.get("/")
def root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to Todo API", "status": "running"}

# =============================================================================
# 3. PYDANTIC MODELS
# =============================================================================

class Item(BaseModel):
    """Pydantic model for Todo items"""
    text: str  # Required field
    is_done: bool = False  # Optional field with default

class ItemResponse(BaseModel):
    """Response model for items including ID"""
    id: int
    text: str
    is_done: bool

# =============================================================================
# 4. TODO LIST ENDPOINTS
# =============================================================================

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    """Create a new todo item"""
    item_id = len(items)
    item_data = item.dict()
    item_data["id"] = item_id
    items.append(item_data)
    print(f"✅ Item created: {item_data}")
    return item_data

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """Get a specific todo item by ID"""
    if item_id < len(items):
        print(f"✅ Retrieved item {item_id}: {items[item_id]}")
        return items[item_id]
    else:
        error_msg = f"Item {item_id} not found"
        print(f"❌ {error_msg}")
        raise HTTPException(status_code=404, detail=error_msg)

@app.get("/items/", response_model=List[ItemResponse])
def list_items(limit: int = 10):
    """List todo items with optional limit"""
    result = items[:limit]
    print(f"✅ Listed {len(result)} items (limit: {limit})")
    return result

# =============================================================================
# 5. ADDITIONAL ENDPOINTS
# =============================================================================

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    """Update an existing todo item"""
    if item_id >= len(items):
        error_msg = f"Item {item_id} not found"
        print(f"❌ {error_msg}")
        raise HTTPException(status_code=404, detail=error_msg)
    
    items[item_id].update(item.dict())
    items[item_id]["id"] = item_id  # Ensure ID remains consistent
    print(f"✅ Updated item {item_id}: {items[item_id]}")
    return items[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete a todo item"""
    if item_id >= len(items):
        error_msg = f"Item {item_id} not found"
        print(f"❌ {error_msg}")
        raise HTTPException(status_code=404, detail=error_msg)
    
    deleted_item = items.pop(item_id)
    # Reindex remaining items
    for i in range(item_id, len(items)):
        items[i]["id"] = i
    
    print(f"✅ Deleted item {item_id}: {deleted_item}")
    return {"message": f"Item {item_id} deleted successfully", "deleted_item": deleted_item}

@app.get("/items/count")
def get_items_count():
    """Get the total count of todo items"""
    count = len(items)
    print(f"✅ Total items count: {count}")
    return {"total_items": count}

# =============================================================================
# 6. SERVER STARTUP
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("🚀 Starting FastAPI Server...")
    print("📚 Interactive Docs: http://127.0.0.1:8000/docs")
    print("📚 Alternative Docs: http://127.0.0.1:8000/redoc")
    print("="*50)
    uvicorn.run(app, host="127.0.0.1", port=8000)