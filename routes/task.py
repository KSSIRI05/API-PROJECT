from fastapi import APIRouter
from APIproject.models.task import Task
from APIproject.schema.task import CreateTask,UpdateTask 

router= APIRouter()

@router.get("/api/v1/task/{id}")
async def get_task(id):
    task = await Task.get(id)
    return  task

@router.get("/api/v1/tasks")
async def get_alltasks():
    tasks = await Task.find_all().to_list()
    return tasks

@router.post("/api/v1/tasks")
async def cretae_task(data : CreateTask):
    task = Task(**data.dict())
    await task.create()
    return task

@router.put("/api/v1/task/{id}")
async def update_task(id: str ,data : UpdateTask):
    task = await Task.get(id)
    for field, value in data.dict().items():
        setattr(task, field, value)
    return task

@router.patch("/api/v1/task/{id}")
async def patch_task(id: str ,data : UpdateTask):
    task = await Task.get(id)
    for field, value in data.dict().items():
        setattr(task, field, value)
    return task

@router.delete("/api/v1/task/{id}")
async def delete_task(id):
    task = await Task.get(id)
    await task.delete
    return  "suprrime"