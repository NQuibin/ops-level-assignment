from typing import List, Optional

from .repository import TasksRepository
from .models import Task, CreateUpdateTaskPayload
from .exceptions import HttpException


class TasksManager:
    def __init__(self):
        self.repository = TasksRepository()

    def _to_model(self, task: dict) -> Task:
        return Task(
            id=str(task.get('id')),
            description=task.get('description'),
            priority=task.get('priority'),
            is_active=task.get('is_active')
        )

    def get_task(self, task_id: str) -> Task:
        task = self.repository.find_one(task_id)
        if task is None:
            raise HttpException(status_code=404, message='Task not found')

        return self._to_model(task)

    def get_all_tasks(self, is_active: Optional[bool] = None) -> List[Task]:
        tasks = self.repository.find_all(None if is_active is None else {'is_active': is_active})
        return [self._to_model(task) for task in tasks]

    def create_task(self, payload: CreateUpdateTaskPayload) -> Task:
        task = self.repository.insert_one(payload.dict())
        return self._to_model(task)

    def update_task(self, task_id: str, payload: CreateUpdateTaskPayload) -> Task:
        task = self.repository.replace_one(task_id, payload.dict())
        return self._to_model(task)

    def delete_task(self, task_id: str) -> bool:
        return self.repository.delete_one(task_id)

    def get_missing_priorities(self) -> List[int]:
        tasks = self.repository.find_all({'is_active': True}, sort=[('priority', 1)])
        if not len(tasks):
            return []

        max_priority = tasks[-1].get('priority')

        priorities = [0] * max_priority
        for task in tasks:
            priorities[task.get('priority') - 1] = 1

        missing_priorities = []
        for i in range(len(priorities)):
            if not priorities[i]:
                missing_priorities.append(i + 1)
        return missing_priorities

