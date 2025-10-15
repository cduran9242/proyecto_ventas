from fastapi import APIRouter
from app.controllers.rol_controller import RolController
from app.models.rol_model import *

router = APIRouter()
rol_controller = RolController()

@router.post("/create_rol")
async def create_rol(rol: RolCreate):
    return rol_controller.create_rol(rol)

@router.get("/get_rol/{rol_id}", response_model=RolResponse)
async def get_rol(rol_id: int):
    return rol_controller.get_rol(rol_id)

@router.get("/get_roles/")
async def get_roles():
    return rol_controller.get_roles()
