from typing import Optional

from fastapi import FastAPI, Response, status

from .manager import TasksManager
from .models import CreateUpdateTaskPayload

app = FastAPI()
manager = TasksManager()


@app.get('/v1/items')
def get_tasks(is_active: Optional[bool] = None):
    return manager.get_all_tasks(is_active)


@app.get('/v1/tasks/{task_id}')
def get_task(task_id: str):
    return manager.get_task(task_id)


@app.post('/v1/tasks')
def create_task(payload: CreateUpdateTaskPayload, response: Response):
    task = manager.create_task(payload)
    response.status_code = status.HTTP_201_CREATED
    return task


@app.put('/v1/tasks/{task_id}')
def update_task(task_id: str, payload: CreateUpdateTaskPayload):
    return manager.update_task(task_id, payload)


@app.delete('/v1/tasks/{task_id}')
def delete_task(task_id: str, response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT
    return manager.delete_task(task_id)


@app.get('/v1/items/missing-priorities')
def get_missing_priorities():
    return manager.get_missing_priorities()
