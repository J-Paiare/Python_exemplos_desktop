import ttkbootstrap as ttk # importa a biblioteca ttkboostrap para criar a interface grafica
from ttkbootstrap.constants import * #importa constantes úteis do ttlbootstrap
from PIL import Image,ImageTk #importa constantes úteis do ttkboostrap
from functools import partial #importa a biblioteca PIL para trabalhar com imagens
import os
import sys

def resource_path(relative_path):
    """ obtem o caminho absoluto para o recurso, funciona para dev e PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Calculadora:
    def __init__(self):
        # configuraçao da janela principal
        self.janela = ttk.Window(themename="darkly")
        self.janela.geometry('400x750') #define o tamanho da janela
        self.janela.title('Calculadora Senai')

        #definiçao de cores e fontes
        self.cor_fundo = 'black' #cor de fundo da interface
        self.cor_botao = 'secondary' #cor do botao numerico
        self.cor_texto = "white" #cor de texto
        self.cor_operador = 'warning' #cor dos botoes operadores
        self.font_padrao = ('Roboto', 18) #fonte padrao dos botoes
        self.fonte_display = ('Roboto', 18) #fonte do display

        #configuraçao do incone da janela
        icon_path = resource_path("calc.ico") #caminho do icone
        self.frame_display.pack(fill='both', expand=True) #adiciona o frame ao layout da janela

        #frame para o display
        self.frame_display = ttk.Frame(self.janela) #frame para o display
        self.frame_display.pack(fill='both', expand=True) #adiciona o frame ao layout da janela
        
        # display para os calculos
        self.display = ttk.Label(
            self.frame_display,
            text='',
            font=self.fonte_display,
            anchor='e', #alinha o texto a direita
            padding=(20, 10) #adiciona um preenchimento interno ao rotulo
        )
        self.display.pack(fill='both', expand=True) #adiciona o display ao frame

        #frame para os botoes
        self.frame_botoes = ttk.Frame(self.janela) #cria um frame para os botoes
        self.frame_botoes.pack(fill='both', expand=True) #adiciona o frame ao layoutda janela

        # configuraçoes dos botoes
        self.botoes = [
            ['C', '<X]', '^', '/'], #linha 1
            ['7','8','9', 'X'], #linha 2
            ['4', '5', '6', '+'], #linha 3
            ['1', '2', '3', '-'], #linha 4
            ['.', '0', '()', '='] #linha 5
        ]

        #criando botoes
        for i, linha in enumerate(self.botoes): #intera sobre as linhas de botoes
            for j, texto in enumerate(linha): #altera sobre os botoes em cada linha
                estilo = 'warnig.TButton' if texto in ['C', '<X]', '^', '/', 'X', '+', '-', '='] else 'secondary.Tbutton' 
                botao = ttk.Button(
                    self.frame_botoes, 
                    text = texto,
                    style = estilo,
                    width=10, #largura do botao
                    command = partial(self.interpretar_botao, texto)
                )
                botao.grid(row=i, column=j, padx=1, pady=1, sticky='nsew') #adiciona o botao a grid

        #configura o redimensionamento das linhas e colunas
        for i in range(5):
            self.frame_botoes.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.frame_botoes.grid_columnconfigure(j, weight=1)
        
        #frame para a imagem SENAI
        self.frame_imagem = ttk.Frame(self.janela)
        self.frame_imagem.pack(fill='both', expand=True, pady=10)

        #carregando e exibindo a imagem SENAI
        imagem_path = resource_path("Senai.png") #obtem o caminho para a imagem
        imagem = Image.open(imagem_path) # abre a imagem usando PIL
        imagem = imagem.resize((300, 100), Image.LANCZOS) #redimensiona a imagem mantendo a qualidade
        imagem_tk =ImageTk.PhotoImage(imagem) #converte a imagem para o formato compativel com o tk

        label_imagem = ttk.Label(self.frame_imagem, image=imagem_tk, text="")
        label_imagem.image = imagem_tk
        label_imagem.pack()
        
        # frame para o seleor de temas
        self.frame_tema = ttk.Frame(self.janela)
        self.frame_tema.pack(fill='X', padx=10, pady=10)

        #label escolher tema
        self.label_tema = ttk.Label(self.frame_tema, text="Escolher tema: ", font=('Roboto', 12))
        self.label_tema.pack(side='top', pady=(0, 5))

        #seletor de temas (ComboBox)
        self.temas = ['darkly', 'cosmo', 'flatly', 'journal', 'litera, lumen', 'minty', 'pulse','sandstone', 'united', 'yeti', 'morth', 'simplex','cerculean']
        self.seletor_tema = ttk.Combobox(self.frame_tema, values=self.temas, state='readonly')
        self.seletor_tema.set('darkly') #define o tema pardao
        self.seletor_tema.pack(side='top', fill='X')
        self.seletor_tema.bind('<<ComboboxSelected>>', self.mudar_tema)

        # inicia a janela principal
        self.janela.mainloop() #inicia o loop principal
       
    def mudar_tema(self, evento):
        """ muda o tema"""
        novo_tema = self.seletor_tema.get()
        self.janela.style.theme_use(novo_tema)

    def interpretar_botao(self, valor):
        """ interpreta o botao pressionado e atualiza o display"""
        texto_atual = self.display.cget("text")

        if (valor =="C"):
        #limpa o display
            self.display.configure(text='')
        elif (valor == '<X]'):
            #apaga o ultimo charactere
            self.display.configure(tex=texto_atual[:-1])
        elif (valor == '='):
            #calcula o resultado da expressao
            self.calcular()
        elif (valor == '()'):
            # adiciona parenteses
            if not texto_atual or texto_atual[-1] in '+-/^X':
                self.display.configure(text=texto_atual + '(')
            elif texto_atual[-1] in '0123456789)':
                self.display.configure(text=texto_atual + ')')

        else: 
            #adiciona o valor do botao pressionado ao display
            self.display.configure(text=texto_atual + valor)

    def calcular(self):
        """ realiza o calculo da expressao no display"""
        expressao = self.display.cget("text")
        expressao = expressao.replace('X', '*').replace('^', '**') #substitui operadores para sintase python

        try: 
            #avalia a expressao e exibe o resultado
            resultado = eval(expressao)
            self.display.configure(text=str(resultado))
        except:
            #exibe mensagem de erro
            self.display.configure(text="Erro")

# inicia a aplicaçao
if __name__=="__Main__":
    Calculadora() #instancia a classe calculadora
    

