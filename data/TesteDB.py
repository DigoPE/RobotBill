import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'billdb',
    user = 'root',
    passwd = '1234'
    )

def fechaConexao():
    mydb.close()

print(mydb)

#Test
if mydb.is_connected():
    #Pega informações do Servidor.
    db_info = mydb.get_server_info()
    print('Conectado ao servidor MySQL Versão: ', db_info)
    #Ele recebe e lê os elementos de uma tabela.
    cursor = mydb.cursor()
    cursor.execute('select database();')
    #Esse metodo vai buscar uma linha.
    linha = cursor.fetchone()
    print('Conectado ao Banco de Dados: ', linha)

#Fecha a Conexão para liberar os recursos do servidor.
if mydb.is_connected():
    cursor.close()
    #mydb.close()
    fechaConexao()
    print('Conexão MySQL foi encerrada!')