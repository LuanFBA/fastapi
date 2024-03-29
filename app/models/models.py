from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True)
    senha = Column(String)
    ativo = Column(Boolean, default=True)

    produtos = relationship('Produto', back_populates='usuario')


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    detalhes = Column(String, index=True)
    preco = Column(Float, index=True)
    disponivel = Column(Boolean, index=True, default=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", name="fk_usuarios"))

    usuario = relationship("Usuario", back_populates="produtos")
