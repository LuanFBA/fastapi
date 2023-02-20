from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def verificar_hash(senha, hash) -> bool:
    return pwd_context.verify(senha, hash)


def gerar_hash(senha) -> str:
    return pwd_context.hash(senha)
