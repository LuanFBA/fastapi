from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.usuarios.schemas import Usuario
from app.api.produtos.schemas import Produto, ProdutoCreate
from app.repository.produto import RepositorioProduto
from app.api.deps import get_db, obter_usuario_logado


produtos_router = APIRouter()


@produtos_router.post("/", response_model=Produto, status_code=201)
def criar_produto_usuario(
    produto: ProdutoCreate,
    usuario: Usuario = Depends(obter_usuario_logado),
    db: Session = Depends(get_db),
):
    produto_criado = RepositorioProduto(db).criar(produto, usuario_id=usuario.id)

    return produto_criado


@produtos_router.get("/")
def listar_produtos_usuario(
    usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_db)
):
    produto_db = RepositorioProduto(db).listar_me(usuario_id=usuario.id)

    if produto_db is None:
        raise HTTPException(status_code=404, detail="Não existem produtos!")

    return produto_db


@produtos_router.get("/listar", response_model=list[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produto_db = RepositorioProduto(db).listar()

    if produto_db is None:
        raise HTTPException(status_code=404, detail="Não existem produtos!")

    return produto_db


@produtos_router.put("/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto: Produto,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    produto_db = RepositorioProduto(db).obter(id=produto_id)

    if produto_db is None:
        raise HTTPException(
            status_code=404, detail=f"Produto com id: {produto_id} não encontrado!"
        )

    if produto_db.usuario_id != usuario.id:
        raise HTTPException(status_code=400, detail="Sem permissões necessárias")

    produto_atualizado = RepositorioProduto(db).atualizar(
        id=produto_id, produto=produto
    )

    return produto_atualizado


@produtos_router.delete("/{produto_id}")
def remover_produto(
    produto_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    produto_db = RepositorioProduto(db).obter(id=produto_id)

    if produto_db is None:
        raise HTTPException(
            status_code=404, detail=f"Produto com id: {produto_id} não encontrado!"
        )

    if produto_db.usuario_id != usuario.id:
        raise HTTPException(status_code=400, detail="Sem permissões necessárias")

    produto_removido = RepositorioProduto(db).remover(id=produto_id)

    return produto_removido
