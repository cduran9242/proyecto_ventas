from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBaseModel(BaseModel):
    nombres: str
    apellidos: str
    email: EmailStr
    telefono: str
    cedula: str
    contrasena: str
    rol_id: int
    estado_id: int = 1  

class UsuarioCreate(UsuarioBaseModel):
    pass

class UsuarioResponse(BaseModel):
    id: int
    nombres: str
    apellidos: str
    email: EmailStr
    telefono: str
    cedula: str
    rol_id: int
    estado_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
