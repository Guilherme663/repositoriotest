from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

## AQUI ESTAMOS CONFIGURANDO A SEGURANÇA PARA USAR JWT (JSON WEB TOKENS) COM O ALGORITMO HS256. O HTTPBearer É UM ESQUEMA DE AUTENTICAÇÃO QUE EXIGE QUE O CLIENTE ENVIE UM TOKEN DE AUTENTICAÇÃO NO CABEÇALHO DA REQUISIÇÃO. O SECRETE_KEY É USADO PARA ASSINAR E VERIFICAR OS TOKENS JWT, ENQUANTO O ALGORITHM ESPECIFICA O ALGORITMO DE ASSINATURA USADO PARA GERAR O TOKEN. ESSA CONFIGURAÇÃO É ESSENCIAL PARA PROTEGER AS ROTAS DA API E GARANTIR QUE APENAS USUÁRIOS AUTENTICADOS POSSAM ACESSAR DETERMINADAS FUNCIONALIDADES.
SECRET_KEY = "segredo"
ALGORITHM = "HS256"

security = HTTPBearer()

async def criar_token():
    dados = {"user": "guilherme"}
    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token

async def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dados
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    




