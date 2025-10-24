from fastapi import FastAPI
from .routes.task import router as task_router

app = FastAPI()


@app.get("/health")
def read_root():
    return {"etat": "bon"}

app.include_router(task_router, prefix="/api/v1")


