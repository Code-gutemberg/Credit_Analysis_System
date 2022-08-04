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
    menu[1] = 'Ver Pessoas Cadastradas'
    menu[2] = 'Cadastrar nova pessoa'
    menu[3] = 'Sair do Sistema'
    print('=' * 50)
    for k, v in menu.items():
        print(f'{k} - {v}')
    print('=' * 50)


def pessoas_cadastradas():
    print('=' * 50)
    titulo('[=] PESSOAS CADASTRADAS'.center(50))
