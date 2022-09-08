from logging import error
import interface
import treatment
from time import sleep


def auth(db_root, user='', password=''):
    if password == '':
        return False
    else:
        with open(db_root, 'r') as read:
            root = user
            pass_root = password
            for line in read:
                data = line.split(';')
                if root == data[0] and pass_root == data[1]:
                    return True
                else:
                    return False


def file_exists(db):
    try:
        file = open(db, 'r')
        file.close()
    except FileNotFoundError:
        print(f'[ERROR] - Arquivo {db} não existe!')
        return False
    else:
        return True


def create_file(db):
    try:
        create = open(db, 'w+')
        create.close()
    except error:
        print('[ERROR] - Houve um erro na criação do arquivo!')
    else:
        print(f'[SUCESS] - Arquivo {db} criado com sucesso!')


def write_Pfisica(db_Pfisica, name, cpf, age, income):
    try:
        wr = open(db_Pfisica, 'a+')
    except error:
        print('[ERROR] - Erro na abertura do arquivo')
    else:
        try:
            wr.write(f'{id(db_Pfisica)};{name};{cpf};{age};'
                     f'{interface.Real(income)}\n')
        except error:
            print('[ERROR] - Erro na escrita do arquivo')
        else:
            interface.title('[SUCESS] - CADASTRADO COM SUCESSO!')
            sleep(2)
            wr.close()


def write_Pjuridica(db_Pjuridica, name, cnpj, size, capital, flow, dre):
    try:
        wr = open(db_Pjuridica, 'a+')
    except error:
        print('[ERROR] - Erro na abertura do arquivo')
    else:
        try:
            wr.write(f'{id(db_Pjuridica)};{name};{cnpj};{size};')
            wr.write(f'{interface.Real(capital)};{interface.Real(flow)};'
                     f'{interface.Real(dre)}\n')
        except error:
            print('[ERROR] - Erro na escrita do arquivo')
        else:
            interface.title('[SUCESS] - CADASTRADO COM SUCESSO!')
            sleep(2)
            wr.close()


def query_Pfisica(db_Pfisica, query):
    cpf = treatment.read_cpf(query)
    with open(db_Pfisica, 'r') as read:
        for line in read:
            data = line.split(';')
            if cpf == data[2]:
                print('=' * 50)
                print('DADOS DO USUÁRIO'.center(50))
                print('=' * 50)
                print()
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'{"Idade: "}{data[3]} anos')
                print(f'{"Renda Líquida: "}{data[4]}')
                print('=' * 50)
                return True
    return False


def query_Pjuridica(db_Pjrudica, query):
    with open(db_Pjrudica, 'r') as read:
        cnpj = treatment.read_cnpj(query)
        for line in read:
            data = line.split(';')
            if cnpj == data[2]:
                print('=' * 50)
                print('DADOS DA EMPRESA'.center(50))
                print('=' * 50)
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da Empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'{"Porte: "}{data[3]}')
                print(f'{"Capital Imobilizado: "}{data[4]}')
                print(f'{"Fluxo de Caixa: "}{data[5]}')
                print(f'{"DRE: "}{data[6]}')
                print('=' * 50)
                return True
    return False


def query_Pfisica_register(db_Pfisica, query):
    with open(db_Pfisica, 'r') as read:
        cpf = treatment.read_cpf(query)
        for line in read:
            data = line.split(';')
            if cpf == data[2]:
                return True


def query_Pjuridica_register(db_Pjrudica, query):
    with open(db_Pjrudica, 'r') as read:
        cnpj = treatment.read_cnpj(query)
        for line in read:
            data = line.split(';')
            if cnpj == data[2]:
                return True


def delete_Pfisica(db_Pfisica, query):
    cpf = treatment.read_cpf(query)
    with open(db_Pfisica, 'r') as read:
        lines = read.readlines()
    with open(db_Pfisica, 'w', encoding='utf8') as wr:
        for x, line in enumerate(lines):
            if cpf in line:
                if x == 0:
                    wr.write('0;0;0;0;0\n')
                wr.write('')
            else:
                wr.write(line)


def delete_Pjuridica(db_Pjuridica, query):
    cnpj = treatment.read_cnpj(query)
    with open(db_Pjuridica, 'r') as read:
        lines = read.readlines()
    with open(db_Pjuridica, 'w', encoding='utf8') as wr:
        for x, line in enumerate(lines):
            if cnpj in line:
                if x == 0:
                    wr.write('0;0;0;0;0;0;0\n')
                wr.write('')
            else:
                wr.write(line)


def credit_Pfisica(db_Pfisica, query, credit, portion):
    cpf = query
    read = open(db_Pfisica, 'rt')
    for line in read:
        data = line.split(';')
        if cpf in data:
            # Script para remover tudo que identifique como string
            income = float(data[4].strip('\n').strip('R$ ').replace(',', '.'))
            # Análise de risco
            low_risk = (income * 30) / 100
            medium_risk = (income * 45) / 100
            high_risk = (income * 60) / 100
            # Juros de acordo com o risco
            low_interest = (credit * 20) / 100
            medium_interest = (credit * 30) / 100
            high_interest = (credit * 45) / 100
            # Valor real do emprestimo
            lend_1 = (credit + low_interest) / portion
            lend_2 = (credit + medium_interest) / portion
            lend_3 = (credit + high_interest) / portion
            if lend_1 <= low_risk:
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_1)}')
                print('Valor Total do contrato: '
                      f'{interface.Real(credit+low_interest)}')
            elif lend_2 <= medium_risk:
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_2)}')
                print('Valor Total do contrato: '
                      f'{interface.Real(credit+medium_interest)}')
            elif lend_3 <= high_risk:
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_3)}')
                print('Valor Total do contrato: ',
                      f'{interface.Real(credit+high_interest)}')
            else:
                interface.title('[FAILURE] - EMPRÉSTIMO REPROVADO')


def credit_Pjuridica(db_Pjuridica, query, credit, portion):
    cnpj = query
    read = open(db_Pjuridica, 'rt')
    for line in read:
        data = line.split(';')
        if cnpj in data:
            # Scripts para remover tudo que identifique como string
            immobilized = float(
                data[4].strip('\n').strip('R$ ').replace(',', '.'))
            flow = float(data[5].strip('\n').strip('R$ ').replace(',', '.'))
            dre = float(data[6].strip('\n').strip('R$ ').replace(',', '.'))
            # Análise de risco
            flow_average = flow / 3
            credit_50 = (credit * 50) / 100
            low_risk = (immobilized * 30) / 100
            medium_risk = (dre * 30) / 100
            high_risk = flow_average
            # Juros de acordo com o risco
            low_interest = (credit * 10) / 100
            medium_interest = (credit * 20) / 100
            high_interest = (credit * 35) / 100
            # risco baixo: 30% do imobilizado no valor do credito como garantia
            if low_risk >= credit:
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print('Valor da Parcela: '
                      f'{interface.Real((credit+low_interest)/portion)}')
                print('Valor Total do contrato: '
                      f'{interface.Real(credit+low_interest)}')
            # risco medio: 30% do DRE como garantia, equivalente a 50% do valor
            elif medium_risk >= credit_50:
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print('Valor da Parcela: '
                      f'{interface.Real((credit+medium_interest)/portion)}')
                print('Valor Total do contrato: '
                      f'{interface.Real(credit+medium_interest)}')
            # risco alto: A média do fluxo de caixa maior
            # ou igual que a parcela do empréstimo
            elif high_risk >= (credit / portion):
                interface.title('[SUCESS] - EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print('Valor da Parcela: '
                      f'{interface.Real((credit+high_interest)/portion)}')
                print('Valor Total do contrato: '
                      f'{interface.Real(credit+high_interest) }')
            else:
                interface.title('[FAILURE] - EMPRÉSTIMO REPROVADO')


def id(db_id, default='0'):
    id = list()
    with open(db_id, 'r') as read:
        lines = read.readlines()
        for line in lines:
            while True:
                if default in line.split(';'):
                    sum = int(default) + 1
                    default = str(sum)
                    id.append(default)
                    break
        return id[-1]
