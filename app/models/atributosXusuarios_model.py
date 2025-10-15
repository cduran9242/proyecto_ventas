from pydantic import BaseModel
from datetime import datetime

class AtributoUsuarioBaseModel(BaseModel):
    usuario_id: int
    atributo_id: int
    tipo: str       # texto, numero, booleano, fecha, json
    valor: str
    estado: str     # 'Activo' o 'Inactivo'

class AtributoUsuarioCreate(AtributoUsuarioBaseModel):
    pass

class AtributoUsuarioResponse(AtributoUsuarioBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
