from fastapi import APIRouter, Depends
import aiosqlite
from auth import verificar_token

router = APIRouter(prefix="/clientes")

@router.post("/")
async def listar_clientes(user = Depends(verificar_token)):
    async with aiosqlite.connect("clientes.db") as db:
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