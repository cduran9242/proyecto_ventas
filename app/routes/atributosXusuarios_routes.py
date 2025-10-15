from fastapi import APIRouter
from controllers.atributoXusuario_controller import AtributosXUsuariosController
from models.atributosXusuarios_model import AtributosXUsuarios

router = APIRouter()
atributosXusuarios_controller = AtributosXUsuariosController()

@router.post("/create_atributo_usuario")
async def create_atributo_usuario(data: AtributosXUsuarios):
    return atributosXusuarios_controller.create_atributo_usuario(data)

@router.get("/get_atributo_usuario/{id}", response_model=AtributosXUsuarios)
async def get_atributo_usuario(id: int):
    return atributosXusuarios_controller.get_atributo_usuario(id)

@router.get("/get_atributos_usuarios/")
async def get_atributos_usuarios():
    return atributosXusuarios_controller.get_atributos_usuarios()
