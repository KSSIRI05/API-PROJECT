from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.models.task import Task
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

_client = None  # keep reference to avoid GC

async def init_db():
    global _client
    _client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=60000)
    database = _client["API-DATA"]
    await init_beanie(database=database, document_models=[Task])

async def check_db_connection():
    client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    try:
        await client.admin.command("ping")
        return True
    except Exception:
        return False
    finally:
        client.close()