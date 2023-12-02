from app.api.usuarios.schemas import Usuario, UsuarioCreate, LoginData, LoginSucesso
from app.repository.usuario import RepositorioUsuario
from app.api.deps import get_db

from app.security.hash import gerar_hash, verificar_hash
from app.security.token import criar_access_token
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException


login_router = APIRouter()


@login_router.post("/signup", response_model=Usuario, status_code=201)
def signup(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_encontrado = RepositorioUsuario(db).obter_por_email(email=usuario.email)

    if usuario_encontrado:
        raise HTTPException(
            status_code=400, detail="Já existe um usuário com este e-mail!"
        )

    usuario.senha = gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario=usuario)

    return usuario_criado


@login_router.post("/login/token", response_model=LoginSucesso)
def login(login_data: LoginData, db: Session = Depends(get_db)):
    email = login_data.email
    senha = login_data.senha

    usuario_db = RepositorioUsuario(db).obter_por_email(email=email)

    if not usuario_db:
        raise HTTPException(
            status_code=401, detail=f"E-mail ou senha estão incorretos!"
        )

    senha_valida = verificar_hash(senha, usuario_db.senha)

    if not senha_valida:
        raise HTTPException(
            status_code=401, detail=f"E-mail ou senha estão incorretos!"
        )

    # GERAR JWT
    token = criar_access_token({"sub": usuario_db.email})

    return LoginSucesso(usuario=usuario_db, access_token=token)
