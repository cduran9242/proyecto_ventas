# app/models/productos_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductoBaseModel(BaseModel):
    Codigo_producto: str  
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: Optional[bool] = None 

class ProductoCreate(ProductoBaseModel):
    pass

class ProductoResponse(ProductoBaseModel):
    IdProductos: int
    Codigo_producto: str  
    Nombre_Producto: str
    Descripcion: str
    Categoria: str
    Unidad_medida: str
    estado: Optional[bool] = None
    created_at: datetime  
    updated_at: datetime

    class Config:
        from_attributes = True
