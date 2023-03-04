from pydantic import BaseModel
from typing import Optional


class ProdutoBase(BaseModel):
    nome: str
    detalhes: Optional[str]
    preco: Optional[float]


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: Optional[int] = None
    disponivel: bool
    usuario_id: Optional[int]

    class Config:
        orm_mode = True


class ProdutoSimples(ProdutoBase):
    id: Optional[int]
    nome: str
    detalhes: Optional[str]
    preco: Optional[float]
    disponivel: bool

    class Config:
        orm_mode = True
