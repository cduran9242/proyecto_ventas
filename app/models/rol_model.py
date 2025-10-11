from pydantic import BaseModel

class Rol(BaseModel):
    idRol: int =None
    nombre: str
    descripcion: str