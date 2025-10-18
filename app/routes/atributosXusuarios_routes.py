# app/routes/atributosXusuarios_routes.py
from fastapi import APIRouter
from app.controllers.atributosXusuarios_controller import AtributosXusuariosController
from app.models.atributosXusuarios_model import *

router = APIRouter()
atributosXusuarios_controller = AtributosXusuariosController()

@router.post("/create_atributo_usuario")
async def create_atributo_usuario(atributo_usuario: AtributoXUsuarioCreate):
    return atributosXusuarios_controller.create_atributo_usuario(atributo_usuario)

@router.get("/get_atributo_usuario/{atributo_usuario_id}", response_model=AtributoXUsuarioResponse)
async def get_atributo_usuario(atributo_usuario_id: int):
    return atributosXusuarios_controller.get_atributo_usuario(atributo_usuario_id)

@router.get("/get_atributos_by_usuario/{usuario_id}")
async def get_atributos_by_usuario(usuario_id: int):
    return atributosXusuarios_controller.get_atributos_by_usuario(usuario_id)

@router.get("/get_atributosXusuarios/")
async def get_atributosXusuarios():
    return atributosXusuarios_controller.get_atributosXusuarios()

@router.put("/update_atributo_usuario/{atributo_usuario_id}")
async def update_atributo_usuario(atributo_usuario_id: int, atributo_usuario: AtributoXUsuarioCreate):
    return atributosXusuarios_controller.update_atributo_usuario(atributo_usuario_id, atributo_usuario)

@router.delete("/delete_atributo_usuario/{atributo_usuario_id}")
async def delete_atributo_usuario(atributo_usuario_id: int):
    return atributosXusuarios_controller.delete_atributo_usuario(atributo_usuario_id)
