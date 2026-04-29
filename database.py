import aiosqlite

DB_NAME = "clientes.db"

async def criar_tabela():
    async with aiosqlite.connect("clientes.db") as db:

        # tabela clientes
        await db.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
        """)

        # 🔥 tabela usuários
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """)

        await db.commit()