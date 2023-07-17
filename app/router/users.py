from fastapi import APIRouter
from app.models.base import Login
from ..controllers.users import User


def user_router() -> APIRouter:
    router = APIRouter()

    @router.post('/login', tags=['Users'])
    async def login(item: Login):
        return User(item).login()

    return router
