from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.usuarios.schemas import Usuario
from app.repository.usuario import RepositorioUsuario
from app.api.deps import get_db, obter_usuario_logado


usuarios_router = APIRouter()


@usuarios_router.get("/", response_model=list[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios_db = RepositorioUsuario(db).listar()

    if usuarios_db is None:
        raise HTTPException(status_code=404, detail="Não exitem usuários!")

    return usuarios_db


@usuarios_router.get("/me")
def obter_usuario_me(usuario: Usuario = Depends(obter_usuario_logado)):

    if usuario.ativo == False:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")

    return usuario


# @usuarios_router.delete("/")
# def remover_usuario(db: Session = Depends(get_db), usuario: Usuario = Depends(obter_usuario_logado)):
#     usuario_removido = RepositorioUsuario(db).remover(id=usuario.id)

#     return usuario_removido


@usuarios_router.get("/{usuario_id}", response_model=Usuario)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = RepositorioUsuario(db).obter(id=usuario_id)
    
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    return usuario_db
