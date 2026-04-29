from fastapi import FastAPI,Depends, HTTPException
import aiosqlite
from auth import verificar_token,criar_token
from database import criar_tabela,get_db

app = FastAPI()

# chama ao iniciar
@app.on_event("startup")
async def startup():
    await criar_tabela()
    
@app.get("/protegido")
async def rota_protegida(user=Depends(verificar_token)):
    return {"msg": "acesso liberado", "user": user}

# 🔥 CREATES
@app.post("/clientes")
async def criar_clientes(nome: str, user = Depends(verificar_token)):
        db = await get_db()
        await db.execute(
            "INSERT INTO clientes (nome) VALUES (?)",
            (nome,)
        )
        await db.commit()

        return {"msg": "cliente criado"}

# 📖 READ
@app.get("/clientes")
async def listar_clientes(user = Depends(verificar_token)):
    db = await get_db()
    async with db.execute("SELECT * FROM clientes") as cursor:
        clientes = await cursor.fetchall()

    # deixar mais bonito
    resultado = []
    for cliente in clientes:
        resultado.append({
            "id": cliente[0],
            "nome": cliente[1]
        })

    return resultado

# ✏️ UPDATE
@app.put("/clientes/{id}")
async def atualizar_clientes(id: int, nome: str, user = Depends(verificar_token)):
    db = await get_db()
    await db.execute(
        "UPDATE clientes SET nome = ? WHERE id = ?",
        (nome, id)
    )
    await db.commit()

    return {"msg": "atualizado"}

# ❌ DELETE
@app.delete("/clientes/{id}")
async def deletar_clientes(id: int, user = Depends(verificar_token)):
    db = await get_db()
    await db.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id,)
        )
    await db.commit()

    return {"msg": "deletado"}
