def read_int(entry):
    while True:
        try:
            read_int = int(input(entry))
        except (ValueError, TypeError):
            print('[ERROR] - Digite um número válido.')
            break
        except (KeyboardInterrupt):
            print('[ERROR] - Ocorreu alguma interrupção')
            break
        else:
            return read_int
        
    
def read_coin(value):
    while True:
        valid = False
        while not valid:
            cipher = str(input(value)).replace(',', '.').strip()
            if cipher.isalpha() or cipher == '':
                print(f'[ERROR]] - [{cipher}] é um preço inválido!')
            else:
                try:
                    valid = True
                    return float(cipher)
                except ValueError:
                    print('[ERROR]] - Não inserir pontuação no inicio do valor')
                    print('[ERROR]] - Insira na penúltima casa decimal.')
                    continue
                
                
def read_cpf(entry):
    while True:
        cpf = input(entry)
        if '.' not in cpf:
            print(f'[ERROR] - Insira pontuações.')
        elif '-' not in cpf:
            print(f'[ERROR] - Insira o hífen.')
        elif len(cpf) < 14 and '.-' not in cpf:
            print(f'[ERROR] - Mínimo 14 caracteres.')
        elif len(cpf) > 14:
            print(f'[ERROR] - Máximo 14 caracteres.')
        else:
            return cpf
        

def read_cnpj(entry):
    while True:
        cnpj = input(entry)
        if '.' not in cnpj:
            print(f'[ERROR] - Insira pontuações.')
        elif '/' not in cnpj:
            print(f'[ERROR] - Insira a barra.')
        elif '-' not in cnpj:
            print(f'[ERROR] - Insira o hífen.')
        elif len(cnpj) < 18 and '.-' not in cnpj:
            print(f'[ERROR] - Mínimo 18 caracteres.')
        elif len(cnpj) > 18:
            print(f'[ERROR] - Máximo 18 caracteres.')
        else:
            return cnpj
        
        
def read_name(entry):
    while True:
        name = input(entry)
        if len(name) > 40:
            print(f'[ERROR] - ERRO, máximo caracteres [40]')
            continue
        elif len(name) < 3:
            print(f'[ERROR] - Mínimo de 3 caracteres')
            continue
        else:
            return name
            