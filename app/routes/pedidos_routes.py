# app/routes/pedidos_routes.py
from fastapi import APIRouter
from app.controllers.pedidos_controller import PedidosController
from app.models.pedidos_model import *

router = APIRouter()
pedidos_controller = PedidosController()

# ========== ENCABEZADO PEDIDOS ==========
@router.post("/create_encabezado_pedido")
async def create_encabezado_pedido(encabezado: EncabezadoPedidoCreate):
    return pedidos_controller.create_encabezado_pedido(encabezado)

@router.get("/get_encabezado_pedido/{pedido_id}", response_model=EncabezadoPedidoResponse)
async def get_encabezado_pedido(pedido_id: int):
    return pedidos_controller.get_encabezado_pedido(pedido_id)

@router.get("/get_encabezados_pedidos/")
async def get_encabezados_pedidos():
    return pedidos_controller.get_encabezados_pedidos()

@router.put("/update_encabezado_pedido/{pedido_id}")
async def update_encabezado_pedido(pedido_id: int, encabezado: EncabezadoPedidoCreate):
    return pedidos_controller.update_encabezado_pedido(pedido_id, encabezado)

@router.delete("/delete_encabezado_pedido/{pedido_id}")
async def delete_encabezado_pedido(pedido_id: int):
    return pedidos_controller.delete_encabezado_pedido(pedido_id)

# ========== DETALLE PEDIDOS ==========
@router.post("/create_detalle_pedido")
async def create_detalle_pedido(detalle: DetallePedidoCreate):
    return pedidos_controller.create_detalle_pedido(detalle)

@router.get("/get_detalles_pedido/{pedido_id}")
async def get_detalles_pedido(pedido_id: int):
    return pedidos_controller.get_detalles_pedido(pedido_id)

@router.get("/get_detalle_pedido/{detalle_id}", response_model=DetallePedidoResponse)
async def get_detalle_pedido(detalle_id: int):
    return pedidos_controller.get_detalle_pedido(detalle_id)

@router.put("/update_detalle_pedido/{detalle_id}")
async def update_detalle_pedido(detalle_id: int, detalle: DetallePedidoCreate):
    return pedidos_controller.update_detalle_pedido(detalle_id, detalle)

@router.delete("/delete_detalle_pedido/{detalle_id}")
async def delete_detalle_pedido(detalle_id: int):
    return pedidos_controller.delete_detalle_pedido(detalle_id)

# ========== PEDIDOS COMPLETOS ==========
@router.get("/get_pedido_completo/{pedido_id}")
async def get_pedido_completo(pedido_id: int):
    return pedidos_controller.get_pedido_completo(pedido_id)

@router.get("/get_pedidos_by_vendedor/{vendedor_id}")
async def get_pedidos_by_vendedor(vendedor_id: int):
    return pedidos_controller.get_pedidos_by_vendedor(vendedor_id)

@router.get("/get_pedidos_by_cliente/{cliente_id}")
async def get_pedidos_by_cliente(cliente_id: int):
    return pedidos_controller.get_pedidos_by_cliente(cliente_id)