from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBaseModel(BaseModel):
    nombres: str
    apellidos: str
    email: EmailStr
    telefono: str
    cedula: str
    password: str
    rol_id: int
    estado: str  # 'Activo', 'Inactivo', 'Suspendido'

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
    estado: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
