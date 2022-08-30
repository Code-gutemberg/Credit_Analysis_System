from random import randint
import interface, treatment
from time import sleep

def auth(db_root, user='', password=''):
    if password == '':
        return False
    else:
        root = user
        pass_root = password
        read = open(db_root, 'rt')
        for line in read:
            data = line.split(';')
            if root in data[0] and pass_root in data[1]:
                return True
            else:
                return False


def file_exists(db):
    try:
        file = open(db, 'rt')
        file.close()
    except FileNotFoundError:
        print(f'\033[0;31mArquivo {db} não existe!\033[m')
        return False
    else:
        return True


def create_file(db):
    try:
        create = open(db, 'wt+')
        create.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[0;31mAquivo {db} criado com sucesso!\033[m')


def write_Pfisica(db_Pfisica, name='', cpf='', age=0, income=0):
    id = 0
    try:
        write = open(db_Pfisica, 'at+')
    except:
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            id = randint(0, 100)
            write.write(f'{id};{name};{cpf};{age};{interface.Real(income)}\n')
        except:
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.title(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            write.close()


def write_Pjuridica(db_Pjuridica, name='', cnpj='', size='', capital=0, flow=0, dre=0):
    id = 0
    try:
        write = open(db_Pjuridica, 'at+')
    except:
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            id = randint(0, 100)
            write.write(f'{id};{name};{cnpj};{size};')
            write.write(
                f'{interface.Real(capital)};{interface.Real(flow)};{interface.Real(dre)}\n')
        except:
            print('\033[0;31mErro na escrita do arquivo\033[m')
        else:
            interface.title(f'\033[0;32mCADASTRADO COM SUCESSO!\033[m')
            sleep(2)
            write.close()


def query_Pfisica(db_Pfisica, query):
    try:
        read = open(db_Pfisica, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        cpf = treatment.read_cpf(query)
        for line in read:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            if cpf in data:
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
    try:
        read = open(db_Pjrudica, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        cnpj = treatment.read_cnpj(query)
        for line in read:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            if cnpj in data:
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
    try:
        read = open(db_Pfisica, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        cpf = treatment.read_cpf(query)
        for line in read:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            if cpf in data:
                return True
        return False


def query_Pjuridica_register(db_Pjrudica, query):
    try:
        read = open(db_Pjrudica, 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        cnpj = treatment.read_cnpj(query)
        for line in read:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            if cnpj == data[2]:
                return True
        return False


def delete_Pfisica(db_Pfisica, query):
    cpf = treatment.read_cpf(query)
    with open(db_Pfisica, 'r') as read:
        lines = read.readlines()
    
    with open(db_Pfisica, 'w', encoding='utf8') as write:
        for line in lines:
            if cpf in line:
                write.write('')
            else:
                write.write(line)


def delete_Pjuridica(db_Pjuridica, query):
    cnpj = treatment.read_cnpj(query)
    with open(db_Pjuridica, 'r') as read:
        lines = read.readlines()
    
    with open(db_Pjuridica, 'w', encoding='utf8') as write:
        for line in lines:
            if cnpj in line:
                write.write('')
            else:
                write.write(line)


def credit_Pfisica(db_Pfisica, query='', credit=0.0, portion=0):
    cpf = query
    read = open(db_Pfisica, 'rt')
    for line in read:
        data = line.split(';')
        data[1] = data[1].replace('\n', '')
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
            high_interest= (credit * 45) / 100
            # Valor real do emprestimo
            lend_1 = (credit + low_interest) / portion
            lend_2 = (credit + medium_interest) / portion
            lend_3 = (credit + high_interest) / portion
            if lend_1  <= low_risk:
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_1)}')
                print(f'Valor Total do contrato: {interface.Real(credit+low_interest)}')
            elif lend_2 <= medium_risk:
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_2)}')
                print(f'Valor Total do contrato: {interface.Real(credit+medium_interest)}')
            elif lend_3 <= high_risk:
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome: "}{data[1]}')
                print(f'{"CPF: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real(lend_3)}')
                print(f'Valor Total do contrato: {interface.Real(credit+high_interest)}')
            else:
                interface.title('EMPRÉSTIMO REPROVADO')


def credit_Pjuridica(db_Pjuridica, query='', credit=0.0, portion=0):
    cnpj = query
    read = open(db_Pjuridica, 'rt')
    for line in read:
        data = line.split(';')
        data[1] = data[1].replace('\n', '')
        if cnpj in data:
            # Scripts para remover tudo que identifique como string
            immobilized = float(data[4].strip('\n').strip('R$ ').replace(',', '.'))
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
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real((credit+low_interest)/portion) }')
                print(f'Valor Total do contrato: {interface.Real(credit+low_interest)}')
            # risco medio: 30% do DRE como garantia, equivalente a 50% do valor do credito
            elif medium_risk >= credit_50:
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real((credit+medium_interest)/portion)}')
                print(f'Valor Total do contrato: {interface.Real(credit+medium_interest)}')
            # risco alto: A média do fluxo de caixa maior ou igual que a parcela do empréstimo
            elif high_risk >= (credit / portion):
                interface.title('EMPRÉSTIMO APROVADO')
                print(f'{"ID: "}{data[0]}')
                print(f'{"Nome da empresa: "}{data[1]}')
                print(f'{"CNPJ: "}{data[2]}')
                print(f'Valor do Crédito: {interface.Real(credit)}')
                print(f'Duração do Contrato: {portion} meses')
                print(f'Valor da Parcela: {interface.Real((credit+high_interest)/portion)}')
                print(f'Valor Total do contrato: {interface.Real(credit+high_interest) }')
            else:
                interface.title('EMPRÉSTIMO REPROVADO')
