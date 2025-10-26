# config/database.py
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.task import Task  # modèle à enregistrer dans Beanie

async def init_db():
    client = AsyncIOMotorClient(
        "mongodb+srv://kssmohammed05_db_user:kssiri2005@cluster0.ujnawwf.mongodb.net/?retryWrites=true&w=majority"
    )
    # on sélectionne la base de données
    database = client["API-DATA"]

    # initialisation de Beanie avec la base et les modèles
    await init_beanie(database=database, document_models=[Task])
