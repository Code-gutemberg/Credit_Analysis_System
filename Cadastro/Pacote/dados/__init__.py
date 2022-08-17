'''FUNÇÕES PARA TESTAR, CRIAR, ABRIR E ALIMENTAR DOIS BANCOS DE DADOS EM TXT'''
from aifc import Error
from random import randint
import interface
from time import sleep

def autenticacao(db_root, usuario='', senha=''):
    root = usuario
    senha_root = senha
    ler = open(db_root, 'rt')
    for linha in ler:
        dado = linha.split(';')
        if root in dado[0] and senha_root in dado[1]:
            return True
        else:
            return False


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


def excluir_Pfisica(db_Pfisica, consulta):
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
    with open(db_Pfisica, 'r') as ler:
        linhas = ler.readlines()
    
    with open(db_Pfisica, 'w', encoding='utf8') as escrever:
        for linha in linhas:
            if cpf in linha:
                escrever.write('')
            else:
                escrever.write(linha)


def excluir_Pjuridica(db_Pjuridica, consulta):
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
    with open(db_Pjuridica, 'r') as ler:
        linhas = ler.readlines()
    
    with open(db_Pjuridica, 'w', encoding='utf8') as escrever:
        for linha in linhas:
            if cnpj in linha:
                escrever.write('')
            else:
                escrever.write(linha)


def credito_Pfisica(db_Pfisica, consulta='', credito=0.0, parcela=0):
    cpf = consulta
    ler = open(db_Pfisica, 'rt')
    for linha in ler:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        if cpf in dado:
            saida = dado[4].strip('\n').strip('R$ ').replace(',', '.')
            # Script para remover tudo que identifique como string
            emprestimo = credito / parcela
            if emprestimo > float(saida):
                interface.titulo('EMPRÉSTIMO REPROVADO')
            else:
                interface.titulo('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome: "}{dado[1]}')
                print(f'{"CPF: "}{dado[2]}')
                print(f'Valor do Crédito: {interface.Real(credito)}')
                print(f'Duração do Contrato: {parcela} meses')
                print(f'Valor da Parcela: {interface.Real(emprestimo)}')


def credito_Pjuridica(db_Pjuridica, consulta='', credito=0.0, parcela=0):
    cnpj = consulta
    ler = open(db_Pjuridica, 'rt')
    for linha in ler:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        if cnpj in dado:
            imobilizado = float(dado[4].strip('\n').strip('R$ ').replace(',', '.'))
            fluxo = float(dado[5].strip('\n').strip('R$ ').replace(',', '.'))
            dre = float(dado[6].strip('\n').strip('R$ ').replace(',', '.'))
            # Scripts para remover tudo que identifique como string
            risco_1 = (imobilizado * 30) / 100      # 30% do imobilizado como garantia
            risco_2 = (fluxo * 30) / 100    # 30% da soma(3 ultimos meses) do fluxo de caixa como garantia
            risco_3 = (dre * 30) / 100      # 30% do DRE como garantia
            if risco_1 >= credito or risco_2 >= credito/parcela or risco_3 >= credito:
                interface.titulo('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{dado[0]}')
                print(f'{"Nome da empresa: "}{dado[1]}')
                print(f'{"CNPJ: "}{dado[2]}')
                print(f'Valor do Crédito: {interface.Real(credito)}')
                print(f'Duração do Contrato: {parcela} meses')
                print(f'Valor da Parcela: {interface.Real(credito/parcela)}')
            else:
                interface.titulo('EMPRÉSTIMO REPROVADO')
    