# app/models/estados_model.py
from pydantic import BaseModel
from datetime import datetime

class EstadoBaseModel(BaseModel):
    nombre: str
    descripcion: str

class EstadoCreate(EstadoBaseModel):
    pass

class EstadoResponse(EstadoBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True