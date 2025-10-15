from pydantic import BaseModel
from datetime import datetime

class AtributoUsuarioBaseModel(BaseModel):
    usuario_id: int
    atributo_id: int
    tipo: str       
    valor: str
    estado: str     

class AtributoUsuarioCreate(AtributoUsuarioBaseModel):
    pass

class AtributoUsuarioResponse(AtributoUsuarioBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
