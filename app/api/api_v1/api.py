from fastapi import APIRouter

from app.api.api_v1.rotas import usuarios, produtos, login


api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(produtos.router, prefix="/produtos", tags=["produtos"])
