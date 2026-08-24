import pytest
from httpx import AsyncClient
from app.models.users import User

@pytest.mark.asyncio
async def test_register_user_success(client: AsyncClient):
    user_data = {
        "name": "newUser",
        "username": "newUsername",
        "email": "newuser@example.com",
        "password": "strongpassword123"
    }
    
    response = await client.post("/api/users", json = user_data)
    
    assert response.status_code == 201
    assert response.json()["email"] == "newuser@example.com"
    
    user_in_db = await User.find_one(User.email == "newuser@example.com")
    assert user_in_db is not None

@pytest.mark.asyncio
async def test_login_user_success(client: AsyncClient, test_user):
    test_user.password = "hashed_version_of_password"
    await test_user.save()
    
    login_data = {
        "username": "testuser@example.com",
        "password": "strongpassword123"
    }
    
    response = await client.post("/api/auth/login", data = login_data)
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

@pytest.mark.asyncio
async def test_login_user_invalid_credentials(client: AsyncClient, test_user):
    login_data = {
        "username": "testuser@example.com",
        "password": "wrongpassword"
    }
    
    response = await client.post("/api/auth/login", data = login_data)
    
    assert response.status_code == 401
