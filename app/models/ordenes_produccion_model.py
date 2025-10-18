# app/models/ordenes_produccion_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrdenProduccionBaseModel(BaseModel):
    Estado_Siguiente: Optional[str] = None
    Estado_Anterior: Optional[str] = None
    Fecha_Inicio: Optional[datetime] = None
    Fecha_Fin_Estimada: Optional[datetime] = None
    Fecha_Fin_Real: Optional[datetime] = None

class OrdenProduccionCreate(OrdenProduccionBaseModel):
    pass

class OrdenProduccionResponse(OrdenProduccionBaseModel):
    IdWo: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
