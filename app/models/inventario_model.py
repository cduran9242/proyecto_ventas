# app/models/inventario_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InventarioBaseModel(BaseModel):
    IdProducto: int
    Lote: Optional[str] = None
    Cantidad_disponible: float

class InventarioCreate(InventarioBaseModel):
    pass

class InventarioResponse(InventarioBaseModel):
    Idinvnetario: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True