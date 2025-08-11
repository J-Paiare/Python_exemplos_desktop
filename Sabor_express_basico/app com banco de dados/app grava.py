# importação de biblioteca necessárias
# biblioteca os - operation system que permite rodar comando para mexer no sistema, editar, criar, excluir, poder fazer o crud
import os
import sqlite3


# ========================================================================================================================================================================================================================================================banco de dados
def inicializar_banco():
    """
    Função para inicializar o banco de dados SQLite
    Cria a tavela restaurantes se ela não existir
    """

    conn = sqlite3.connect('restaurantes.db')
    cursor = conn.cursor()

    # criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            ativo BOOLEAN NOT NULL DEFAULT 0
        )
    ''')

    # inserir dados iniciais apenas se a tabela estiver vazia
    cursor.execute('SELECT COUNT(*) FROM restaurantes')
    count = cursor.fetchone()[0]

    if count == 0:
        restaurantes_iniciais = [
            ('Praça', 'Japonesa', False),
            ('Pizza Suprema', 'Pizza', True),
            ('Cantina', 'Italiano', False)
        ]

        cursor.executemany('''
            INSERT INTO restaurantes (nome, categoria, ativo) VALUES (?, ?, ?)
        ''', restaurantes_iniciais)
    
    conn.commit()
    conn.close()


# lista de dicionários representando os restaurantes
# no python, chamamos array de dicionário
restaurantes = [
    {'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True}, 
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

# =====================================================================================================================================================================================================================================================================================================================
# -------------------------------------------------------------------------------------Funções de exibição e utilitárias

# camelCase - nomes com mistura de maiúsculas e minúsculas
# snake_case - utilizamos underline para separar cada palavra, utilizamos essa forma no python por padrão
def exibir_nome_do_programa():
    # três aspas serve para colocar um comentário ou print em várias linhas
    print("""        
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Excluir restaurante')
    print('5. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela (funciona apenas no windows)

    # estilizar com ******** dependendo da quantidade de letras no texto
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():

    """
    Função para processar a escola do usuário no menu principal
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # == - q nem no php, para ver se é igual string ou int msm, === - mais restrito para o tipo de dado até, = - passar valor
        if opcao_escolhida == 1:
            # print('Opção 1 escolhida!\n')
            # voltar_ao_menu_principal()
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            # print('Opção 2 escolhida!\n')
            listar_restaurantes()

        elif opcao_escolhida == 3:
            # print('Opção 3 escolhida!\n')
            # voltar_ao_menu_principal()
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            excluir_restaurante()

        elif opcao_escolhida == 5:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


# =========================================================================================================================================================================================================================================================================================================================
# ---------------------------------------------------------------------------------------Funções principais do programa

# 
def cadastrar_novo_restaurante():
    """
    Função para processar um novo restaurante

    inputs:
    - nome do restaurante
    - categoria

    outputs:
    - adiciona um novo restaurante à lista de restaurantes
    """
    exibir_subtitulo('Cadastro de novos restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    try:
        conn = sqlite3.connect('restaurantes.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO restaurantes (nome, categoria, ativo) VALUES (?, ?, ?)
        ''', (nome_do_restaurante, categoria, False))

        conn.commit()
        conn.close()

        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    except sqlite3.Error as e:
        print(f'Erro ao cadastrar restaurante: {e}')

    voltar_ao_menu_principal()

# ======================================================================================================================================================================================================================================================================================================================
def listar_restaurantes():
    """
    Função para listar todos os restaurantes cadastrados
    """

    exibir_subtitulo('Listando os restaurantes\n')

    try:
        conn = sqlite3.connect('restaurantes.db')
        cursor = conn.cursor()

        cursor.execute('SELECT nome, categoria, ativo FROM restaurantes ORDER BY nome')
        restaurantes = cursor.fetchall()

        if restaurantes:
            print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')
            print('-' * 65)

            for restaurante in restaurantes:
                nome = restaurante[0]
                categoria = restaurante[1]
                ativo = 'ativado' if restaurante[2] else 'desativado'
                print(f'{nome.ljust(21)} | {categoria.ljust(20)} | {ativo}')
        else: 
            print('Nenhum restaurante cadastrado.')

        conn.close()

    except sqlite3.Error as e:
        print(f'Erro ao listar restaurantes: {e}')

    voltar_ao_menu_principal()

# ====================================================================================================================================================================================================================================================================================================================================================================================
def alternar_estado_do_restaurante():
    """
    Função para ativar ou desativar um restaurante
    """

    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    try:
        conn = sqlite3.connect('restaurantes.db')
        cursor = conn.cursor()

        # verificar se o restaurante existe e buscar seu estado atual
        cursor.execute('SELECT ativo FROM restaurantes WHERE nome = ?', (nome_restaurante,))
        resultado = cursor.fetchone()

        if resultado is not None:
            estado_atual = resultado[0]
            novo_estado = not estado_atual

            # atualizar o estado
            cursor.execute('''
                UPDATE restaurantes SET ativo = ? WHERE nome = ?
            ''', (novo_estado, nome_restaurante))

            conn.commit()

            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if novo_estado else f'O restaurate {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
        else:
            print('O restaurante não foi encontrado!')

        conn.close()

    except sqlite3.Error as e:
        print(f'Erro ao alterar estado do restaurante: {e}')
    
    voltar_ao_menu_principal()

# =======================================================================================================================================================================================================================================================================================================================
def excluir_restaurante():
    """
    Função para excluir um restaurante
    """
    exibir_subtitulo('Excluir restaurante\n')

    # Primeiro, listar os restaurantes disponíveis
    try:
        conn = sqlite3.connect('restaurantes.db')
        cursor = conn.cursor()

        cursor.execute('SELECT nome, categoria FROM restaurantes ORDER BY nome')
        restaurantes = cursor.fetchall()

        if restaurantes:
            print('Restaurantes cadastrados: ')
            print('-' * 40)
            for restaurante in restaurantes:
                print(f'• {restaurante[0]} ({restaurante[1]})')
            print()

            nome_restaurante = input('Digite o nome do restaurante que deseja excluir: ')

            # verificar se o restaurante existe
            cursor.execute('SELECT id FROM restaurantes WHERE nome = ?', (nome_restaurante,))
            resultado = cursor.fetchone()   

            if resultado is not None:
                confirmacao = input(f'Tem certeza que deseja excluir o restaurante "{nome_restaurante}"? (s/n): ')

                if confirmacao.lower() == 's':
                    cursor.execute('DELETE FROM restaurantes WHERE nome = ?', (nome_restaurante,))
                    conn.commit()
                    print(f'O restaurante {nome_restaurante} foi excluído com sucesso!')
                else:
                    print('Exclusão cancelada.')
            else:
                print('O restaurante não foi encontrado!')
        else: 
            print('Nenhum restaurante cadastrado para excluir.')
        
        conn.close()

    except sqlite3.Error as e:
        print(f'Erro ao excluir restaurant: {e}')

    voltar_ao_menu_principal()
    

# ===================================================================================================================================================================================================================================================================================================================================================================================
# MAIN
# função main sempre tem que estar como último item do script
def main():
    """
    Função para processar a escolha do usuário no menu principal
    """

    inicializar_banco()
    os.system('cls') # limpa a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# padrão para qualuer sistema de python, define o main como main
if __name__ == '__main__':
    main()
