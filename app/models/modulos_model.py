from pydantic import BaseModel
from datetime import datetime

class ModuloBaseModel(BaseModel):
    nombre: str
    descripcion: str
    ruta: str
    estado: str 

class ModuloCreate(ModuloBaseModel):
    pass

class ModuloResponse(ModuloBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
