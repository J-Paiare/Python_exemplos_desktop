#Usando bibliotca Tkinter (Padrao do Python para intefaces)
import tkinter as tk

# Submódulo do Tikinter para widgets mais modernos e estilizados
from tkinter import ttk

def atualizar_resultado():
    # Obter o texto da caixa de texto
    nome = caixa_texto.get()
    # Obter a opção selecionada nos botões do rádio.
    preferencia = var_radio.get()
    #Verificar se a caixa de seleção de saudação informal está marcada
    if var_check_saudacao.get():
        saudacao = "Oi"
    else:
        saudacao = "Bem-vindo"


    #Verificar se a caixa de seleção de saudação informal está marcada
    # persnaliza esta marcada
    if var_check_saudacao.get():
        saudacao = f"{saudacao}, Caro(a)"

    # obter a cor favorita selecionada
    cor_favorita = combo_cor.get() 

    # Montar a mensagem final
    mensagem += f" sua cor favorita é {cor_favorita}."

    # Atualizar o texto do rótulo de mensagem
    label_resultado.config(text=mensagem)

    #criar a Janela principal
Janela = tk.Tk()
Janela.title("Exemplo de interface")
Janela.geometry("400x150")
Janela.config(bg="light blue")

#Criar uma caixa de entrada (entry)
label_nome = tk.Label(Janela, text="digite seu nome")
label_nome.pack(pady=5)
caixa_texto= tk.Entry(Janela, width=60)
caixa_texto.pack(pady=10)



#Executar a janela principal
Janela.mainloop()

