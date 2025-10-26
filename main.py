from fastapi import FastAPI
from routes.task import router as task_router
from config.configuration import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/health")
def read_root():
    return {"etat": "bon"}

app.include_router(task_router, prefix="/api/v1")


