'''FUNÇÕES PARA TESTAR, CRIAR, ABRIR E ALIMENTAR DOIS BANCOS DE DADOS EM TXT'''

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


def ler_arquivo_Pfisica(entrada):
    contador = 0
    controle_id = dict()
    controle_id['id'] = contador

    try:
        ler = open(entrada, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        interface.pessoas_db()
        print('DADOS PESSOAS FÍSICAS'.center(50))
        print()
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{"id: "}{contador}')
            print(f'{"Nome: "}{dado[0]}')
            print(f'{"CPF: "}{dado[1]}')
            print(f'{"Idade: "}{dado[2]} anos')
            print(f'{"Renda Líquida: "}{dado[3]}')
            contador += 1
            controle_id['dados'] = dado
            print('=' * 50)
        sleep(2)
        print()


def ler_arquivo_Pjuridica(entrada):
    contador = 0
    controle_id = dict()
    controle_id['id'] = contador
    try:
        ler = open(entrada, 'rt')    # r = read e t = texto
    except (Error):
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        interface.pessoas_db()
        
        print('DADOS PESSOAS JURÍDICAS'.center(50))
        print()
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{"id: "}{contador}')
            print(f'{"Nome da Empresa: "}{dado[0]}')
            print(f'{"CNPJ: "}{dado[1]}')
            print(f'{"Porte: "}{dado[2]}')
            print(f'{"Capital Imobilizado: "}{dado[3]}')
            print(f'{"Fluxo de Caixa: "}{dado[4]}')
            print(f'{"DRE: "}{dado[5]}')
            contador += 1
            controle_id['dados'] = dado
            print('=' * 50)
        sleep(2)
        print()


def escrever_arquivo_Pfisico(entrada, nome='', cpf='', idade=0, renda=0):

    try:
        escrever = open(entrada, 'at+')  # a = append, t = texto, + = adicionar
    except (Error):
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            escrever.write(
                f'{nome};{cpf};{idade};{interface.Real(renda)}\n')
        except (Error):
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.titulo(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            escrever.close()


def escrever_arquivo_Pjuridico(entrada, nome='', cnpj='', porte='', capital=0, fluxo=0, dre=0):
    try:
        escrever = open(entrada, 'at+')  # a = append, t = texto, + = adicionar
    except (Error):
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            escrever.write(f'{nome};{cnpj};{porte};')
            escrever.write(f'{interface.Real(capital)};{interface.Real(fluxo)};{interface.Real(dre)}\n')
        except (Error):
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.titulo(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            escrever.close()


def leiaDinheiro(msg):
    while True:
        valido = False
        while not valido:
            entrada = str(input(msg)).replace(',', '.').strip()
            if entrada.isalpha() or entrada == '':
                print(f'ERRO, [{entrada}] é um preço inválido!')
            else:
                try:
                    valido = True
                    return float(entrada)
                except ValueError:
                    print('ERRO, não inserir pontuação no inicio do valor.'
                        ' Insira na penúltima casa decimal.')
                    continue