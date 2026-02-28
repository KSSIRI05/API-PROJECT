# config/database.py
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.models.task import Task  # modèle à enregistrer dans Beanie
import os

from dotenv import load_dotenv
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI,serverSelectionTimeoutMS=60000)  # 60 secondes au lieu de 30
    # on sélectionne la base de données
    database = client["API-DATA"]
    
    # initialisation de Beanie avec la base et les modèles
    await init_beanie(database=database, document_models=[Task])
