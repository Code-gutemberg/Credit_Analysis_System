# Sistema de Cadastro com banco de dados em texto
from time import sleep
import interface
import dados

arquivo_Pfisica = 'banco_dados_Pfisica.txt' # Define o nome do banco de dados Pessoa Fisica
arquivo_Pjuridica = 'banco_dados_Pjuridica.txt' # Define o nome do banco de dados Pessoa Juridica

if not dados.arquivo_existe(arquivo_Pfisica):   # Se não existir o db_Pfisica.txt, cria-se
    dados.criar_arquivo(arquivo_Pfisica)
if not dados.arquivo_existe(arquivo_Pjuridica): # Se não existir o db_Pjuridica.txt, cria-se
    dados.criar_arquivo(arquivo_Pjuridica)

while True:
    interface.titulo('SISTEMA DE ANÁLISE DE CRÉDITO')   # MENU Principal
    interface.titulo('[#] MENU PRINCIPAL')              # MENU Principal
    interface.subtitulo()                               # MENU Principal
    usuario = interface.LeiaInt('Digite o código correspondente: ')
    
    if usuario == 1:        # MENU Análise de Proposta de Crédito
        interface.titulo('[$] ANÁLISE DE PROPOSTA DE CRÉDITO')
        interface.submenu()
        while True:
            usuario = interface.LeiaInt('Digite o código correspondente: ')
            if usuario == 1:        # SUBMENU Pessoa Física
                cpf = 'Digite o CPF: '
                resposta_Pfisica = False
                if dados.query_Pfisica(arquivo_Pfisica, cpf, resposta_Pfisica) == False:
                    print('CPF não existe')
                    while True:
                        usuario = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                        if usuario in 'S':
                            interface.titulo('[+] NOVO CADASTRO')
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
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'N':
                        interface.titulo('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                        sleep(1)
                        break
                else:
                    break # colocar as opções de análise de crédito
                
            elif usuario == 2:      # SUBMENU Pessoa Jurídica
                cnpj = 'Digite o CNPJ: '
                resposta_Pjuridica = False
                if dados.query_Pjuridica(arquivo_Pjuridica, cnpj, resposta_Pjuridica) == False:
                    print('CNPJ não existe')
                    while True:
                        usuario = str(input('Deseja Cadastrar um Novo usuário [S/N]: ')).upper()[0]
                        if usuario in 'S':
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
                            dados.escrever_Pjuridica(arquivo_Pjuridica, nome, cnpj, porte,
                                                            capital, soma_fluxo, dre)  # type: ignore
                        elif usuario in 'N':
                            break
                        else:
                            print('\033[31mERRO, digite SIM ou NÃO \033[m')
                    if usuario in 'N':
                        interface.titulo('[!] PROGRAMA ENCERRADO COM SUCESSO!')
                        sleep(1)
                        break
                else:
                    break
            else:
                interface.erro_codigo()
        sleep(1)
        break
    
    elif usuario == 2:      # Menu Cadastro de Usuário
        interface.titulo('[+] NOVO CADASTRO')
        interface.submenu()
        usuario = interface.LeiaInt('Digite o código correspondente: ')
        if usuario == 1:
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
        elif usuario == 2:
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
            dados.escrever_Pjuridica(arquivo_Pjuridica, nome, cnpj, porte,
                                            capital, soma_fluxo, dre)  # type: ignore
    
    elif usuario == 3:      # MENU Remover Usuário
        interface.titulo('[DEL] REMOVER USUÁRIO')
        interface.submenu()
        while True:
            usuario = interface.LeiaInt('Digite o código correspondente: ')
            if usuario == 1:    # SUBMENU pessoa física
                dados.ler_db_Pfisica(arquivo_Pfisica)
                break
            elif usuario == 2:  # SUBMENU pessoa jurídica
                dados.ler_db_Pjuridica(arquivo_Pjuridica)
                break
            else:
                interface.erro_codigo()
        sleep(1)
        break
    
    elif usuario == 4:      # Menu Sair do Programa
        interface.titulo('[!] PROGRAMA ENCERRADO COM SUCESSO!')
        sleep(1)
        break
    
    else:
        interface.erro_codigo()
        sleep(2)
