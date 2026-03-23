from database.conexao import conectar_banco

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(11) NOT NULL UNIQUE,
        logradouro VARCHAR(200),
        bairro VARCHAR(100),
        cidade VARCHAR(100) NOT NULL,
        estado VARCHAR(2),
        cep VARCHAR(8),
        telefone VARCHAR(15) NOT NULL,
        telefone2 VARCHAR(15),
        telefone3 VARCHAR(15),
        renda DECIMAL(10,2),
        data_nascimento DATE
    )
    """)

    conexao.commit()
    conexao.close()