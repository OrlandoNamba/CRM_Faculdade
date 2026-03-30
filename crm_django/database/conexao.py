import sqlite3
import os
import sys


def get_base_dir():
    # Se estiver rodando como .exe
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # Se estiver rodando pelo VSCode / Python normal
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR = get_base_dir()
CAMINHO_BANCO = os.path.join(BASE_DIR, 'database', 'crm.db')


def conectar_banco():
    print("BANCO EM USO:", CAMINHO_BANCO)
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao