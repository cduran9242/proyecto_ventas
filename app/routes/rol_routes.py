from fastapi import APIRouter, HTTPException
from controllers.rol_controller import *
from models.rol_model import Rol

router = APIRouter()

nuevo_rol = RolController()


@router.post("/create_rol")
async def create_rol(rol: Rol):
    rpta = nuevo_rol.create_user(rol)
    return rpta


@router.get("/get_rol/{rol_id}",response_model=Rol)
async def get_user(Rol_id: int):
    rpta = nuevo_rol.get_rol(Rol_id)
    return rpta

@router.get("/get_rols/")
async def get_rols():
    rpta = nuevo_rol.get_rol()
    return rpta