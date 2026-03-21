"""
Items API router - Example CRUD endpoints.

This is a template router showing common patterns for REST APIs.
Customize this for your actual use case.
"""

from typing import List

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()


class Item(BaseModel):
    """Item model - example domain object."""

    id: int = Field(..., description="Unique identifier")
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: str | None = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be positive)")
    is_available: bool = Field(default=True, description="Whether item is available")


class ItemCreate(BaseModel):
    """Item creation model - excludes auto-generated fields."""

    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    is_available: bool = Field(default=True)


class ItemUpdate(BaseModel):
    """Item update model - all fields optional."""

    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float | None = Field(None, gt=0)
    is_available: bool | None = None


# In-memory storage (replace with database in production)
items_db: dict[int, Item] = {
    1: Item(id=1, name="Example Item", description="This is an example item", price=19.99),
    2: Item(
        id=2,
        name="Another Item",
        description="Another example item",
        price=29.99,
        is_available=False,
    ),
}
next_id = 3


@router.get("/items", response_model=List[Item])
async def list_items(skip: int = 0, limit: int = 100):
    """
    List all items with pagination.

    Args:
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return

    Returns:
        List of items
    """
    items = list(items_db.values())
    return items[skip : skip + limit]


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """
    Get a specific item by ID.

    Args:
        item_id: The ID of the item to retrieve

    Returns:
        The requested item

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return items_db[item_id]


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """
    Create a new item.

    Args:
        item: The item data to create

    Returns:
        The created item with generated ID
    """
    global next_id

    new_item = Item(
        id=next_id,
        name=item.name,
        description=item.description,
        price=item.price,
        is_available=item.is_available,
    )
    items_db[next_id] = new_item
    next_id += 1

    return new_item


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    """
    Update an existing item.

    Args:
        item_id: The ID of the item to update
        item_update: The fields to update

    Returns:
        The updated item

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    existing_item = items_db[item_id]

    # Update only provided fields
    update_data = item_update.model_dump(exclude_unset=True)
    updated_item = existing_item.model_copy(update=update_data)
    items_db[item_id] = updated_item

    return updated_item


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """
    Delete an item.

    Args:
        item_id: The ID of the item to delete

    Raises:
        HTTPException: 404 if item not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    del items_db[item_id]
