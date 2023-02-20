from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True)
    senha = Column(String)
    ativo = Column(Boolean, default=True)

    produtos = relationship('Produto', back_populates='usuario')
