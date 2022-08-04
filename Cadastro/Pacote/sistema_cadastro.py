# Sistema de Cadastro com banco de dados em texto
from time import sleep
import interface
import dados


arquivo = 'banco_dados.txt'

if not dados.arquivo_existe(arquivo):   # Se não existir o arquivo.txt, cria-se
    dados.criar_arquivo(arquivo)        # Cria um arquivo.txt

while True:
    interface.titulo('MENU PRINCIPAL')
    interface.subtitulo()       # Chama as opções do programa
    usuario = interface.LeiaInt('Escolha uma das opções: ')
    if usuario == 1:
        dados.ler_arquivo(arquivo)
    elif usuario == 2:
        interface.titulo('[+] NOVO CADASTRO')
        while True:
            nome = str(input('Nome: '))
            if len(nome) > 40:
                print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
            elif len(nome) < 3:
                print(f'\033[31m ERRO, mínimo caracteres [3] \033[m')
            else:
                idade = interface.LeiaInt('Idade: ')
                break
        dados.escrever_arquivo(arquivo, nome, idade)  # type: ignore
    elif usuario == 3:
        interface.titulo('PROGRAMA ENCERRADO COM SUCESSO!')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO, Digite um número válido.\033[m')
        sleep(2)
