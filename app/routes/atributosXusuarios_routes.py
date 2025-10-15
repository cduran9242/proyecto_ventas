from fastapi import APIRouter
from app.controllers.atributosXusuarios_controller import AtributosXUsuariosController
from app.models.atributosXusuarios_model import *

router = APIRouter()
atributosXusuarios_controller = AtributosXUsuariosController()

@router.post("/create_atributo_usuario")
async def create_atributo_usuario(data: AtributoUsuarioCreate):
    return atributosXusuarios_controller.create_atributo_usuario(data)

@router.get("/get_atributo_usuario/{id}", response_model=AtributoUsuarioResponse)
async def get_atributo_usuario(id: int):
    return atributosXusuarios_controller.get_atributo_usuario(id)

@router.get("/get_atributos_usuarios/")
async def get_atributos_usuarios():
    return atributosXusuarios_controller.get_atributos_usuarios()
