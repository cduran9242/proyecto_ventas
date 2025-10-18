# app/models/pedidos_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EncabezadoPedidoBaseModel(BaseModel):
    Tipo_Pedido: Optional[str] = None
    IdCliente: int
    IdVendedor: int
    Moneda: Optional[str] = None
    TRM: Optional[float] = None
    OC_Cliente: Optional[str] = None
    Condicion_pago: Optional[str] = None

class EncabezadoPedidoCreate(EncabezadoPedidoBaseModel):
    pass

class EncabezadoPedidoResponse(EncabezadoPedidoBaseModel):
    IdPedido: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class DetallePedidoBaseModel(BaseModel):
    IdPedido: int
    IdProducto: int
    Numero_Linea: Optional[int] = None
    Cantidad_solicitada: float
    Cantidad_confirmada: Optional[float] = None
    Precio_unitario: Optional[float] = None
    Precio_Total: Optional[float] = None
    Precio_Extrajero: Optional[float] = None
    Precio_Total_extrajero: Optional[float] = None
    Numero_Documento: Optional[str] = None
    Tipo_Documento: Optional[str] = None
    Estado_Siguiente: int
    Estado_Anterior: int

class DetallePedidoCreate(DetallePedidoBaseModel):
    pass

class DetallePedidoResponse(DetallePedidoBaseModel):
    IdDetalle_Pedidos: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True