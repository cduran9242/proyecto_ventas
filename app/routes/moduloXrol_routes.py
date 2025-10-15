from fastapi import APIRouter
from controllers.moduloXrol_controller import ModuloXRolController
from models.moduloXrol_model import ModuloXRol

router = APIRouter()
moduloXrol_controller = ModuloXRolController()

@router.post("/create_modulo_rol")
async def create_modulo_rol(data: ModuloXRol):
    return moduloXrol_controller.create_modulo_rol(data)

@router.get("/get_modulo_rol/{id}", response_model=ModuloXRol)
async def get_modulo_rol(id: int):
    return moduloXrol_controller.get_modulo_rol(id)

@router.get("/get_modulos_roles/")
async def get_modulos_roles():
    return moduloXrol_controller.get_modulos_roles()
