# Sistema de Análise de Crédito com manipulação de arquivo txt
from time import sleep
import interface
import data
import treatment
import os

file_Pfisica = 'db_Pfisica.txt'
file_Pjuridica = 'db_Pjuridica.txt'
file_root = 'db_root.txt'

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
    if data.auth(file_root, root, password) is True:
        print('Checando banco de dados...')
        sleep(2)
        print(f'[SUCESS] - Usuário {root} Logado')
        interface.title('INICIANDO SISTEMA')
        sleep(2)
        os.system('cls')
        while True:
            # MENU Principal
            print(f'Usuário: {root}')
            interface.title('SISTEMA DE ANÁLISE DE CRÉDITO')
            interface.subtitle()
            menu = treatment.read_int('Digite o código correspondente: ')
            # MENU Análise de Proposta de Crédito
            if menu == 1:
                os.system('cls')
                print(f'Usuário: {root}')
                interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                interface.submenu()     # Opção PJ/PF
                while True:
                    submenu = treatment.read_int('Digite o código '
                                                 'correspondente: ')
                    if submenu == 1:    # SUBMENU Pessoa Física
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA')
                        cpf = 'Digite o CPF: '
                        if data.query_Pfisica(file_Pfisica, cpf) is False:
                            interface.title('USUÁRIO NÃO CADASTRADO')
                            while True:
                                user = str(input('Novo cadastro[S/N]: '))[0]
                                if user in 'Ss':
                                    os.system('cls')
                                    print(f'Usuário: {root}')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO')
                                    name = treatment.read_name('Nome: ')
                                    cpf = treatment.read_cpf('CPF: ')
                                    age = treatment.read_int('Idade: ')
                                    income = treatment.read_coin('Renda '
                                                                 'Liquida:R$ ')
                                    data.write_Pfisica(file_Pfisica, name, cpf,
                                                       age, income)
                                elif user in 'Nn':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'Nn':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE PROPOSTA DE CRÉDITO')
                            cpf = treatment.read_cpf('Digite novamente CPF: ')
                            credit = treatment.read_coin('Valor Crédito:R$ ')
                            portion = treatment.read_int('Quantas Parcelas: ')
                            credit_Pfisica = data.credit_Pfisica(
                                file_Pfisica,
                                cpf,
                                credit,
                                portion
                                )
                            stop = input()
                            os.system('cls')
                            break
                    elif submenu == 2:  # SUBMENU Pessoa Jurídica
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA')
                        cnpj = 'Digite o CNPJ: '
                        if data.query_Pjuridica(file_Pjuridica, cnpj) is False:
                            interface.title('EMPRESA NÃO CADASTRADA')
                            while True:
                                user = str(input('Novo cadastro[S/N]: '))[0]
                                if user in 'Ss':
                                    os.system('cls')
                                    print(f'Usuário: {root}')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO')
                                    flow = list()
                                    name = treatment.read_name('Nome: ')
                                    cnpj = treatment.read_cnpj('CNPJ: ')
                                    size = str(input('Porte: ')).upper()
                                    capital = treatment.read_coin(
                                        'Capital Imobilizado: R$ ')
                                    flow.append(treatment.read_coin(
                                        'Fluxo de Caixa Mês 1/3: R$ '))
                                    flow.append(treatment.read_coin(
                                        'Fluxo de Caixa Mês 2/3: R$ '))
                                    flow.append(treatment.read_coin(
                                        'Fluxo de Caixa Mês 3/3: R$ '))
                                    dre = treatment.read_coin(': R$ ')
                                    sum_flow = sum(flow)
                                    data.write_Pjuridica(file_Pjuridica,
                                                         name, cnpj,
                                                         size, capital,
                                                         sum_flow, dre)
                                elif user in 'Nn':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'Nn':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE PROPOSTA DE CRÉDITO')
                            cnpj = treatment.read_cnpj('Digite o CNPJ: ')
                            credit = treatment.read_coin('Crédito: R$ ')
                            portion = treatment.read_int('Parcela: ')
                            credit_Pjuridica = data.credit_Pjuridica(
                                file_Pjuridica, cnpj, credit, portion)
                            stop = input()
                            os.system('cls')
                            break
            # MENU Cadastro de Usuário
            elif menu == 2:
                os.system('cls')
                print(f'Usuário: {root}')
                interface.title('[+] CADASTRAR USUÁRIO')
                interface.submenu()
                submenu = treatment.read_int('Digite código correspondente: ')
                if submenu == 1:    # SUBMENU Pessoa física
                    os.system('cls')
                    print(f'Usuário: {root}')
                    interface.title('[=] CONSULTA DE PESSOA FÍSICA')
                    cpf = 'Digite o CPF: '
                    if data.query_Pfisica_register(file_Pfisica, cpf) is True:
                        interface.title('JÁ EXISTE CADASTRO DO USUÁRIO')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA')
                        interface.title('USUÁRIO NÃO CADASTRADO')
                        while True:
                            user = str(input('Novo cadastro:[S/N]: '))[0]
                            if user in 'Ss':
                                os.system('cls')
                                print(f'Usuário: {root}')
                                interface.title('[+] CADASTRAR USUÁRIO')
                                interface.title('[+] NOVO CADASTRO DE USUÁRIO')
                                name = treatment.read_name('Nome: ')
                                cpf = treatment.read_cpf('CPF: ')
                                age = treatment.read_int('Idade: ')
                                income = treatment.read_coin(
                                    'Renda Liquida: R$ ')
                                data.write_Pfisica(file_Pfisica,
                                                   name, cpf, age, income)
                            elif user in 'Nn':
                                os.system('cls')
                                break
                            else:
                                print('[ERROR] - Digite SIM ou NÃO')
                        if user in 'Nn':
                            os.system('cls')
                            continue
                elif submenu == 2:      # SUBMENU Pessoa Jurídica
                    os.system('cls')
                    print(f'Usuário: {root}')
                    interface.title('[=] CONSULTA DE PESSOA JURÍDICA')
                    cnpj = 'Digite o CNPJ: '
                    if data.query_Pjuridica_register(file_Pjuridica,
                                                     cnpj) is True:
                        interface.title('JÁ EXISTE CADASTRO DA EMPRESA')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA')
                        interface.title('EMPRESA NÃO CADASTRADA')
                        while True:
                            user = str(input('Novo cadastro[S/N]: '))[0]
                            if user in 'Ss':
                                os.system('cls')
                                print(f'Usuário: {root}')
                                flow = list()
                                interface.title('[+] CADASTRAR USUÁRIO')
                                interface.title('[+] NOVO CADASTRO DE EMPRESA')
                                name = treatment.read_name('Nome da Empresa: ')
                                cnpj = treatment.read_cnpj('CNPJ: ')
                                size = str(input('Porte da empresa: ')).upper()
                                capital = treatment.read_coin(
                                    'Capital Imobilizado: R$ ')
                                flow.append(treatment.read_coin(
                                    'Fluxo de Caixa Mês 1/3: R$ '))
                                flow.append(treatment.read_coin(
                                    'Fluxo de Caixa Mês 2/3: R$ '))
                                flow.append(treatment.read_coin(
                                    'Fluxo de Caixa Mês 3/3: R$ '))
                                dre = treatment.read_coin('DRE: R$ ')
                                sum_flow = sum(flow)
                                data.write_Pjuridica(file_Pjuridica,
                                                     name, cnpj, size,
                                                     capital, sum_flow, dre)
                            elif user in 'Nn':
                                break
                            else:
                                print('[ERROR] - Digite SIM ou NÃO')
                        if user in 'Nn':
                            sleep(1)
                            os.system('cls')
                            continue
            # MENU Remover Usuário
            elif menu == 3:
                os.system('cls')
                print(f'Usuário: {root}')
                interface.title('[DEL] REMOVER USUÁRIO')
                interface.submenu()
                while True:
                    submenu = treatment.read_int(
                        'Digite código correspondente: ')
                    if submenu == 1:    # SUBMENU pessoa física
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA PESSOA FÍSICA')
                        cpf = 'Digite o CPF: '
                        if data.query_Pfisica(file_Pfisica, cpf) is False:
                            interface.title('USUÁRIO NÃO CADASTRADO')
                            sleep(2)
                            os.system('cls')
                            break
                        else:
                            while True:
                                user = str(input('Excluir? [S/N]: '))[0]
                                if user in 'Ss':
                                    cpf = 'Digite novamente o CPF: '
                                    data.delete_Pfisica(file_Pfisica, cpf)
                                    interface.title('[SUCESS] '
                                                    'USUÁRIO EXCLUÍDO!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'Nn':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'SsNn':
                                os.system('cls')
                                break
                    elif submenu == 2:  # SUBMENU pessoa jurídica
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA PESSOA JURÍDICA')
                        cnpj = 'Digite o CNPJ: '
                        if data.query_Pjuridica(file_Pjuridica, cnpj) is False:
                            interface.title('EMPRESA NÃO CADASTRADA')
                            sleep(2)
                            os.system('cls')
                            break
                        else:
                            while True:
                                user = str(input('Excluir empresa?[S/N]: '))[0]
                                if user in 'Ss':
                                    cnpj = 'Digite novamente o CNPJ: '
                                    data.delete_Pjuridica(file_Pjuridica, cnpj)
                                    interface.title('[SUCESS] '
                                                    'EMPRESA EXCLUÍDA!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'Nn':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'NnSs':
                                os.system('cls')
                                break
            # MENU Sair do Programa
            elif menu == 4:
                interface.title('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                sleep(2)
                os.system('cls')
                break
            else:
                interface.error_code()
                sleep(2)
                os.system('cls')
                continue
        break
    else:
        print('[ERROR] - Usuário ou senha inválido. Tente novamente')
