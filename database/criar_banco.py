from database.conexao import conectar_banco

conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

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
    data_nascimento DATE
)
""") # Executa um comando SQL para criar a tabela "clientes" com os campos especificados, se ela ainda não existir

conexao.commit() # Salva as alterações no banco de dados
conexao.close() # Fecha a conexão com o banco de dados