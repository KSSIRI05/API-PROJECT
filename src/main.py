from fastapi import FastAPI, HTTPException
from src.routes.task import router as task_router
from src.config.configuration import init_db, check_db_connection

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/health")
async def health():
    if await check_db_connection():
        return {"etat": "bon", "mongodb": "connecté"}
    raise HTTPException(status_code=503, detail="Connexion MongoDB échouée")

app.include_router(task_router)


