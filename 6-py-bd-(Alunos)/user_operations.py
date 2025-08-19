# inicializa a classe com referencias ao banco de dados e a interface do usuario
class UserOperations:
    def __init__(self, db, ui):
        self.db = db
        self.ui = ui
        #cadastra um novo usuario do banco de dados
        def cadastrar(self):
            nome = self.ui.nome_entry.get()
            if nome:
                self.db.insert_user(nome)
                messagebox.showinfo("Sucesso", "Usuario Cadastrado com sucesso")
                self.ui.nome_entry.delete(0, 'end')
                self.ui.carregar_dados()
            else:
                messagebox.showerror("erro", "Por favor, preencha o campo nome")

        #atualiza as informaçoes de um usuario existente
        def atualizar_usuario(self):
            if self.ui.selected_user:
                novo_nome = self.ui.nome_entry.get()
                if novo_nome:
                    self.db.update_user(self.ui.selected_user[0], novo_nome)
                    messagebox.showinfo("sucesso", "usuario atualizado com sucesso")
                    self.ui.carregar_dados()
                    self.ui.nome_entry.delete(0, 'end')
                    self.ui.selected_user = None
                else:
                    messagebox.showerror("erro", "por favor preencha o campo nome")
            else:
                messagebox.showerror("erro", "por favor selecione um usuario para atualizar")

        # exclui o usuario do banco de dados
        def excluir_usuario(self):
            if self.ui.selected_user:
                if messagebox.askyesno("confirmar", "Tem certeza que deseja excluir este usuario?"):
                    self.db.delete_user(self.ui.selected_user[0])
                    messagebox.showinfo("Sucesso", "usuario exluido com sucesso")
                    self.ui.carregar_dados()
                    sel.ui.nome_entry.delete(0, 'end')
                    self.ui.selected_user = None
            else:
                messagebox.showerror("Erro", "Por favor selecione im usuario para excluir")
    