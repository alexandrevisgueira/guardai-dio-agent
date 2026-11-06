"""
app_seguro.py - Versão corrigida do lab/app.py, apenas para laboratório.

O que mudou em relação ao app.py:
1. Consulta parametrizada: o usuário e a senha vão como parâmetros (?),
   nunca concatenados no SQL. O banco trata o que foi digitado como dado,
   não como comando. Isso mitiga o SQL Injection (CWE-89).
2. Senhas guardadas como hash com salt (PBKDF2, da biblioteca padrão),
   não em texto puro.
3. Comparação de hash em tempo constante (hmac.compare_digest).
4. Sem imprimir o SQL na tela: detalhes internos não vão para o usuário.

Como rodar:  python lab/app_seguro.py
"""

import hashlib
import hmac
import os
import sqlite3

DB = ":memory:"
ITERACOES = 600_000


def gerar_hash(senha, salt=None):
    salt = salt or os.urandom(16)
    h = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, ITERACOES)
    return salt, h


def criar_banco():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT UNIQUE, salt BLOB, senha_hash BLOB)")
    for usuario, senha in [("admin", "S3nh@Forte!"), ("alice", "alice123")]:
        salt, h = gerar_hash(senha)
        cur.execute("INSERT INTO usuarios (usuario, salt, senha_hash) VALUES (?, ?, ?)", (usuario, salt, h))
    conn.commit()
    return conn


def login(conn, usuario, senha):
    cur = conn.cursor()
    # Consulta parametrizada: o ? é preenchido pelo driver, de forma segura
    cur.execute("SELECT id, usuario, salt, senha_hash FROM usuarios WHERE usuario = ?", (usuario,))
    linha = cur.fetchone()
    if linha is None:
        return None
    _, h = gerar_hash(senha, linha[2])
    if hmac.compare_digest(h, linha[3]):
        return (linha[0], linha[1])
    return None


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
