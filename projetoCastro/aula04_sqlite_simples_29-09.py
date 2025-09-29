# aula02_sqlite_simple.py
# Lê produtos.json e grava em produtos.db (SQLite), depois exporta CSV.
import json
import sqlite3
import csv
import os

JSON_PATH = "produtos.json"
DB_PATH = "produtos.db"
CSV_OUT = "produtos_from_sqlite.csv"

# 1) Carrega dados do JSON criado na Aula 1
if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"{JSON_PATH} não encontrado. Execute a Aula 1 primeiro.")
with open(JSON_PATH, "r", encoding="utf-8") as f:
    produtos = json.load(f)   # lista de dicionários: [{"nome":..., "preco":..., "quantidade":...}, ...]

# 2) Conectar/criar banco SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 3) Criar tabela se não existir
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

# 4) Inserir registros (usar INSERT OR IGNORE para evitar duplicatas por nome)
for p in produtos:
    nome = p.get("nome")
    preco = float(p.get("preco", 0))
    quantidade = int(p.get("quantidade", 0))
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
            (nome, preco, quantidade)
        )
    except Exception as e:
        print("Erro ao inserir:", e)

# 5) Commit e listar
conn.commit()
cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
rows = cursor.fetchall()
print("Registros no DB (SQLite):")
for r in rows:
    print(r)

# 6) Exportar para CSV
with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nome", "preco", "quantidade"])
    writer.writerows(rows)

print("Exportado para:", CSV_OUT)

# 7) Fechar conexão
conn.close()
