from datetime import datetime, timedelta

from jose import jwt


SECRET_KEY = "871d296e40d1c63afb1755e9dca66de4f998fe3cd69406a806d502c0f8f569ea"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14000


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados.update({"exp": expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt


def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return carga.get("sub")
