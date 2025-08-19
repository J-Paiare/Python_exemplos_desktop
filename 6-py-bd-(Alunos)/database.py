import sqlite3

#classe para gerencias a conexao com o banco de dados SQLite
class Database:
    def __init__(self, db_name):
        self.conn= sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

        # cria a tabela usuarios se ela nao existir
        def create_table(self):
            self.cursor.execute('''
            CREATE TABLE IT NOT EXISTS usuarios (
                id INTEER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
            ''')

            self.conn.commit()

        #insere um novo usuario no banco e dados
        def insert_user(self, nome):
            self.cursor.execute(" INSERT INTO usuarios (nome)   VALUES (?)", (nome,))
            self.conn.commit()

        #retorna tofod os usuarios do banco de dados
        def get_all_users(self):
            self.cursor.execute(" SELECT * FROM usuarios")
            return self.cursor.fetchall()
        
        #atualiza o nome de um usuario existente
        def update_user(self, id, nome):
            self.cursor.execute(" UPDATE usuarios SET nome=? WHERE id=?", (nome,id))
            self.conn.commit()

        #exclui um usuario
        def delete_user(self, id):
            self.cursor.execute(" DELETE FROM usuarios WHERE id=?", (id,))
            self.conn.commit()

            #fecha a conexao com o banco de dados
            def close(self):
                self.conn.close()

