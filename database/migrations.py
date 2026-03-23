from database.conexao import conectar_banco

def adicionar_colunas_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN telefone2 VARCHAR(15)")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN telefone3 VARCHAR(15)")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN renda DECIMAL(10,2)")
    except:
        pass

    conexao.commit()
    conexao.close()


adicionar_colunas_clientes()