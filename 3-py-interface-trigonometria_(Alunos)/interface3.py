import tkinter as tk #importa a biblioteca TKinter para a criaçao da interface grafica
import math #Importa a biblioteca math para realizar operaçoes matematicas
from PIL import Image, ImageTk #importa as classes Image e ImageTk da biblioteca PIL para manipulaçao de Imagens
import os #importa a biblioteca os para operaçoes com o sistema de arquivos
import sys #importa a biblioteca sys para manipulaçao de variaveis e funçoes do sistema

def resource_path(relative_path):
    """ Obtem o caminho absoluto para o recurso, funciona para Dev e para PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def calcular():
    """realiza o calculo dos valored trigonometricos(seno, cosseno e tangente) do angulo fornecido e atualiza as abels com o resultado
    """
    try:
        angulo = float(entrada_angulo.get())
        radiano = math.radians(angulo)

        #calcula os valores trigonometricos
        seno = math.sin(radiano)
        cosseno = math.cos(radiano)
        tangente = math.tan(radiano)

        #atualiza as labels com os resultado formatados com 3 casas decimais
        resultado_seno.config(text=f"{seno:.3f}")
        resultado_cosseno.config(text=f"{cosseno:.3f}")
        resultado_tangente.config(text=f"{tangente:.3f}")
    except ValueError:
        #em caso de erro (por exemplo entrada invalida) exibe o erro
        resultado_seno.config(text="Erro")
        resultado_cosseno.config(text="Erro")
        resultado_tangente.config(text="Erro")

def limpar():
    """
    Limpa a entrada do uisuario e reseta as labels dos resultados
    """
    #limpa os campos
    entrada_angulo.delete(0, tk.END) 
    resultado_seno.config(test="")
    resultado_cosseno.config(test="")
    resultado_tangente.config(test="")

def validar_entrada(texto):
    """
    Valida a entrada do usuario permitingo apenas nunmeros e garantingo que estevam entre 0 e 90
    """

    if texto.isdigit() or texto == "": #permite apenas numeros ou o campo vazio
        if texto == "":
            return True
        valor = int(texto) #converte o texto para inteiro
        return 0 <= valor <= 90 #retorna true se o valor estiver entre 0 e 90
    return False #se nao for numero retorna falso

#configuraçoes da janela principal
janela = tk.Tk()
janela.title("Calculadora Trigonometrica")
janela.geometry("400x550")
janela.configure(bg="#f0f0f0")

# carregar e definir icone da janela principal
try:
    icone_path = resource_path("seno.png")
    icone = Image.open(icone_path)
    icone = ImageTk.PhotoImage(icone)
except FileNotFoundError:
    print("Imagem nao encontrada para o icone")

    #Imagem seno2.png
    try:
        Imagem_path = resource_path("seno2.png")
        Imagem = Image.open(Imagem_path)
        Imagem =  Imagem_resize((380, 200), Image.LANCZOS)
        foto = ImageTk.PhotoImage(Imagem)
        label_Imagem = tk.label(janela, Imagem=foto, bg="#f0f0f0", borderwidth=0)

        label_Imagem.Image = foto
        label_Image.pack(pady=20)
    except FileNotFoundError:
    label_Imagem = tk.label(janela,text="Imagem nao encontrada", bg="#f0f0f0")
    label_Imagem.pack(pady=20)

#entrada do angulo
frame_entrada = tk.Label(janela,  bg="#f0f0f0")
frame_entrada.pack(pady=10)

label_angulo = tk.Label(frame_entrada, text="angulo (0 á 90): ", font=('arial', 14,  bg="#f0f0f0"))
label_angulo.pack(pady=(0,5))

validacao = janela.register(validar_entrada)
entrada_angulo.pack(pady=(0,5))

validacao = janela.register(validar_entrada)
entrada_angulo = tk.Entry(frame_entrada, width=3, justfy='center', font=('Arial', 16),
                          bd=0, highlightthickness=0, relief=flat,  bg="#f0f0f0", fg='red', validate="key", validatecommand=(validacao, '%P'))

entrada_angulo.pack()

#linha a baixo do campo de entrada
linha = tk.Frame(frame_entrada, bg="black", height=1, width=entrada_angulo.winfo_reqheight()) #linha decorativa
linha.pack(pady=(0,5))

#botoes
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady=20)

botao_calcular= tk.Button(frame_botoes, text="calcular", command=calcular, font=('Arial' 12),
                           bg="#f0f0f0", relief='flat', bd=0, highlightthickness=0)
botao_calcular.pack(side=tk.LEFT, padx=10)

botao_limpar= tk.Button(frame_botoes, text="Limpar", command=limpar, font=('Arial' 12),
                           bg="#f0f0f0", relief='flat', bd=0, highlightthickness=0)
botao_limpar.pack(side=tk.LEFT, padx=10)

# resultados
frame_resultados =  tk.frame(janela, bg="#f0f0f0")
frame_resultados.pack(pady=10)

#Label e resultado para o seno
label_seno = tk.Label(frame_resultados, text="Seno", font=('Arial', 12), bg="#f0f0f0")
label_seno.grid(row=0, column=0, padx=10, pady=5, sticky='e')
resultado_seno = tk.Label(frame_resultados, text="",font=('Arial', 12, 'bold'), bg="#f0f0f0", fg='red')
resultado_seno.grid(row=0, column=1, padx=10, pady=5, sticky='w')

#labvel resultado cosseno
label_cosseno = tk.Label(frame_resultados, text="Cosseno", font=('Arial', 12), bg="#f0f0f0")
label_cosseno.grid(row=0, column=0, padx=10, pady=5, sticky='e')
resultado_cosseno = tk.Label(frame_resultados, text="",font=('Arial', 12, 'bold'), bg="#f0f0f0", fg='red')
resultado_cosseno.grid(row=0, column=1, padx=10, pady=5, sticky='w')

#label resultado tangente
label_tangente = tk.Label(frame_resultados, text="Tangente", font=('Arial', 12), bg="#f0f0f0")
label_tangente.grid(row=0, column=0, padx=10, pady=5, sticky='e')
resultado_tangente = tk.Label(frame_resultados, text="",font=('Arial', 12, 'bold'), bg="#f0f0f0", fg='red')
resultado_tangente.grid(row=0, column=1, padx=10, pady=5, sticky='w')

#inicia a janela
janela.mainloop()