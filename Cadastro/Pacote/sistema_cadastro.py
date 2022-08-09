# Sistema de Cadastro com banco de dados em texto
from time import sleep
import interface
import dados

arquivo_Pfisica = 'banco_dados_Pfisica.txt'
arquivo_Pjuridica = 'banco_dados_Pjuridica.txt'
# Se não existir o arquivo.txt, cria-se
if not dados.arquivo_existe(arquivo_Pfisica):
    dados.criar_arquivo(arquivo_Pfisica)        # Cria um arquivo.txt
# Se não existir o arquivo.txt, cria-se
if not dados.arquivo_existe(arquivo_Pjuridica):
    dados.criar_arquivo(arquivo_Pjuridica)        # Cria um arquivo.txt
while True:
    interface.titulo('SISTEMA DE ANÁLISE DE CRÉDITO')
    interface.titulo('[#] MENU PRINCIPAL')
    interface.subtitulo()       # Chama as opções do programa
    usuario = interface.LeiaInt('Digite o código correspondente: ')
    if usuario == 1:
        interface.titulo('[$] ANÁLISE DE PROPOSTA DE CRÉDITO!')
        interface.submenu()
        usuario = interface.LeiaInt('Digite o código correspondente: ')
        sleep(1)
        break        
    elif usuario == 2:
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
    elif usuario == 3:
        break
    elif usuario == 4:
        interface.submenu()
        while True:
            usuario = interface.LeiaInt('Digite o código correspondente: ')
            if usuario == 1:
                dados.ler_db_Pfisica(arquivo_Pfisica)
                break
            elif usuario == 2:
                dados.ler_db_Pjuridica(arquivo_Pjuridica)
                break
            else:
                interface.erro_codigo()
    elif usuario == 5:
        interface.titulo('[!] PROGRAMA ENCERRADO COM SUCESSO!')
        sleep(1)
        break
    else:
        interface.erro_codigo()
        sleep(2)
