"""
Tests for Items API endpoints.
"""

import pytest
from fastapi.testclient import TestClient

from generaltemplate.main import app

client = TestClient(app)


class TestItemsAPI:
    """Tests for Items CRUD endpoints."""

    def test_list_items(self):
        """Test listing all items."""
        response = client.get("/api/items")
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 2  # We have 2 default items

    def test_get_item_by_id(self):
        """Test getting a specific item by ID."""
        response = client.get("/api/items/1")
        assert response.status_code == 200

        data = response.json()
        assert data["id"] == 1
        assert "name" in data
        assert "price" in data

    def test_get_nonexistent_item(self):
        """Test getting an item that doesn't exist."""
        response = client.get("/api/items/99999")
        assert response.status_code == 404

        data = response.json()
        assert "detail" in data

    def test_create_item(self):
        """Test creating a new item."""
        new_item = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": 49.99,
            "is_available": True,
        }

        response = client.post("/api/items", json=new_item)
        assert response.status_code == 201

        data = response.json()
        assert "id" in data
        assert data["name"] == new_item["name"]
        assert data["price"] == new_item["price"]

    def test_create_item_validation(self):
        """Test item creation with invalid data."""
        invalid_item = {
            "name": "",  # Empty name should fail
            "price": -10,  # Negative price should fail
        }

        response = client.post("/api/items", json=invalid_item)
        assert response.status_code == 422  # Validation error

    def test_update_item(self):
        """Test updating an existing item."""
        # First create an item
        new_item = {
            "name": "Update Test",
            "price": 29.99,
        }
        create_response = client.post("/api/items", json=new_item)
        item_id = create_response.json()["id"]

        # Now update it
        update_data = {
            "name": "Updated Name",
            "price": 39.99,
        }
        response = client.put(f"/api/items/{item_id}", json=update_data)
        assert response.status_code == 200

        data = response.json()
        assert data["name"] == update_data["name"]
        assert data["price"] == update_data["price"]

    def test_update_nonexistent_item(self):
        """Test updating an item that doesn't exist."""
        update_data = {"name": "Updated Name"}
        response = client.put("/api/items/99999", json=update_data)
        assert response.status_code == 404

    def test_delete_item(self):
        """Test deleting an item."""
        # First create an item
        new_item = {
            "name": "Delete Test",
            "price": 19.99,
        }
        create_response = client.post("/api/items", json=new_item)
        item_id = create_response.json()["id"]

        # Now delete it
        response = client.delete(f"/api/items/{item_id}")
        assert response.status_code == 204

        # Verify it's deleted
        get_response = client.get(f"/api/items/{item_id}")
        assert get_response.status_code == 404

    def test_delete_nonexistent_item(self):
        """Test deleting an item that doesn't exist."""
        response = client.delete("/api/items/99999")
        assert response.status_code == 404

    def test_list_items_pagination(self):
        """Test items list pagination."""
        response = client.get("/api/items?skip=0&limit=1")
        assert response.status_code == 200

        data = response.json()
        assert len(data) <= 1
