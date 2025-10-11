from pydantic import BaseModel

class User(BaseModel):
    id: int =None
    idRol: int
    nombre: str 
    apellido: str 
    cedula: str 
    edad: int 
    email: str
    usuario: str
    contrasena: str
    estado: str