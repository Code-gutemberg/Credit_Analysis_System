'''FUNÇÕES PARA TESTAR, CRIAR, ABRIR E ALIMENTAR UM BANCO DE DADOS EM TXT'''

from aifc import Error
import interface
from time import sleep


def arquivo_existe(entrada):
    """Descrição
    Função para testar se existe arquivo txt criado.
    Parâmetro:
        entrada(str): recebe uma string.
    Retorno:
        bool: Retorna falso ou verdadeiro
    """
    try:
        arquivo = open(entrada, 'rt')    # r = read e t = texto
        arquivo.close()
    except FileNotFoundError:   # exceção de arquivo inexistente
        print(f'\033[0;31mArquivo {entrada} não existe!\033[m')
        return False
    else:
        return True


def criar_arquivo(entrada):
    """Descrição
    Função para criar arquivo.
    Parâmetro:
        entrada(str): recebe uma string.
    """
    try:
        criar = open(entrada, 'wt+')   # w = Write, t = texto, + = adicionar
        criar.close()
    except (Error):
        print('\033[0;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[0;31mAquivo {entrada} criado com sucesso!\033[m')


def ler_arquivo(entrada):
    """Descrição:
    Função para ler arquivo. Ex: txt.
    Parâmetro:
        entrada(str): recebe uma string.
    """
    try:
        ler = open(entrada, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        interface.pessoas_cadastradas()
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}', end='')
            print(f'{dado[1].rjust(4)} anos')
        sleep(2)


def escrever_arquivo(entrada, nome='desconhecido', idade=0):
    """Descrição:
    Função para escrever informações no arquivo criado.
    Parâmetros:
        entrada(str): recebe uma string.
        nome(str, opcional): recebe uma string. Padrão: 'desconhecido'.
        idade(int, opcional): recebe um inteiro. Padrão: 0.
    """
    try:
        escrever = open(entrada, 'at+')  # a = append, t = texto, + = adicionar
    except (Error):
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            escrever.write(f'{nome};{idade}\n')
        except (Error):
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.titulo(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            escrever.close()
