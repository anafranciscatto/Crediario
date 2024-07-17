import mysql.connector

class Conexao:
    @staticmethod
    def conectar():
        # Conectando ao banco de dados
        mydb = mysql.connector.connect(
            host="localhost",
            user="userCrediario",
            password="12345",
            database="projCrediario"
        )
        return mydb

# Exemplo de utilização:
mydb = Conexao.conectar()

# Aqui você pode realizar operações no banco de dados usando mydb

# Lembre-se de fechar a conexão quando não precisar mais dela
mydb.close()
