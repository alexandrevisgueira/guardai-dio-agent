"""
app.py - Login VULNERÁVEL, apenas para laboratório.

Este arquivo existe para testar o GuardAI: peça ao agente que encontre
a falha, explique a exploração e ajude a corrigir.
NÃO use este código em nenhum sistema real.

Como rodar:  python lab/app.py
"""

import sqlite3

DB = ":memory:"  # banco em memória: nada é gravado em disco


def criar_banco():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
    cur.executemany(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        [("admin", "S3nh@Forte!"), ("alice", "alice123")],
    )
    conn.commit()
    return conn


def login(conn, usuario, senha):
    cur = conn.cursor()
    # Monta o SQL juntando o que a pessoa digitou
    query = "SELECT id, usuario FROM usuarios WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'"
    print(f"[debug] SQL executado: {query}")
    cur.execute(query)
    return cur.fetchone()


def main():
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    resultado = login(conn, usuario, senha)
    if resultado:
        print(f"Login OK. Bem-vindo, {resultado[1]}!")
    else:
        print("Usuário ou senha inválidos.")


if __name__ == "__main__":
    main()
