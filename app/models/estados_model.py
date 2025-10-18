from pydantic import BaseModel
from datetime import datetime

class AtributoBaseModel(BaseModel):
    nombre: str
    descripcion: str
           

class AtributoCreate(AtributoBaseModel):
    pass

class AtributoResponse(AtributoBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
