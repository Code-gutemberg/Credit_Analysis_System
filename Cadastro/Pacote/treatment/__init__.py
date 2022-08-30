def read_int(entry):
    while True:
        try:
            read_int = int(input(entry))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, Digite um número válido.\033[m')
            break
        except (KeyboardInterrupt):
            print('\033[0;31mOcorreu alguma interrupção\033[m')
            break
        else:
            return read_int
        
    
def read_coin(value):
    while True:
        valid = False
        while not valid:
            cipher = str(input(value)).replace(',', '.').strip()
            if cipher.isalpha() or cipher == '':
                print(f'ERRO, [{cipher}] é um preço inválido!')
            else:
                try:
                    valid = True
                    return float(cipher)
                except ValueError:
                    print('ERRO, não inserir pontuação no inicio do valor.'
                          ' Insira na penúltima casa decimal.')
                    continue
                
                
def read_cpf(entry):
    while True:
        cpf = input(entry)
        if '.' not in cpf:
            print(f'\033[31m ERRO, insira pontuações \033[m')
        elif '-' not in cpf:
            print(f'\033[31m ERRO, insira o hífen \033[m')
        elif len(cpf) < 14 and '.-' not in cpf:
            print(f'\033[31m ERRO, mínimo caracteres [14] \033[m')
        elif len(cpf) > 14:
            print(f'\033[31m ERRO, máximo caracteres [14] \033[m')
        else:
            return cpf
        

def read_cnpj(entry):
    while True:
        cnpj = input(entry)
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
            return cnpj