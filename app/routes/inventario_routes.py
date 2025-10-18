# app/routes/inventario_routes.py
from fastapi import APIRouter
from app.controllers.inventario_controller import InventarioController
from app.models.inventario_model import *

router = APIRouter()
inventario_controller = InventarioController()

@router.post("/create_inventario")
async def create_inventario(inventario: InventarioCreate):
    return inventario_controller.create_inventario(inventario)

@router.get("/get_inventario/{inventario_id}", response_model=InventarioResponse)
async def get_inventario(inventario_id: int):
    return inventario_controller.get_inventario(inventario_id)

@router.get("/get_inventario_by_producto/{producto_id}")
async def get_inventario_by_producto(producto_id: int):
    return inventario_controller.get_inventario_by_producto(producto_id)

@router.get("/get_all_inventario/")
async def get_all_inventario():
    return inventario_controller.get_all_inventario()

@router.put("/update_inventario/{inventario_id}")
async def update_inventario(inventario_id: int, inventario: InventarioCreate):
    return inventario_controller.update_inventario(inventario_id, inventario)

@router.delete("/delete_inventario/{inventario_id}")
async def delete_inventario(inventario_id: int):
    return inventario_controller.delete_inventario(inventario_id)

@router.get("/get_stock_producto/{producto_id}")
async def get_stock_producto(producto_id: int):
    return inventario_controller.get_stock_total_producto(producto_id)