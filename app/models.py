from pydantic import BaseModel, PositiveInt


class Task(BaseModel):
    id: str
    description: str
    priority: PositiveInt
    is_active: bool


class CreateUpdateTaskPayload(BaseModel):
    description: str
    priority: PositiveInt
    is_active: bool
