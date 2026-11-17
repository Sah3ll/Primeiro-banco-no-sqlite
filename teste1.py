import sqlite3

try:
    banco = sqlite3.connect('banco.db')
    #Criação de conexão com o banco de dados
    cursor = banco.cursor()
    #Cria um objeto para executar comandos SQL
    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")
    #Executa instruções SQL
    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")
    banco.commit() #Confirma as alterações realizadas
    print("Os dados foram adicionados com sucesso!!")
    #Mostra que os comandos foram executados com sucesso

    cursor.execute("Select *FROM aluno")
    print(cursor.fetchall())
    #recupera todos os dados
    cursor.execute("DELETE from aluno WHERE idade = 20")
    #Executa instruções SQL no caso o de apagar uma informação
    banco.commit() #Confirma as alterações realizadas
    banco.close() #Encerra a concxão com o banco de dados
    print("Os dados foram removidos com sucesso!!")
    #Mostra que os comandos foram executados com sucesso
except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)
    #Executado apensas se houver erro ao apagar um dado