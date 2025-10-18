# app/models/atributosXusuarios_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AtributoXUsuarioBaseModel(BaseModel):
    usuario_id: int
    atributo_id: int
    tipo: str  
    valor: Optional[str] = None
    estado_id: int = 1 

class AtributoXUsuarioCreate(AtributoXUsuarioBaseModel):
    pass

class AtributoXUsuarioResponse(AtributoXUsuarioBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
