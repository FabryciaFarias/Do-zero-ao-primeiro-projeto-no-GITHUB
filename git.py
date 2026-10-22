import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor() #objeto mensageiro de conexão com o banco de dados

cursor.execute("""create table if not exists contas_bancarias(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL, 
    cpf TEXT NOT NULL UNIQUE)""")

# cursor.execute("""INSERT INTO contas_bancarias
#     (titular, saldo, cpf) VALUES
#     ("Maria", 6000, "149.473.045.07")""")

cursor.execute("""SELECT titular, saldo FROM contas_bancarias""") #Seleciona todos os registros da tabela contas_bancarias
cursor.execute("""update contas_bancarias set titular = "Karol" where titular = "Maria" """) #atualiza o Nome do titular da conta de maria para karol
#cursor.execute('delete from contas_bancarias where id = 2') #deleta o registro da tabela contas_bancarias onde o titular é maria

contas = cursor.fetchall() #busca todos os registros da tabela contas_bancarias
for conta in contas:
    titular, saldo = conta
    print(f""" 
    titular:{titular}, 
    saldo:{saldo}, 
  """)

conexao.commit() #salva as alterações no banco de dados


