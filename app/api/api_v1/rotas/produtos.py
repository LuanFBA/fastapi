from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.usuario import Usuario
from app.schemas.produto import Produto, ProdutoCreate, ProdutoSimples
from app.crud import crud_produto
from app.api.deps import get_db, obter_usuario_logado


router = APIRouter()


@router.post("/", response_model=Produto, status_code=201)
def criar_produto_usuario(
    produto: ProdutoCreate,
    usuario: Usuario = Depends(obter_usuario_logado),
    db: Session = Depends(get_db),
):
    produto_criado = crud_produto.criar_produto_usuario(
        db=db, produto=produto, usuario_id=usuario.id
    )

    return produto_criado


@router.get("/", response_model=list[Produto])
def listar_produtos_usuario(
    usuario: Usuario = Depends(obter_usuario_logado),
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    produto_db = crud_produto.listar_produtos_usuario(
        db=db, usuario_id=usuario.id, skip=skip, limit=limit
    )

    if produto_db is None:
        raise HTTPException(status_code=404, detail="Não existem produtos!")

    return produto_db


@router.get("/listar", response_model=list[Produto])
def listar_produtos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    produto_db = crud_produto.listar_produtos(db=db, skip=skip, limit=limit)

    if produto_db is None:
        raise HTTPException(status_code=404, detail="Não existem produtos!")

    return produto_db


@router.put("/{produto_id}", response_model=ProdutoSimples)
def atualizar_produto(
    produto_id: int,
    produto: Produto,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    produto_db = crud_produto.obter_produto(db=db, produto_id=produto_id)

    if produto_db is None:
        raise HTTPException(
            status_code=404, detail=f"Produto com id: {produto_id} não encontrado!"
        )

    if produto_db.usuario_id != usuario.id:
        raise HTTPException(status_code=400, detail="Sem permissões necessárias")

    produto_atualizado = crud_produto.atualizar_produto(
        db=db,
        produto_id=produto_id,
        nome=produto.nome,
        detalhes=produto.detalhes,
        preco=produto.preco,
        disponivel=produto.disponivel,
    )

    return produto_atualizado


@router.delete("/{produto_id}")
def remover_produto(
    produto_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    produto_db = crud_produto.obter_produto(db=db, produto_id=produto_id)

    if produto_db is None:
        raise HTTPException(
            status_code=404, detail=f"Produto com id: {produto_id} não encontrado!"
        )

    if produto_db.usuario_id != usuario.id:
        raise HTTPException(status_code=400, detail="Sem permissões necessárias")

    produto_removido = crud_produto.remover_produto(db=db, produto_id=produto_id)

    return produto_removido
