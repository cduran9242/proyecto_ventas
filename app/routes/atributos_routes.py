from fastapi import APIRouter
from app.controllers.atributos_controller import AtributoController
from app.models.atributos_model import *

router = APIRouter()
atributos_controller = AtributoController()

@router.post("/create_atributo")
async def create_atributo(atributo: AtributoCreate):
    return atributos_controller.create_atributo(atributo)

@router.get("/get_atributo/{atributo_id}", response_model=AtributoResponse)
async def get_atributo(atributo_id: int):
    return atributos_controller.get_atributo(atributo_id)

@router.get("/get_atributos/")
async def get_atributos():
    return atributos_controller.get_atributos()
