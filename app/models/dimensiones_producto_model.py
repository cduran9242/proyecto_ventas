# app/models/dimensiones_producto_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DimensionesProductoBaseModel(BaseModel):
    IdProducto: int
    Ancho: Optional[float] = None
    Espesor: Optional[float] = None
    Diametro_Interno: Optional[float] = None
    Diametro_Externo: Optional[float] = None

class DimensionesProductoCreate(DimensionesProductoBaseModel):
    pass

class DimensionesProductoResponse(DimensionesProductoBaseModel):
    IdDimensiones: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
