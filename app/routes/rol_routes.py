from fastapi import APIRouter
from controllers.rol_controller import RolController
from models.rol_model import Rol

router = APIRouter()
rol_controller = RolController()

@router.post("/create_rol")
async def create_rol(rol: Rol):
    return rol_controller.create_rol(rol)

@router.get("/get_rol/{rol_id}", response_model=Rol)
async def get_rol(rol_id: int):
    return rol_controller.get_rol(rol_id)

@router.get("/get_roles/")
async def get_roles():
    return rol_controller.get_roles()
