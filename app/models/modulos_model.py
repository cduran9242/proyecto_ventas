# app/models/modulos_model.py
from pydantic import BaseModel
from datetime import datetime

class ModuloBaseModel(BaseModel):
    nombre: str
    descripcion: str
    ruta: str
    estado_id: int = 1 

class ModuloCreate(ModuloBaseModel):
    pass

class ModuloResponse(ModuloBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True