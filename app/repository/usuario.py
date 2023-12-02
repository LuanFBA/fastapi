from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from app.models.models import Usuario
from app.api.usuarios.schemas import UsuarioCreate


class RepositorioUsuario:
    def __init__(self, db: Session):
        self.db = db

    def obter(self, id: int):
        consulta = select(Usuario).where(Usuario.id == id)
        return self.db.execute(consulta).scalars().first()

    def obter_por_email(self, email: str):
        consulta = select(Usuario).where(Usuario.email == email)
        return self.db.execute(consulta).scalars().first()

    def criar(self, usuario: UsuarioCreate):
        usuario_db = Usuario(
            nome=usuario.nome, email=usuario.email, senha=usuario.senha
        )
        self.db.add(usuario_db)
        self.db.commit()
        self.db.refresh(usuario_db)
        return usuario_db

    def listar(self):
        consulta = select(Usuario)
        usuarios = self.db.execute(consulta).scalars().all()
        return usuarios

    def remover(self, id: int):
        delete_stmt = delete(Usuario).where(Usuario.id == id)

        self.db.execute(delete_stmt)
        self.db.commit()
