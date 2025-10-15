from fastapi import APIRouter
from controllers.modulos_controller import ModulosController
from models.modulos_model import Modulo

router = APIRouter()
modulos_controller = ModulosController()

@router.post("/create_modulo")
async def create_modulo(modulo: Modulo):
    return modulos_controller.create_modulo(modulo)

@router.get("/get_modulo/{modulo_id}", response_model=Modulo)
async def get_modulo(modulo_id: int):
    return modulos_controller.get_modulo(modulo_id)

@router.get("/get_modulos/")
async def get_modulos():
    return modulos_controller.get_modulos()
