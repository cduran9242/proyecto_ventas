from fastapi import APIRouter
from app.controllers.modulos_controller import ModuloController
from app.models.modulos_model import *

router = APIRouter()
modulos_controller = ModuloController()

@router.post("/create_modulo")
async def create_modulo(modulo: ModuloCreate):
    return modulos_controller.create_modulo(modulo)

@router.get("/get_modulo/{modulo_id}", response_model=ModuloResponse)
async def get_modulo(modulo_id: int):
    return modulos_controller.get_modulo(modulo_id)

@router.get("/get_modulos/")
async def get_modulos():
    return modulos_controller.get_modulos()
