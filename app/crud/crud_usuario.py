from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate
from app.models.usuario import Usuario

def obter_usuario(db: Session, usuario_id: int) -> Usuario:
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def obter_usuario_email(db: Session, usuario_email: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.email == usuario_email).first()


def listar_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()


def criar_usuario(db: Session, usuario: UsuarioCreate):
    usuario_db = Usuario(email=usuario.email, nome=usuario.nome, senha=usuario.senha)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


def remover_usuario(db: Session, usuario_id: int):
    usuario_db = obter_usuario(db, usuario_id)
    db.delete(usuario_db)
    db.commit()
