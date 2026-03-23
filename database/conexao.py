import sqlite3
import os

def conectar_banco():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_banco = os.path.join(BASE_DIR, 'database', 'crm.db')

    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row
    return conexao