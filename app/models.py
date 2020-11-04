from pydantic import BaseModel


class Task(BaseModel):
    id: str
    description: str
    priority: int
    is_active: bool


class CreateUpdateTaskPayload(BaseModel):
    description: str
    priority: int
    is_active: bool
