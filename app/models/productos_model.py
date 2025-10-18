from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductoBaseModel(BaseModel):
    idProductos: int = 1
    Codigo_prducto: str
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: int

class ProductoCreate(ProductoBaseModel):
    pass

class ProductoUpdate(ProductoBaseModel):
    pass

class ProductoResponse(ProductoBaseModel):
    idProductos: int = 1
    Codigo_prducto: str
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: int
    Fecha_creacion: datetime
    Fecha_update: datetime

    class Config:
        orm_mode = True
