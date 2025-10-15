from fastapi import APIRouter
from app.controllers.moduloXrol_controller import ModuloRolController
from app.models.moduloXrol_model import *

router = APIRouter()
moduloXrol_controller = ModuloRolController()

@router.post("/create_modulo_rol")
async def create_modulo_rol(data: ModuloRolCreate):
    return moduloXrol_controller.create_modulo_rol(data)

@router.get("/get_modulo_rol/{id}", response_model=ModuloRolResponse)
async def get_modulo_rol(id: int):
    return moduloXrol_controller.get_modulo_rol(id)

@router.get("/get_modulos_roles/")
async def get_modulos_roles():
    return moduloXrol_controller.get_modulos_roles()
