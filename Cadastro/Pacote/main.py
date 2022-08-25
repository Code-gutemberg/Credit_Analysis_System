# Sistema de Análise de Crédito com manipulação de arquivo txt
from time import sleep
import interface
import data
import os

file_Pfisica = 'db_Pfisica.txt'
file_Pjuridica = 'db_Pjuridica.txt'
file_root = 'db_root'

if not data.file_exists(file_Pfisica):
    data.create_file(file_Pfisica)

if not data.file_exists(file_Pjuridica):
    data.create_file(file_Pjuridica)

if not data.file_exists(file_root):
    data.create_file(file_root)

while True:
    root = input('Nome do Usuário: ')
    password = input('Senha do Usuário: ')
    data.auth(file_root, root, password)
    if data.auth(file_root, root, password) == True:
        interface.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            # MENU Principal
            interface.title('SISTEMA DE ANÁLISE DE CRÉDITO')
            interface.subtitle()                               
            user = interface.read_int('Digite o código correspondente: ')
            # MENU Análise de Proposta de Crédito
            if user == 1:
                os.system('cls')
                interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                interface.submenu() # Opção PJ/PF
                while True:
                    user = interface.read_int('Digite o código correspondente: ')
                    if user == 1:    # SUBMENU Pessoa Física
                        os.system('cls')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                        cpf = 'Digite o CPF: '
                        reply_Pfisica = False
                        if data.query_Pfisica(file_Pfisica, cpf, reply_Pfisica) == False:
                            interface.title(f'USUÁRIO NÃO CADASTRADO')
                            while True:
                                user = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                                if user in 'S':
                                    os.system('cls')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO DE USUÁRIO')
                                    while True:
                                        name = str(input('Nome: '))
                                        if len(name) > 40:
                                            print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                        elif len(name) < 3:
                                            print(f'\033[31m ERRO, mínimo caracteres [3] \033[m')
                                        else:
                                            cpf = str(input('CPF: '))
                                            if '.' not in cpf:
                                                print(f'\033[31m ERRO, insira pontuações \033[m')
                                            elif '-' not in cpf:
                                                print(f'\033[31m ERRO, insira o hífen \033[m')
                                            elif len(cpf) < 14 and '.-' not in cpf:
                                                print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
                                            elif len(cpf) > 14:
                                                print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
                                            else:
                                                age = interface.read_int('Idade: ')
                                                income = data.read_coin('Renda Liquida: R$ ')
                                                break
                                    data.write_Pfisica(file_Pfisica, name, cpf, age, income)  # type: ignore
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('\033[31mERRO, digite SIM ou NÃO \033[m')
                            if user in 'N':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                            cpf = str(input('Digite novamente o CPF: '))
                            credit = float(input('Valor do Crédito: R$ '))
                            portion = int(input('Quantidade da Parcela: '))
                            query_Pfisica = data.credit_Pfisica(file_Pfisica, cpf, credit, portion)
                            stop = input()
                            os.system('cls')
                            break
                        
                    elif user == 2:  # SUBMENU Pessoa Jurídica
                        os.system('cls')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                        cnpj = 'Digite o CNPJ: '
                        reply_Pjuridica = False
                        if data.query_Pjuridica(file_Pjuridica, cnpj, reply_Pjuridica) == False:
                            interface.title(f'EMPRESA NÃO CADASTRADA')
                            while True:
                                user = str(input('Deseja Cadastrar uma Nova empresa [S/N]: ')).upper()[0]
                                if user in 'S':
                                    os.system('cls')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO DE EMPRESA')
                                    flow = list()
                                    while True:
                                        name = str(input('Nome da Empresa: '))
                                        if len(name) > 40:
                                            print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                        elif len(name) < 3:
                                            print(f'\033[31m ERRO, mínimo caracteres [3] \033[m')
                                        else:
                                            cnpj = str(input('CNPJ: '))
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
                                                size = str(input('Porte da empresa: '))
                                                capital = data.read_coin('Capital Imobilizado: R$ ')
                                                flow.append(data.read_coin('Fluxo de Caixa Mês 1/3: R$ '))
                                                flow.append(data.read_coin('Fluxo de Caixa Mês 2/3: R$ '))
                                                flow.append(data.read_coin('Fluxo de Caixa Mês 3/3: R$ '))
                                                dre = data.read_coin('Demonstração de Resultado do Exercício: R$ ')
                                                sum_flow = sum(flow)
                                                break
                                    data.write_Pjuridica(file_Pjuridica, name, cnpj, size, capital, sum_flow, dre)  # type: ignore
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('\033[31mERRO, digite SIM ou NÃO \033[m')
                            if user in 'N':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                            cnpj = str(input('Digite novamente o CNPJ: '))
                            credit = float(input('Valor do Crédito: R$ '))
                            portion = int(input('Quantidade da Parcela: '))
                            query_Pjuridica = data.credit_Pjuridica(file_Pjuridica, cnpj, credit, portion)
                            stop = input()
                            os.system('cls')
                            break
            # MENU Cadastro de Usuário                
            elif user == 2:
                os.system('cls')
                interface.title('[+] CADASTRAR USUÁRIO')
                interface.submenu()
                user = interface.read_int('Digite o código correspondente: ')
                if user == 1:    # SUBMENU Pessoa física
                    os.system('cls')
                    interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                    cpf = 'Digite o CPF: '
                    reply_Pfisica = False
                    if data.query_Pfisica_register(file_Pfisica, cpf, reply_Pfisica) == True:
                        interface.title(f'JÁ EXISTE CADASTRO DO USUÁRIO')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                        interface.title(f'USUÁRIO NÃO CADASTRADO')
                        while True:
                            user = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                            if user in 'S':
                                os.system('cls')
                                interface.title('[+] CADASTRAR USUÁRIO')
                                interface.title('[+] NOVO CADASTRO DE USUÁRIO')
                                while True:
                                    name = str(input('Nome: '))
                                    if len(name) > 40:
                                        print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                    elif len(name) < 3:
                                        print(f'\033[31m ERRO, mínimo caracteres [3] \033[m')
                                    else:
                                        cpf = str(input('CPF: '))
                                        if '.' not in cpf:
                                            print(f'\033[31m ERRO, insira pontuações \033[m')
                                        elif '-' not in cpf:
                                            print(f'\033[31m ERRO, insira o hífen \033[m')
                                        elif len(cpf) < 14 and '.-' not in cpf:
                                            print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
                                        elif len(cpf) > 14:
                                            print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
                                        else:
                                            age = interface.read_int('Idade: ')
                                            income = data.read_coin('Renda Liquida: R$ ')
                                            break
                                data.write_Pfisica(file_Pfisica, name, cpf, age, income)  # type: ignore
                            elif user in 'N':
                                os.system('cls')
                                break
                            else:
                                print('\033[31mERRO, digite SIM ou NÃO \033[m')
                        if user in 'N':
                            os.system('cls')
                            continue
                    
                elif user == 2:      # SUBMENU Pessoa Jurídica
                    os.system('cls')
                    interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                    cnpj = 'Digite o CNPJ: '
                    reply_Pjuridica = False
                    if data.query_Pjuridica_register(file_Pjuridica, cnpj, reply_Pjuridica) == True:
                        interface.title(f'JÁ EXISTE CADASTRO DA EMPRESA')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                        interface.title(f'EMPRESA NÃO CADASTRADA')
                        while True:
                            user = str(input('Deseja Cadastrar uma Nova empresa? [S/N]: ')).upper()[0]
                            if user in 'S':
                                os.system('cls')
                                flow = list()
                                while True:
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO DE EMPRESA')
                                    name = str(input('Nome da Empresa: '))
                                    if len(name) > 40:
                                        print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                    elif len(name) < 3:
                                        print(f'\033[31m ERRO, mínimo caracteres [3] \033[m')
                                    else:
                                        cnpj = str(input('CNPJ: '))
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
                                            size = str(input('Porte da empresa: '))
                                            capital = data.read_coin('Capital Imobilizado: R$ ')
                                            flow.append(data.read_coin('Fluxo de Caixa Mês 1/3: R$ '))
                                            flow.append(data.read_coin('Fluxo de Caixa Mês 2/3: R$ '))
                                            flow.append(data.read_coin('Fluxo de Caixa Mês 3/3: R$ '))
                                            dre = data.read_coin('Demonstração de Resultado do Exercício: R$ ')
                                            sum_flow = sum(flow)
                                            break
                                data.write_Pjuridica(file_Pjuridica, name, cnpj, size,
                                                                capital, sum_flow, dre)  # type: ignore
                            elif user in 'N':
                                break
                            else:
                                print('\033[31mERRO, digite SIM ou NÃO \033[m')
                        if user in 'N':
                            sleep(1)
                            os.system('cls')
                            continue
            # MENU Remover Usuário
            elif user == 3:
                os.system('cls')
                interface.title('[DEL] REMOVER USUÁRIO')
                interface.submenu()
                while True:
                    user = interface.read_int('Digite o código correspondente: ')
                    if user == 1:    # SUBMENU pessoa física
                        os.system('cls')
                        interface.title('[=] CONSULTA PESSOA FÍSICA NO BANCO DE DADOS')
                        cpf = 'Digite o CPF: '
                        reply_Pfisica = False
                        if data.query_Pfisica(file_Pfisica, cpf, reply_Pfisica) == False:
                            interface.title(f'USUÁRIO NÃO CADASTRADO')
                            sleep(2)
                            os.system('cls')
                            break
                        else:
                            while True:
                                user = str(input('Deseja excluir esse usuário? [S/N]: ')).upper()[0]
                                if user in 'S':
                                    cpf = 'Digite novamente o CPF: '
                                    data.delete_Pfisica(file_Pfisica, cpf)
                                    os.system('cls')
                                    interface.title(f'USUÁRIO EXCLUÍDO COM SUCESSO!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('\033[31mERRO, digite SIM ou NÃO \033[m')
                            if user in 'SN':
                                os.system('cls')
                                break
                        
                    elif user == 2:  # SUBMENU pessoa jurídica
                        os.system('cls')
                        interface.title('[=] CONSULTA PESSOA JURÍDICA NO BANCO DE DADOS')
                        cnpj = 'Digite o CNPJ: '
                        reply_Pjuridica = False
                        if data.query_Pjuridica(file_Pjuridica, cnpj, reply_Pjuridica) == False:
                            interface.title(f'EMPRESA NÃO CADASTRADA')
                            sleep(2)
                            os.system('cls')
                            break
                        else:
                            while True:
                                user = str(input('Deseja excluir essa empresa? [S/N]: ')).upper()[0]
                                if user in 'S':
                                    cnpj = 'Digite novamente o CNPJ: '
                                    data.delete_Pjuridica(file_Pjuridica, cnpj)
                                    os.system('cls')
                                    interface.title(f'EMPRESA EXCLUÍDA COM SUCESSO!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('\033[31mERRO, digite SIM ou NÃO \033[m')
                            if user in 'NS':
                                os.system('cls')
                                break
            # MENU Sair do Programa
            elif user == 4:
                interface.title('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                sleep(2)
                os.system('cls')
                break
            else:
                interface.error_code()
                sleep(1)
    else:
        print('Usuário ou senha inválido. Tente novamente')