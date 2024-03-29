from app.db.session import SessionLocal
from app.repository.usuario import RepositorioUsuario
from app.security.token import verificar_access_token

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl= "token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        email: str = verificar_access_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido!")

    if not email:
        raise HTTPException(status_code=401, detail="Token inválido!")

    usuario_db = RepositorioUsuario(db).obter_por_email(email=email)

    if not usuario_db:
        raise HTTPException(status_code=401, detail="Token inválido!")

    return usuario_db
