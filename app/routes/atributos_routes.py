from fastapi import APIRouter, HTTPException
from controllers.atributos_controller import *
from models.atributos_model import Atributos

router = APIRouter()

nuevo_atributo = AtributosController()

@router.post("/create_atributo")
async def create_atributo(atributo: Atributos):
    rpta = nuevo_atributo.create_atributo(atributo)
    return rpta

@router.get("/get_rol/{rol_id}",response_model=Atributos)
async def get_user(Rol_id: int):
    rpta = nuevo_atributo.get_rol(Rol_id)
    return rpta

@router.get("/get_rols/")
async def get_rols():
    rpta = nuevo_atributo.get_rol()
    return rpta