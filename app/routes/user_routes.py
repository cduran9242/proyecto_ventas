from fastapi import APIRouter
from app.controllers.user_controller import UserController
from app.models.user_model import *

router = APIRouter()
user_controller = UserController()

@router.post("/create_user")
async def create_user(user: UsuarioCreate):
    return user_controller.create_user(user)

@router.get("/get_user/{user_id}", response_model=UsuarioResponse)
async def get_user(user_id: int):
    return user_controller.get_user(user_id)

@router.get("/get_users/")
async def get_users():
    return user_controller.get_users()
