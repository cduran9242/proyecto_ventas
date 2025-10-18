# app/routes/productos_routes.py
from fastapi import APIRouter
from app.controllers.producto_controller import ProductoController
from app.models.productos_model import *

router = APIRouter()
producto_controller = ProductoController()

@router.post("/create_producto")
async def create_producto(producto: ProductoCreate):
    return producto_controller.create_producto(producto)

@router.get("/get_producto/{producto_id}", response_model=ProductoResponse)
async def get_producto(producto_id: int):
    return producto_controller.get_producto(producto_id)

@router.get("/get_productos/")
async def get_productos():
    return producto_controller.get_productos()

@router.put("/update_producto/{producto_id}")
async def update_producto(producto_id: int, producto: ProductoCreate):
    return producto_controller.update_producto(producto_id, producto)

@router.delete("/delete_producto/{producto_id}")
async def delete_producto(producto_id: int):
    return producto_controller.delete_producto(producto_id)

@router.get("/get_producto_by_codigo/{codigo_producto}")
async def get_producto_by_codigo(codigo_producto: str):
    return producto_controller.get_producto_by_codigo(codigo_producto)