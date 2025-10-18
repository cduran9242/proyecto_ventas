from fastapi import APIRouter
from app.controllers.estado_controller import EstadoController
from app.schemas.estado_schema import EstadoCreate

router = APIRouter
estado_controller = EstadoController()

@router.post("/create_estado")
def crear_estado(estado: EstadoCreate):
    return estado_controller.create_estado(estado)

@router.get("/get_estado/{estado_id}")
def obtener_estado(estado_id: int):
    return estado_controller.get_estado(estado_id)

@router.get("/get_estados/")
def listar_estados():
    return estado_controller.get_estados()
