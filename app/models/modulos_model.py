from pydantic import BaseModel

class Modulos(BaseModel):
    idModulos: int =None
    nombre: str
    descripcion: str