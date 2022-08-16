# Sistema de Cadastro com banco de dados em texto
from time import sleep
import interface
import dados
import os

arquivo_Pfisica = 'banco_dados_Pfisica.txt' # Define o nome do banco de dados Pessoa Fisica
arquivo_Pjuridica = 'banco_dados_Pjuridica.txt' # Define o nome do banco de dados Pessoa Juridica

if not dados.arquivo_existe(arquivo_Pfisica):   # Se não existir o db_Pfisica.txt, cria-se
    dados.criar_arquivo(arquivo_Pfisica)
if not dados.arquivo_existe(arquivo_Pjuridica): # Se não existir o db_Pjuridica.txt, cria-se
    dados.criar_arquivo(arquivo_Pjuridica)

while True:
    interface.titulo('SISTEMA DE ANÁLISE DE CRÉDITO')   # MENU Principal
    interface.subtitulo()                               # MENU Principal
    usuario = interface.LeiaInt('Digite o código correspondente: ')
    if usuario == 1:        # MENU Análise de Proposta de Crédito
        os.system('cls')
        interface.titulo('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
        interface.submenu() # Opção PJ/PF
        while True:
            usuario = interface.LeiaInt('Digite o código correspondente: ')
            if usuario == 1:        # SUBMENU Pessoa Física
                os.system('cls')
                interface.titulo('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                cpf = 'Digite o CPF: '
                resposta_Pfisica = False
                if dados.query_Pfisica(arquivo_Pfisica, cpf, resposta_Pfisica) == False:
                    interface.titulo(f'USUÁRIO NÃO CADASTRADO')
                    while True:
                        usuario = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                        if usuario in 'S':
                            os.system('cls')
                            interface.titulo('[+] CADASTRAR USUÁRIO')
                            interface.titulo('[+] NOVO CADASTRO DE USUÁRIO')
                            while True:
                                nome = str(input('Nome: '))
                                if len(nome) > 40:
                                    print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                elif len(nome) < 3:
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
                                        idade = interface.LeiaInt('Idade: ')
                                        renda = dados.ler_moeda('Renda Liquida: R$ ')
                                        break
                            dados.escrever_Pfisica(arquivo_Pfisica, nome, cpf, idade, renda)  # type: ignore
                        elif usuario in 'N':
                            os.system('cls')
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'N':
                        os.system('cls')
                        break
                else:
                    interface.titulo('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                    cpf = str(input('Digite novamente o CPF: '))
                    credito = float(input('Valor do Crédito: R$ '))
                    parcela = int(input('Quantidade da Parcela: '))
                    query_Pfisica = dados.credito_Pfisica(arquivo_Pfisica, cpf, credito, parcela)
                    segura = input()
                    os.system('cls')
                    break
                
            elif usuario == 2:      # SUBMENU Pessoa Jurídica
                os.system('cls')
                interface.titulo('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                cnpj = 'Digite o CNPJ: '
                resposta_Pjuridica = False
                if dados.query_Pjuridica(arquivo_Pjuridica, cnpj, resposta_Pjuridica) == False:
                    interface.titulo(f'EMPRESA NÃO CADASTRADA')
                    while True:
                        usuario = str(input('Deseja Cadastrar uma Nova empresa [S/N]: ')).upper()[0]
                        if usuario in 'S':
                            os.system('cls')
                            interface.titulo('[+] CADASTRAR USUÁRIO')
                            interface.titulo('[+] NOVO CADASTRO DE EMPRESA')
                            fluxo = list()
                            while True:
                                nome = str(input('Nome da Empresa: '))
                                if len(nome) > 40:
                                    print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                                elif len(nome) < 3:
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
                                        porte = str(input('Porte da empresa: '))
                                        capital = dados.ler_moeda('Capital Imobilizado: R$ ')
                                        fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 1/3: R$ '))
                                        fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 2/3: R$ '))
                                        fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 3/3: R$ '))
                                        dre = dados.ler_moeda('Demonstração de Resultado do Exercício: R$ ')
                                        soma_fluxo = sum(fluxo)
                                        break
                            dados.escrever_Pjuridica(arquivo_Pjuridica, nome, cnpj, porte, capital, soma_fluxo, dre)  # type: ignore
                        elif usuario in 'N':
                            os.system('cls')
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'N':
                        os.system('cls')
                        break
                else:
                    interface.titulo('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
                    cnpj = str(input('Digite novamente o CNPJ: '))
                    credito = float(input('Valor do Crédito: R$ '))
                    parcela = int(input('Quantidade da Parcela: '))
                    query_Pjuridica = dados.credito_Pjuridica(arquivo_Pjuridica, cnpj, credito, parcela)
                    segura = input()
                    os.system('cls')
                    break

    elif usuario == 2:      # MENU Cadastro de Usuário
        os.system('cls')
        interface.titulo('[+] CADASTRAR USUÁRIO')
        interface.submenu()
        usuario = interface.LeiaInt('Digite o código correspondente: ')
        if usuario == 1:    # SUBMENU Pessoa física
            os.system('cls')
            interface.titulo('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
            cpf = 'Digite o CPF: '
            resposta_Pfisica = False
            if dados.query_Pfisica_cadastro(arquivo_Pfisica, cpf, resposta_Pfisica) == True:
                interface.titulo(f'JÁ EXISTE CADASTRO DO USUÁRIO')
                sleep(2)
                os.system('cls')
                continue
            else:
                os.system('cls')
                interface.titulo('[=] CONSULTA DE PESSOA FÍSICA NO BANCO DE DADOS')
                interface.titulo(f'USUÁRIO NÃO CADASTRADO')
                while True:
                    usuario = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                    if usuario in 'S':
                        os.system('cls')
                        interface.titulo('[+] CADASTRAR USUÁRIO')
                        interface.titulo('[+] NOVO CADASTRO DE USUÁRIO')
                        while True:
                            nome = str(input('Nome: '))
                            if len(nome) > 40:
                                print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                            elif len(nome) < 3:
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
                                    idade = interface.LeiaInt('Idade: ')
                                    renda = dados.ler_moeda('Renda Liquida: R$ ')
                                    break
                        dados.escrever_Pfisica(arquivo_Pfisica, nome, cpf, idade, renda)  # type: ignore
                    elif usuario in 'N':
                        os.system('cls')
                        break
                    else:
                        print('\033[31mERRO, digite SIM ou NÃO \033[m')
                if usuario in 'N':
                    os.system('cls')
                    continue
            
        elif usuario == 2:      # SUBMENU Pessoa Jurídica
            os.system('cls')
            interface.titulo('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
            cnpj = 'Digite o CNPJ: '
            resposta_Pjuridica = False
            if dados.query_Pjuridica_cadastro(arquivo_Pjuridica, cnpj, resposta_Pjuridica) == True:
                interface.titulo(f'JÁ EXISTE CADASTRO DA EMPRESA')
                sleep(2)
                os.system('cls')
                continue
            else:
                os.system('cls')
                interface.titulo('[=] CONSULTA DE PESSOA JURÍDICA NO BANCO DE DADOS')
                interface.titulo(f'EMPRESA NÃO CADASTRADA')
                while True:
                    usuario = str(input('Deseja Cadastrar uma Nova empresa? [S/N]: ')).upper()[0]
                    if usuario in 'S':
                        os.system('cls')
                        fluxo = list()
                        while True:
                            interface.titulo('[+] CADASTRAR USUÁRIO')
                            interface.titulo('[+] NOVO CADASTRO DE EMPRESA')
                            nome = str(input('Nome da Empresa: '))
                            if len(nome) > 40:
                                print(f'\033[31m ERRO, máximo caracteres [40] \033[m')
                            elif len(nome) < 3:
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
                                    porte = str(input('Porte da empresa: '))
                                    capital = dados.ler_moeda('Capital Imobilizado: R$ ')
                                    fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 1/3: R$ '))
                                    fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 2/3: R$ '))
                                    fluxo.append(dados.ler_moeda('Fluxo de Caixa Mês 3/3: R$ '))
                                    dre = dados.ler_moeda('Demonstração de Resultado do Exercício: R$ ')
                                    soma_fluxo = sum(fluxo)
                                    break
                        dados.escrever_Pjuridica(arquivo_Pjuridica, nome, cnpj, porte,
                                                        capital, soma_fluxo, dre)  # type: ignore
                    elif usuario in 'N':
                        break
                    else:
                        print('\033[31mERRO, digite SIM ou NÃO \033[m')
                if usuario in 'N':
                    sleep(1)
                    os.system('cls')
                    continue

    elif usuario == 3:      # MENU Remover Usuário
        os.system('cls')
        interface.titulo('[DEL] REMOVER USUÁRIO')
        interface.submenu()
        while True:
            usuario = interface.LeiaInt('Digite o código correspondente: ')
            if usuario == 1:    # SUBMENU pessoa física
                os.system('cls')
                interface.titulo('[=] CONSULTA PESSOA FÍSICA NO BANCO DE DADOS')
                cpf = 'Digite o CPF: '
                resposta_Pfisica = False
                if dados.query_Pfisica(arquivo_Pfisica, cpf, resposta_Pfisica) == False:
                    interface.titulo(f'USUÁRIO NÃO CADASTRADO')
                    sleep(2)
                    os.system('cls')
                    break
                else:
                    while True:
                        usuario = str(input('Deseja excluir esse usuário? [S/N]: ')).upper()[0]
                        if usuario in 'S':
                            cpf = 'Digite novamente o CPF: '
                            dados.excluir_Pfisica(arquivo_Pfisica, cpf)
                            os.system('cls')
                            interface.titulo(f'USUÁRIO EXCLUÍDO COM SUCESSO!')
                            sleep(2)
                            os.system('cls')
                            break
                        elif usuario in 'N':
                            os.system('cls')
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'NS':
                        os.system('cls')
                        break
                
            elif usuario == 2:  # SUBMENU pessoa jurídica
                os.system('cls')
                interface.titulo('[=] CONSULTA PESSOA JURÍDICA NO BANCO DE DADOS')
                cnpj = 'Digite o CNPJ: '
                resposta_Pjuridica = False
                if dados.query_Pjuridica(arquivo_Pjuridica, cnpj, resposta_Pjuridica) == False:
                    interface.titulo(f'EMPRESA NÃO CADASTRADA')
                    sleep(2)
                    os.system('cls')
                    break
                else:
                    while True:
                        usuario = str(input('Deseja excluir essa empresa? [S/N]: ')).upper()[0]
                        if usuario in 'S':
                            cnpj = 'Digite novamente o CNPJ: '
                            dados.excluir_Pjuridica(arquivo_Pjuridica, cnpj)
                            os.system('cls')
                            interface.titulo(f'EMPRESA EXCLUÍDA COM SUCESSO!')
                            sleep(2)
                            os.system('cls')
                            break
                        elif usuario in 'N':
                            os.system('cls')
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'NS':
                        os.system('cls')
                        break

    elif usuario == 4:      # MENU Sair do Programa
        interface.titulo('[!] PROGRAMA ENCERRADO COM SUCESSO!')
        sleep(2)
        os.system('cls')
        break

    else:
        interface.erro_codigo()
        sleep(1)
