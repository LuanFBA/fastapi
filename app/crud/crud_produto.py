from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate


def obter_produto(db: Session, produto_id: int) -> Produto:
    return db.query(Produto).filter(Produto.id == produto_id).first()


def listar_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Produto).offset(skip).limit(limit).all()


def listar_produtos_usuario(
    db: Session, usuario_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(Produto)
        .filter(Produto.usuario_id == usuario_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def criar_produto_usuario(db: Session, produto: ProdutoCreate, usuario_id: int):
    produto_db = Produto(**produto.dict(), usuario_id=usuario_id)
    db.add(produto_db)
    db.commit()
    db.refresh(produto_db)
    return produto_db


def atualizar_produto(
    db: Session,
    produto_id: int,
    nome: str,
    detalhes: str,
    preco: float,
    disponivel: bool,
) -> Produto:
    produto_db = obter_produto(db=db, produto_id=produto_id)
    produto_db.nome = nome
    produto_db.detalhes = detalhes
    produto_db.preco = preco
    produto_db.disponivel = disponivel
    db.commit()
    db.refresh(produto_db)
    return produto_db


def remover_produto(db: Session, produto_id: int):
    produto_db = obter_produto(db=db, produto_id=produto_id)
    db.delete(produto_db)
    db.commit()
