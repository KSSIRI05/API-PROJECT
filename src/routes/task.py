from fastapi import APIRouter, HTTPException
from src.models.task import Task
from src.schema.task import CreateTask,UpdateTask 

router= APIRouter()

@router.get("/api/v1/task/{id}")
async def get_task(id):
    task = await Task.get(id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"tache avec l'{id} non trouvee"
        )
    return  task

@router.get("/api/v1/tasks")
async def get_alltasks():
    tasks = await Task.find_all().to_list()
    if not tasks:
        raise HTTPException(
            status_code=404,
            detail="aucune tache est trouvee"
        )
    return tasks
        
   

@router.post("/api/v1/tasks")
async def cretae_task(data : CreateTask):
    try:
        task = Task(**data.dict())
        await task.create()
        return task
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erreur lors de la création de la tâche : {str(e)}"
        )
    

@router.put("/api/v1/task/{id}")
async def update_task(id: str ,data : UpdateTask):
    task = await Task.get(id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"tache avec l'{id} non trouvee"
        )
    try:
        for field, value in data.dict().items():
            setattr(task, field, value)
            await task.save()
        return task
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erreur lors de la moification de la tâche : {str(e)}"
        )

@router.patch("/api/v1/task/{id}")
async def patch_task(id: str ,data : UpdateTask):
    task = await Task.get(id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"tache avec l'{id} non trouvee"
        )
    try :  
        # Only update fields that were explicitly set in the request
        update_data = data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)
        await task.save()
        return task
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erreur lors de la modification de la tâche : {str(e)}"
        )

@router.delete("/api/v1/task/{id}")
async def delete_task(id):
    task = await Task.get(id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail=f"tache avec l'{id} non trouvee"
        )
    try :
        await task.delete()
        return  "suprrime"
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la supression de la tâche : {str(e)}"
        )