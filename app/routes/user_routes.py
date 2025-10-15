from fastapi import APIRouter
from controllers.user_controller import UserController
from models.user_model import User

router = APIRouter()
user_controller = UserController()

@router.post("/create_user")
async def create_user(user: User):
    return user_controller.create_user(user)

@router.get("/get_user/{user_id}", response_model=User)
async def get_user(user_id: int):
    return user_controller.get_user(user_id)

@router.get("/get_users/")
async def get_users():
    return user_controller.get_users()
