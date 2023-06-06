from fastapi import APIRouter

from app.api.login.views import login_router
from app.api.produtos.views import produtos_router
from app.api.usuarios.views import usuarios_router


api_router = APIRouter()

api_router.include_router(login_router, tags=["login"])
api_router.include_router(usuarios_router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(produtos_router, prefix="/produtos", tags=["produtos"])
