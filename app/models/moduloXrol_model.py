# app/models/moduloXrol_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ModuloXrolBaseModel(BaseModel):
    rol_id: int
    modulo_id: int
    permisos: Optional[str] = None  
    estado_id: int = 1 

class ModuloXrolCreate(ModuloXrolBaseModel):
    pass

class ModuloXrolResponse(ModuloXrolBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True