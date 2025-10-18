# app/routes/atributos_routes.py
from fastapi import APIRouter
from app.controllers.atributos_controller import AtributosController
from app.models.atributos_model import *

router = APIRouter()
atributos_controller = AtributosController()

@router.post("/create_atributo")
async def create_atributo(atributo: AtributoCreate):
    return atributos_controller.create_atributo(atributo)

@router.get("/get_atributo/{atributo_id}", response_model=AtributoResponse)
async def get_atributo(atributo_id: int):
    return atributos_controller.get_atributo(atributo_id)

@router.get("/get_atributos/")
async def get_atributos():
    return atributos_controller.get_atributos()

@router.put("/update_atributo/{atributo_id}")
async def update_atributo(atributo_id: int, atributo: AtributoCreate):
    return atributos_controller.update_atributo(atributo_id, atributo)

@router.delete("/delete_atributo/{atributo_id}")
async def delete_atributo(atributo_id: int):
    return atributos_controller.delete_atributo(atributo_id)

@router.get("/get_atributos_activos/")
async def get_atributos_activos():
    return atributos_controller.get_atributos_activos()
