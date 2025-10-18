# app/routes/estados_routes.py
from fastapi import APIRouter
from app.controllers.estados_controller import EstadosController
from app.models.estados_model import *

router = APIRouter()
estados_controller = EstadosController()

@router.post("/create_estado")
async def create_estado(estado: EstadoCreate):
    return estados_controller.create_estado(estado)

@router.get("/get_estado/{estado_id}", response_model=EstadoResponse)
async def get_estado(estado_id: int):
    return estados_controller.get_estado(estado_id)

@router.get("/get_estados/")
async def get_estados():
    return estados_controller.get_estados()

@router.put("/update_estado/{estado_id}")
async def update_estado(estado_id: int, estado: EstadoCreate):
    return estados_controller.update_estado(estado_id, estado)

@router.delete("/delete_estado/{estado_id}")
async def delete_estado(estado_id: int):
    return estados_controller.delete_estado(estado_id)