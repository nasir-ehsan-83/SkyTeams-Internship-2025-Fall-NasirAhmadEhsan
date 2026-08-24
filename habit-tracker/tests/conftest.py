# tests/conftest.py
import pytest
import pytest_asyncio
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.main import app
from app.models.habits import Habit
from app.models.users import User
from app.core.jwt import create_access_token
from app.config.config import settings

# ============ فقط این بخش را تغییر دهید ============

@pytest_asyncio.fixture(scope="session", autouse=True)
async def initialize_test_db():
    """ساده‌ترین راه‌حل: استفاده از MongoDB بدون احراز هویت برای تست"""
    
    # 1. اتصال به MongoDB محلی بدون احراز هویت
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    
    # 2. پاک کردن دیتابیس تست
    await client.drop_database(settings.DATABASE_NAME_TEST)
    
    # 3. راه‌اندازی Beanie
    await init_beanie(
        database=client[settings.DATABASE_NAME_TEST],
        document_models=[Habit, User]
    )
    
    yield
    
    # 4. پاک کردن دیتابیس بعد از تست
    await client.drop_database(settings.DATABASE_NAME_TEST)
    client.close()

# ============ بقیه کدها مثل قبل ============

@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_collections():
    yield
    await Habit.find_all().delete()
    await User.find_all().delete()

@pytest_asyncio.fixture(scope="function")
async def client():
    async with AsyncClient(app=app, base_url="http://test/api") as ac:
        yield ac

@pytest_asyncio.fixture(scope="function")
async def test_user():
    user = User(
        username="testuser",
        email="testuser@example.com",
        password="fakehashedpassword",
        role="user"
    )
    await user.insert()
    return user

@pytest_asyncio.fixture(scope="function")
async def auth_client(client, test_user):
    token_data = {
        "id": str(test_user.id), 
        "role": test_user.role
    }
    token = await create_access_token(token_data)
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client