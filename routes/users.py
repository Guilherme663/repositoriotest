from fastapi import APIRouter, HTTPException
import aiosqlite
from auth import criar_token

router = APIRouter()

@router.post("/register")
async def registrar(username: str, password: str):
    async with aiosqlite.connect("clientes.db") as db:
        try:
            await db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            await db.commit()
            return {"msg": "usuário criado"}
        except:
            raise HTTPException(status_code=400, detail="usuário já existe")
        
@router.post("/login")
async def login(username: str, password: str):
    async with aiosqlite.connect("clientes.db") as db:
        async with db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ) as cursor:
            user = await cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=400, detail="credenciais inválidas")
        return {"token": criar_token(username)}
