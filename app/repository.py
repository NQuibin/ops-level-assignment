from typing import Optional, List
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb://opslevel:opslevel123123@localhost:27017/tasks?authSource=admin')

db = client.opsLevel
tasks = db.tasks


class TasksRepository:
    def find_one(self, task_id: str) -> Optional[dict]:
        return tasks.find_one({'_id': ObjectId(task_id)})

    def find_all(self, filter_opt: Optional[dict] = None, **kwargs) -> List[dict]:
        return list(tasks.find(filter=filter_opt or {}, **kwargs))

    def insert_one(self, payload: dict) -> dict:
        tasks.insert_one(payload)
        return payload

    def replace_one(self, task_id: str, payload: dict) -> dict:
        tasks.replace_one({'_id': ObjectId(task_id)}, payload)
        payload['_id'] = ObjectId(task_id)
        return payload

    def delete_one(self, task_id: str) -> bool:
        result = tasks.delete_one({'_id': ObjectId(task_id)})
        return bool(result.deleted_count)
