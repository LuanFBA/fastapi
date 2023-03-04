from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.usuario import Usuario
from app.crud import crud_usuario
from app.api.deps import get_db, obter_usuario_logado


router = APIRouter()


@router.get("/", response_model=list[Usuario])
def listar_usuarios(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    usuarios_db = crud_usuario.listar_usuarios(db=db, skip=skip, limit=limit)

    if usuarios_db is None:
        raise HTTPException(status_code=404, detail="Não exitem usuários!")

    return usuarios_db


@router.get("/me")
def obter_usuario_me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario


@router.delete("/")
def remover_usuario(db: Session = Depends(get_db), usuario: Usuario = Depends(obter_usuario_logado)):
    usuario_removido = crud_usuario.remover_usuario(db=db, usuario_id=usuario.id)

    return usuario_removido


@router.get("/{usuario_id}", response_model=Usuario)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = crud_usuario.obter_usuario(db=db, usuario_id=usuario_id)
    
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    return usuario_db
