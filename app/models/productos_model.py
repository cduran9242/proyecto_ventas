# app/models/productos_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductoBaseModel(BaseModel):
    idProductos: int
    Codigo_prducto: str
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: int 

class ProductoCreate(ProductoBaseModel):
    pass


class ProductoResponse(ProductoBaseModel):
    IdProductos: int
    Codigo_producto: str  
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: int
    create_at: datetime
    update_at: datetime

    class Config:
        from_attributes = True
