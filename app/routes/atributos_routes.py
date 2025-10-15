from fastapi import APIRouter
from controllers.atributos_controller import AtributosController
from models.atributos_model import Atributo

router = APIRouter()
atributos_controller = AtributosController()

@router.post("/create_atributo")
async def create_atributo(atributo: Atributo):
    return atributos_controller.create_atributo(atributo)

@router.get("/get_atributo/{atributo_id}", response_model=Atributo)
async def get_atributo(atributo_id: int):
    return atributos_controller.get_atributo(atributo_id)

@router.get("/get_atributos/")
async def get_atributos():
    return atributos_controller.get_atributos()
