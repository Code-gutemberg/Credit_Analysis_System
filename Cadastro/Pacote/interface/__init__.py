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
    menu[1] = 'Banco de Dados [=]'
    menu[2] = 'Cadastrar [+]'
    menu[3] = 'Proposta de Crédito [$]'
    menu[4] = 'Sair do Sistema [!]'
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def pessoas_db():
    print('=' * 50)
    titulo('[=] BANCO DE DADOS'.center(50))


def submenu():
    print('=' * 50)
    print('[1] - Pessoa Física\n'
          '[2] - Pessoa Jurídica')
    print('=' * 50)


def erro_codigo():
    print('\033[0;31mERRO, Digite um número válido.\033[m')
