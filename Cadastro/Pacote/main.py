# Sistema de Análise de Crédito com manipulação de arquivo txt
from time import sleep
import interface, data, treatment
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
    if data.auth(file_root, root, password) == True:
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
                interface.submenu() # Opção PJ/PF
                while True:
                    submenu = treatment.read_int('Digite o código correspondente: ')
                    if submenu == 1:    # SUBMENU Pessoa Física
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                        cpf = 'Digite o CPF: '
                        if data.query_Pfisica(file_Pfisica, cpf) == False:
                            interface.title(f'USUÁRIO NÃO CADASTRADO')
                            while True:
                                user = str(input('Deseja Cadastrar um Novo cliente [S/N]: ')).upper()[0]
                                if user in 'S':
                                    os.system('cls')
                                    print(f'Usuário: {root}')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO DE USUÁRIO')
                                    name = treatment.read_name('Nome: ')
                                    cpf = treatment.read_cpf('CPF: ')
                                    age = treatment.read_int('Idade: ')
                                    income = treatment.read_coin('Renda Liquida: R$ ')
                                    data.write_Pfisica(file_Pfisica, name, cpf, age, income)
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'N':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                            cpf = treatment.read_cpf('Digite novamente o CPF: ')
                            credit = treatment.read_coin('Valor do Crédito: R$ ')
                            portion = treatment.read_int('Quantidade da Parcela: ')
                            credit_Pfisica = data.credit_Pfisica(file_Pfisica, cpf, credit, portion)
                            stop = input()
                            os.system('cls')
                            break
                        
                    elif submenu == 2:  # SUBMENU Pessoa Jurídica
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                        cnpj = 'Digite o CNPJ: '
                        if data.query_Pjuridica(file_Pjuridica, cnpj) == False:
                            interface.title(f'EMPRESA NÃO CADASTRADA')
                            while True:
                                user = str(input('Deseja Cadastrar uma Nova empresa [S/N]: ')).upper()[0]
                                if user in 'S':
                                    os.system('cls')
                                    print(f'Usuário: {root}')
                                    interface.title('[+] CADASTRAR USUÁRIO')
                                    interface.title('[+] NOVO CADASTRO DE EMPRESA')
                                    flow = list()
                                    name = treatment.read_name('Nome da Empresa: ')
                                    cnpj = treatment.read_cnpj('CNPJ: ')
                                    size = str(input('Porte da empresa: ')).upper()
                                    capital = treatment.read_coin('Capital Imobilizado: R$ ')
                                    flow.append(treatment.read_coin('Fluxo de Caixa Mês 1/3: R$ '))
                                    flow.append(treatment.read_coin('Fluxo de Caixa Mês 2/3: R$ '))
                                    flow.append(treatment.read_coin('Fluxo de Caixa Mês 3/3: R$ '))
                                    dre = treatment.read_coin('Demonstração de Resultado do Exercício: R$ ')
                                    sum_flow = sum(flow)
                                    data.write_Pjuridica(file_Pjuridica, name, cnpj, size, capital, sum_flow, dre)
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'N':
                                os.system('cls')
                                break
                        else:
                            interface.title('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                            cnpj = treatment.read_cnpj('Digite novamente o CNPJ: ')
                            credit = treatment.read_coin('Valor do Crédito: R$ ')
                            portion = treatment.read_int('Quantidade da Parcela: ')
                            credit_Pjuridica = data.credit_Pjuridica(file_Pjuridica, cnpj, credit, portion)
                            stop = input()
                            os.system('cls')
                            break
            # MENU Cadastro de Usuário                
            elif menu == 2:
                os.system('cls')
                print(f'Usuário: {root}')
                interface.title('[+] CADASTRAR USUÁRIO')
                interface.submenu()
                submenu = treatment.read_int('Digite o código correspondente: ')
                if submenu == 1:    # SUBMENU Pessoa física
                    os.system('cls')
                    print(f'Usuário: {root}')
                    interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                    cpf = 'Digite o CPF: '
                    if data.query_Pfisica_register(file_Pfisica, cpf) == True:
                        interface.title(f'JÁ EXISTE CADASTRO DO USUÁRIO')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                        interface.title(f'USUÁRIO NÃO CADASTRADO')
                        while True:
                            user = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                            if user in 'S':
                                os.system('cls')
                                print(f'Usuário: {root}')
                                interface.title('[+] CADASTRAR USUÁRIO')
                                interface.title('[+] NOVO CADASTRO DE USUÁRIO')
                                name = treatment.read_name('Nome: ')
                                cpf = treatment.read_cpf('CPF: ')
                                age = treatment.read_int('Idade: ')
                                income = treatment.read_coin('Renda Liquida: R$ ')
                                data.write_Pfisica(file_Pfisica, name, cpf, age, income)
                            elif user in 'N':
                                os.system('cls')
                                break
                            else:
                                print('[ERROR] - Digite SIM ou NÃO')
                        if user in 'N':
                            os.system('cls')
                            continue
                    
                elif submenu == 2:      # SUBMENU Pessoa Jurídica
                    os.system('cls')
                    print(f'Usuário: {root}')
                    interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                    cnpj = 'Digite o CNPJ: '
                    if data.query_Pjuridica_register(file_Pjuridica, cnpj) == True:
                        interface.title(f'JÁ EXISTE CADASTRO DA EMPRESA')
                        sleep(2)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                        interface.title(f'EMPRESA NÃO CADASTRADA')
                        while True:
                            user = str(input('Deseja Cadastrar uma Nova empresa? [S/N]: ')).upper()[0]
                            if user in 'S':
                                os.system('cls')
                                print(f'Usuário: {root}')
                                flow = list()
                                interface.title('[+] CADASTRAR USUÁRIO')
                                interface.title('[+] NOVO CADASTRO DE EMPRESA')
                                name = treatment.read_name('Nome da Empresa: ')
                                cnpj = treatment.read_cnpj('CNPJ: ')
                                size = str(input('Porte da empresa: ')).upper()
                                capital = treatment.read_coin('Capital Imobilizado: R$ ')
                                flow.append(treatment.read_coin('Fluxo de Caixa Mês 1/3: R$ '))
                                flow.append(treatment.read_coin('Fluxo de Caixa Mês 2/3: R$ '))
                                flow.append(treatment.read_coin('Fluxo de Caixa Mês 3/3: R$ '))
                                dre = treatment.read_coin('Demonstração de Resultado do Exercício: R$ ')
                                sum_flow = sum(flow)
                                data.write_Pjuridica(file_Pjuridica, name, cnpj, size, capital, sum_flow, dre)
                            elif user in 'N':
                                break
                            else:
                                print('[ERROR] - Digite SIM ou NÃO')
                        if user in 'N':
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
                    submenu = treatment.read_int('Digite o código correspondente: ')
                    if submenu == 1:    # SUBMENU pessoa física
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA PESSOA FÍSICA NO BANCO DE DADOS')
                        cpf = 'Digite o CPF: '
                        if data.query_Pfisica(file_Pfisica, cpf) == False:
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
                                    interface.title(f'[SUCESS] - USUÁRIO EXCLUÍDO COM SUCESSO!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'SN':
                                os.system('cls')
                                break
                        
                    elif submenu == 2:  # SUBMENU pessoa jurídica
                        os.system('cls')
                        print(f'Usuário: {root}')
                        interface.title('[=] CONSULTA PESSOA JURÍDICA NO BANCO DE DADOS')
                        cnpj = 'Digite o CNPJ: '
                        if data.query_Pjuridica(file_Pjuridica, cnpj) == False:
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
                                    interface.title(f'[SUCESS] - EMPRESA EXCLUÍDA COM SUCESSO!')
                                    sleep(2)
                                    os.system('cls')
                                    break
                                elif user in 'N':
                                    os.system('cls')
                                    break
                                else:
                                    print('[ERROR] - Digite SIM ou NÃO')
                            if user in 'NS':
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