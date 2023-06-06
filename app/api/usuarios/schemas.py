from pydantic import BaseModel, EmailStr
from typing import Optional
from app.api.produtos.schemas import Produto


class UsuarioBase(BaseModel):
    email: Optional[EmailStr] = None
    nome: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    email: EmailStr
    senha: str


class Usuario(UsuarioBase):
    id: Optional[int] = None
    ativo: bool = True
    produtos: list[Produto]

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    email: EmailStr
    senha: str


class LoginSucesso(BaseModel):
    usuario: Usuario
    access_token: str
