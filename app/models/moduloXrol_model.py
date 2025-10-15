from pydantic import BaseModel
from datetime import datetime

class ModuloRolBaseModel(BaseModel):
    rol_id: int
    modulo_id: int
    estado: str 

class ModuloRolCreate(ModuloRolBaseModel):
    pass

class ModuloRolResponse(ModuloRolBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
