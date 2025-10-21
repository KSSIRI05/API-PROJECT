from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def read_root():
    return {"etat": "bon"}

@app.get("/api/v1/tasks")

