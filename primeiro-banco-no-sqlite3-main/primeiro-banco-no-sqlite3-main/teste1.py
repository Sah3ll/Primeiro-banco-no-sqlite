import sqlite3

try: #Conexão com o banco de dados
    banco = sqlite3.connect('banco.db')
    #Execução de instruções e para obter resultados
    cursor = banco.cursor()
    #Criação da tebla
    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")
    #Inserção dos dados
    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")
    banco.commit()
    print("Os dados foram adicionados com sucesso!!")
    #Exibição dos dados inseridos

    cursor.execute("Select *FROM aluno")
    print(cursor.fetchall())
    #Exibição da tabela
    cursor.execute("DELETE from aluno WHERE idade = 20")
    #Comando de para apagar uma informação
    banco.commit() #Executa o comando solicitado acima
    banco.close() #Fecha a conexão com o banco de dados
    print("Os dados foram removidos com sucesso!!")
    #Exibição da confirmação que a informção solicitada para apagar foi executada
except sqlite3.Error as erro: #Caso não poder apagar a linha solicitada acima mostrará uma mensagem de erro
    print("Erro ao excluir: ", erro)
