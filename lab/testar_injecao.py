"""
testar_injecao.py - Valida a correção comparando app.py e app_seguro.py.

Tenta o mesmo login nas duas versões: com credenciais corretas, com senha
errada e com uma entrada de SQL Injection. Na versão vulnerável a injeção
entra sem senha; na segura, não.

Como rodar (na raiz do projeto):  python lab/testar_injecao.py
"""

import contextlib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import app
import app_seguro

CASOS = [
    ("credenciais corretas", "alice", "alice123"),
    ("senha errada", "alice", "errada"),
    ("SQL Injection", "admin' --", "qualquer"),
]


def rodar(modulo):
    conn = modulo.criar_banco()
    for nome, usuario, senha in CASOS:
        with contextlib.redirect_stdout(io.StringIO()):  # esconde o [debug]
            resultado = modulo.login(conn, usuario, senha)
        status = f"ENTROU como {resultado[1]}" if resultado else "bloqueado"
        print(f"  {nome:<22} -> {status}")


for titulo, modulo in [("app.py (vulnerável)", app), ("app_seguro.py (corrigido)", app_seguro)]:
    print(titulo)
    rodar(modulo)
    print()
