from fastapi import APIRouter, HTTPException
from controllers.modulos_controller import *
from models.modulos_model import Modulos

router = APIRouter()

nuevo_modulo = ModuloController()


@router.post("/create_modulo")
async def create_modulo(modulo: Modulos):
    rpta = nuevo_modulo.create_user(modulo)
    return rpta


@router.get("/get_rol/{rol_id}",response_model=Modulos)
async def get_user(Rol_id: int):
    rpta = nuevo_modulo.get_rol(Rol_id)
    return rpta

@router.get("/get_rols/")
async def get_rols():
    rpta = nuevo_modulo.get_rol()
    return rpta