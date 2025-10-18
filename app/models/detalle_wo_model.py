# app/models/detalle_wo_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DetalleWoBaseModel(BaseModel):
    IdWo: int
    IdPedido: Optional[int] = None
    IdProducto: int
    Cantidad_Solicitada: float
    Cantidad_Producida: Optional[float] = None

class DetalleWoCreate(DetalleWoBaseModel):
    pass

class DetalleWoResponse(DetalleWoBaseModel):
    Id_Detalle_WO: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
