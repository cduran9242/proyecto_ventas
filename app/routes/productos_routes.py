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