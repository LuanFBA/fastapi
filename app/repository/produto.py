from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from app.models.models import Produto
from app.api.produtos.schemas import ProdutoCreate, ProdutoSimples


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def obter(self, id: int):
        consulta = select(Produto).where(Produto.id == id)
        produto_db = self.db.execute(consulta).scalars().first()
        return produto_db

    def criar(self, produto: ProdutoCreate, usuario_id: int):
        produto_db = Produto(nome=produto.nome,
                             detalhes= produto.detalhes,
                             preco=produto.preco,
                             usuario_id=usuario_id)
        self.db.add(produto_db)
        self.db.commit()
        self.db.refresh(produto_db)
        return produto_db

    def listar(self):
        consulta = select(Produto)
        produtos = self.db.execute(consulta).scalars().all()
        return produtos
    
    def listar_me(self, usuario_id: int):
        consulta = select(Produto).where(Produto.usuario_id == usuario_id)
        produto_db = self.db.execute(consulta).all()
        return produto_db

    def atualizar(self, id: int, produto: ProdutoSimples):
        update_stmt = update(Produto).where(
            Produto.id == id).values(nome=produto.nome,
                                     detalhes=produto.detalhes,
                                     preco=produto.preco,
                                     disponivel=produto.disponivel)
        self.db.execute(update_stmt)
        self.db.commit()
    
    def remover(self, id: int):
        delete_stmt = delete(Produto).where(Produto.id == id)

        self.db.execute(delete_stmt)
        self.db.commit()
