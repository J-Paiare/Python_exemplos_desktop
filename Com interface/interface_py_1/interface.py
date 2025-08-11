import tkinter as tk

def mostrar_mensagem():
    #obter o texto da caixa de texto
    texto = caixa_texto.get()
    # atualizar o texto no rotulo com o texto da caixa
    label_resultado.config(text=texto)

#criar a Janela principal
Janela = tk.Tk()
Janela.title("Exemplo de interface")
Janela.geometry("400x150")

#mudando a cor de fundo
Janela.config(bg="light blue")

#Criar uma caixa de entrada (entry)
caixa_texto= tk.Entry(Janela, width=60)
caixa_texto.pack(pady=10)

#criar botao
botao = tk.Button(Janela, text="Mostrar texto", command=mostrar_mensagem)
botao.pack(pady=5)

#criar um rotulo para mostrar o resultado
label_resultado = tk.Label(Janela, text="", bg="light blue")
label_resultado.pack(pady=10)

#executar
Janela.mainloop()

