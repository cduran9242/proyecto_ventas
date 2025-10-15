from pydantic import BaseModel
from datetime import datetime

class AtributoBaseModel(BaseModel):
    nombre: str
    tipo_dato: str    
    descripcion: str
    es_requerido: bool
    estado: str        

class AtributoCreate(AtributoBaseModel):
    pass

class AtributoResponse(AtributoBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
