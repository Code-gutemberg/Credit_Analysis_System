def LeiaInt(entrada):
    """Descrição:
    Função para verificar se a entrada é do tipo inteiro.
    Parâmetro:
        entrada (str): recebe uma string.
    Retorno:
        inteiro: retorna um número inteiro.
    """
    while True:
        try:
            inteiro = int(input(entrada))
            # Transforma a string recebida em inteiro
        except (ValueError, TypeError):
            print('\033[0;31mERRO, Digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mOcorreu alguma interrupção\033[m')
            break
        else:
            return inteiro


def titulo(msg):
    print('=' * 50)
    print(msg.center(50))
    print('=' * 50)


def subtitulo():
    menu = dict()
    menu[1] = 'Proposta de Crédito [ $ ]'
    menu[2] = 'Cadastrar Usuário \t[ + ]'
    menu[3] = 'Remover Usuário \t[DEL]'
    menu[4] = 'Consultar Usuário \t[ = ]'
    menu[5] = 'Sair do Sistema \t[ ! ]'
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def usuarios_db():
    print('=' * 50)
    titulo('[=] BANCO DE DADOS'.center(50))


def submenu():
    print('=' * 50)
    print('[1] - Pessoa Física\n'
          '[2] - Pessoa Jurídica')
    print('=' * 50)


def erro_codigo():
    print('\033[0;31mERRO, Digite um número válido.\033[m')


def Real(preço, moeda='R$'):     # Formata para Real BR.
    """-> Descrição

    Parâmetros:
        preço (int/float): Preço recebido
        moeda (str, optional): Opcional com formato em Real Brasileiro R$'.
    Retorno:
        str: retorna o valor formatado em Real Brasileiro R$'.
    """
    return f'{moeda} {preço:.2f}'.replace(".", ",")
