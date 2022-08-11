'''FUNÇÕES PARA TESTAR, CRIAR, ABRIR E ALIMENTAR DOIS BANCOS DE DADOS EM TXT'''
from aifc import Error
from random import randint
import interface
from time import sleep
import os


def arquivo_existe(banco_dados):
    """Descrição
    Função para testar se existe arquivo txt criado.
    Parâmetro:
        entrada(str): recebe uma string.
    Retorno:
        bool: Retorna falso ou verdadeiro
    """
    try:
        arquivo = open(banco_dados, 'rt')    # r = read e t = texto
        arquivo.close()
    except FileNotFoundError:   # exceção de arquivo inexistente
        print(f'\033[0;31mArquivo {banco_dados} não existe!\033[m')
        return False
    else:
        return True


def criar_arquivo(banco_dados):
    """Descrição
    Função para criar arquivo.
    Parâmetro:
        entrada(str): recebe uma string.
    """
    try:
        criar = open(banco_dados, 'wt+')   # w = Write, t = texto, + = adicionar
        criar.close()
    except (Error):
        print('\033[0;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[0;31mAquivo {banco_dados} criado com sucesso!\033[m')


def escrever_Pfisica(db_Pfisica, nome='', cpf='', idade=0, renda=0):
    id = 0
    try:
        escrever = open(db_Pfisica, 'at+')  # a = append, t = texto, + = adicionar
    except (Error):
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            id = randint(0, 100)
            escrever.write(f'{id};{nome};{cpf};{idade};{interface.Real(renda)}\n')
        except (Error):
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.titulo(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            escrever.close()


def escrever_Pjuridica(db_Pjuridica, nome='', cnpj='', porte='', capital=0, fluxo=0, dre=0):
    id = 0
    try:
        escrever = open(db_Pjuridica, 'at+')  # a = append, t = texto, + = adicionar
    except (Error):
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            id = randint(0, 100)
            escrever.write(f'{id};{nome};{cnpj};{porte};')
            escrever.write(
                f'{interface.Real(capital)};{interface.Real(fluxo)};{interface.Real(dre)}\n')
        except (Error):
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.titulo(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            escrever.close()


def ler_moeda(valor):
    while True:
        valido = False
        while not valido:
            cifrada = str(input(valor)).replace(',', '.').strip()
            if cifrada.isalpha() or cifrada == '':
                print(f'ERRO, [{cifrada}] é um preço inválido!')
            else:
                try:
                    valido = True
                    return float(cifrada)
                except ValueError:
                    print('ERRO, não inserir pontuação no inicio do valor.'
                          ' Insira na penúltima casa decimal.')
                    continue


def query_Pfisica(db_Pfisica, consulta, saida=False):
    try:
        ler = open(db_Pfisica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cpf = str(input(consulta))
            if '.' not in cpf:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '-' not in cpf:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cpf) < 14 and '.-' not in cpf:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cpf) > 14:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cpf in dado:
                print('=' * 50)
                print('DADOS DO USUÁRIO'.center(50))
                print('=' * 50)
                print()
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome: "}{dado[1]}')
                print(f'{"CPF: "}{dado[2]}')
                print(f'{"Idade: "}{dado[3]} anos')
                print(f'{"Renda Líquida: "}{dado[4]}')
                print('=' * 50)
                saida = True
                return saida
        return False


def query_Pjuridica(db_Pjrudica, consulta, saida=False):
    try:
        ler = open(db_Pjrudica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cnpj = str(input(consulta))
            if '.' not in cnpj:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '/' not in cnpj:
                print(f'\033[31m ERRO, insira a barra \033[m')
            elif '-' not in cnpj:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cnpj) < 18 and '.-' not in cnpj:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cnpj) > 18:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cnpj in dado:
                print('=' * 50)
                print('DADOS DA EMPRESA'.center(50))
                print('=' * 50)
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome da Empresa: "}{dado[1]}')
                print(f'{"CNPJ: "}{dado[2]}')
                print(f'{"Porte: "}{dado[3]}')
                print(f'{"Capital Imobilizado: "}{dado[4]}')
                print(f'{"Fluxo de Caixa: "}{dado[5]}')
                print(f'{"DRE: "}{dado[6]}')
                print('=' * 50)
                saida = True
                return saida
        return False
            

def query_Pfisica_cadastro(db_Pfisica, consulta, saida=False):
    try:
        ler = open(db_Pfisica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cpf = str(input(consulta))
            if '.' not in cpf:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '-' not in cpf:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cpf) < 14 and '.-' not in cpf:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cpf) > 14:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cpf in dado:
                saida = True
                return saida
        return False


def query_Pjuridica_cadastro(db_Pjrudica, consulta, saida=False):
    try:
        ler = open(db_Pjrudica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cnpj = str(input(consulta))
            if '.' not in cnpj:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '/' not in cnpj:
                print(f'\033[31m ERRO, insira a barra \033[m')
            elif '-' not in cnpj:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cnpj) < 18 and '.-' not in cnpj:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cnpj) > 18:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cnpj == dado[2]:
                saida = True
                return saida
        return False


def query_Pfisica_excluir(db_Pfisica, consulta, saida=False):
    try:
        ler = open(db_Pfisica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cpf = str(input(consulta))
            if '.' not in cpf:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '-' not in cpf:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cpf) < 14 and '.-' not in cpf:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cpf) > 14:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cpf in dado:
                os.system('cls')
                interface.titulo('[DEL] REMOVER USUÁRIO')
                interface.titulo('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                print('DADOS DO USUÁRIO'.center(50))
                print()
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome: "}{dado[1]}')
                print(f'{"CPF: "}{dado[2]}')
                print(f'{"Idade: "}{dado[3]} anos')
                print(f'{"Renda Líquida: "}{dado[4]}')
                print('=' * 50)
                saida = True
                return saida
        return False
    

def query_Pjuridica_excluir(db_Pjrudica, consulta, saida=False):
    try:
        ler = open(db_Pjrudica, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        while True:
            cnpj = str(input(consulta))
            if '.' not in cnpj:
                print(f'\033[31m ERRO, insira pontuações \033[m')
            elif '/' not in cnpj:
                print(f'\033[31m ERRO, insira a barra \033[m')
            elif '-' not in cnpj:
                print(f'\033[31m ERRO, insira o hífen \033[m')
            elif len(cnpj) < 18 and '.-' not in cnpj:
                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
            elif len(cnpj) > 18:
                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
            else:
                break
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if cnpj in dado:
                os.system('cls')
                interface.titulo('[DEL] REMOVER USUÁRIO')
                interface.titulo('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                print('DADOS DA EMPRESA'.center(50))
                print()
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome da Empresa: "}{dado[1]}')
                print(f'{"CNPJ: "}{dado[2]}')
                print(f'{"Porte: "}{dado[3]}')
                print(f'{"Capital Imobilizado: "}{dado[4]}')
                print(f'{"Fluxo de Caixa: "}{dado[5]}')
                print(f'{"DRE: "}{dado[6]}')
                print('=' * 50)
                saida = True
                return saida
        return False