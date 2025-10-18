# app/routes/moduloXrol_routes.py
from fastapi import APIRouter
from app.controllers.moduloXrol_controller import ModuloXrolController
from app.models.moduloXrol_model import *

router = APIRouter()
moduloXrol_controller = ModuloXrolController()

@router.post("/create_modulo_rol")
async def create_modulo_rol(modulo_rol: ModuloXrolCreate):
    return moduloXrol_controller.create_modulo_rol(modulo_rol)

@router.get("/get_modulo_rol/{modulo_rol_id}", response_model=ModuloXrolResponse)
async def get_modulo_rol(modulo_rol_id: int):
    return moduloXrol_controller.get_modulo_rol(modulo_rol_id)

@router.get("/get_modulos_by_rol/{rol_id}")
async def get_modulos_by_rol(rol_id: int):
    return moduloXrol_controller.get_modulos_by_rol(rol_id)

@router.get("/get_roles_by_modulo/{modulo_id}")
async def get_roles_by_modulo(modulo_id: int):
    return moduloXrol_controller.get_roles_by_modulo(modulo_id)

@router.get("/get_moduloXrol/")
async def get_moduloXrol():
    return moduloXrol_controller.get_moduloXrol()

@router.put("/update_modulo_rol/{modulo_rol_id}")
async def update_modulo_rol(modulo_rol_id: int, modulo_rol: ModuloXrolCreate):
    return moduloXrol_controller.update_modulo_rol(modulo_rol_id, modulo_rol)

@router.delete("/delete_modulo_rol/{modulo_rol_id}")
async def delete_modulo_rol(modulo_rol_id: int):
    return moduloXrol_controller.delete_modulo_rol(modulo_rol_id)