from pydantic import BaseModel
from datetime import datetime

class RolBaseModel(BaseModel):
    nombre: str
    descripcion: str
    estado_id: int = 1

class RolCreate(RolBaseModel):
    pass

class RolResponse(RolBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
