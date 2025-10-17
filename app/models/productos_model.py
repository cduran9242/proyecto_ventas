from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    activo: Optional[bool] = True

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id_producto: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
