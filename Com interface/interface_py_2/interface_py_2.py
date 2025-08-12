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
    Label_resultado.config(text=mensagem)

def limpar_campos():
    #limpa todas as caixas
    caixa_texto.delete(0, tk.END)
    var_radio.set("café")
    var_check_saudacao.set(False)
    var_check_personalizada.set(False)
    combo_cor.set("escolha sua cor")
    Label_resultado.config(text="")

#criar a Janela principal
Janela = tk.Tk()
Janela.title("Exemplo de interface")
Janela.geometry("400x550")
Janela.config(bg="light blue")

#Criar uma caixa de entrada (entry)
label_nome = tk.Label(Janela, text="digite seu nome")
label_nome.pack(pady=5)
caixa_texto= tk.Entry(Janela, width=60)
caixa_texto.pack(pady=10)

# criar botoes de radio
label_preferencia = tk.Label(Janela, text="escolha sua preferencia: ")
label_preferencia.pack(pady=5)

var_radio = tk.StringVar(value="Café")
radio_cafe = tk.Radiobutton(Janela, text="Café", variable=var_radio, value="Café")
radio_cha = tk.Radiobutton(Janela, text="Chá", variable=var_radio, value="Chá")
radio_suco = tk.Radiobutton(Janela, text="Suco", variable=var_radio, value="Suco")
radio_agua = tk.Radiobutton(Janela, text="Agua", variable=var_radio, value="Agua")

#metohod tkinther que deixa as opçoes visiveis (.pack)
radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()

# criar caixas de multipla escolha
var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(Janela, text="Usar saudaçao informal", variable=var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar()
check_personalizada = tk.Checkbutton(Janela, text="Usar saudaçao personalizada", variable=var_check_personalizada)
check_personalizada.pack(pady=5)

#comboBox (caixa com seleçao de opçoes)
label_cor = tk.Label(Janela, text="slelecione sua cor favorita", bg="light blue")
label_cor.pack(pady=5)

combo_cor = ttk.Combobox(Janela, values= ["vermelho", "azul", "amarelo", "preto", "laranja", "verde"])
combo_cor.set("escolha sua cor")
combo_cor.pack(pady=5)

# botoes

botao_atualizar = ttk.Button(Janela, text= "atualizar", command=atualizar_resultado)
botao_atualizar.pack(pady=10)

botao_limpar = ttk.Button(Janela, text= "limpar", command=limpar_campos)
botao_limpar.pack(pady=10)

#exibiçao de resultado final (rotulo "label")
Label_resultado = tk.Label(Janela, text="", wraplength=350)
Label_resultado.pack(pady=10)


#Executar a janela principal
Janela.mainloop()

