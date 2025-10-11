from pydantic import BaseModel

class Atributos(BaseModel):
    idAtributos: int =None
    nombre: str
    descripcion: str