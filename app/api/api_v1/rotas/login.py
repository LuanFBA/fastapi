from fastapi import APIRouter, Depends, HTTPException
from app.schemas.usuario import Usuario, UsuarioCreate, LoginData, LoginSucesso
from app.crud import crud_usuario
from app.security.hash import gerar_hash, verificar_hash
from app.security.token import criar_access_token
from sqlalchemy.orm import Session
from app.api.deps import get_db


router = APIRouter()


@router.post("/signup", response_model=Usuario, status_code=201)
def signup(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_encontrado = crud_usuario.obter_usuario_email(
        db=db, usuario_email=usuario.email
    )

    if usuario_encontrado:
        raise HTTPException(
            status_code=400, detail="Já existe um usuário com este e-mail!"
        )

    usuario.senha = gerar_hash(usuario.senha)
    usuario_criado = crud_usuario.criar_usuario(db=db, usuario=usuario)

    return usuario_criado


@router.post("/login/token", response_model=LoginSucesso)
def login(login_data: LoginData, db: Session = Depends(get_db)):
    email = login_data.email
    senha = login_data.senha

    usuario_db = crud_usuario.obter_usuario_email(db, email)

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
