# Cadastro + DB.txt

### Resumo versão 1.0:

Sistema simples **(prompt command)** que cadastra pessoas e a idade, escrito em Python tendo como base de dados arquivo com extenção txt. 

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário

**Telas do Programa:**

[Tela principal](https://user-images.githubusercontent.com/109303611/183476531-02f29dea-5e8a-4b7d-888d-41907baaaf25.JPG)

[Tela de Cadastro](https://user-images.githubusercontent.com/109303611/183476540-4c30a0f4-c7ed-406d-87ff-4c5937feefa3.JPG)

[Tela do banco de dados](https://user-images.githubusercontent.com/109303611/183476552-8922fefd-189e-4462-a068-807f6f96cf09.JPG)

---

### Resumo versão 1.1:

Modificar a __*versão 1.0*__ para sistema de análise de crédito de pessoa física e pessoa jurídica.

**Escopo para versão 1.1:**

- [x] Modificações
    - [x] Alterar o nome da opção 01 e 02
    - [x] Incluir nome do sistema acima do Menu Principal
    - [x] Alterar menu de pessoas cadastradas
    - [x] Alterar menu de cadastro
        
- [x] Cadastro de Pessoa Física
    - [x] Cadastro de CPF
    - [x] Melhora do cadastro de idade
    - [x] Cadastro de Renda Liquida

- [x] Cadastro de Pessoa Jurídica
    - [x] Cadastro Nome da Empresa
    - [x] Cadastro de CNPJ
    - [x] Cadastro de Porte da empresa
    - [x] Cadastro do Capital imobilizado
    - [x] Cadastro do Fluxo de caixa dos ultimos 3 meses
    - [x] Cadastro do D.R.E do último ano

- [x] Cadastro de Menu Proposta de crédito
    - [x] Análise Pessoa física
    - [x] Análise Pessoa Jurídica

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário
* Lista

**Telas do Programa:**

[Tela Principal](https://user-images.githubusercontent.com/109303611/183444915-c5446a8f-d05c-4f4d-a1f5-97349923137d.JPG)

[Tela Banco de Dados Pessoa fisica](https://user-images.githubusercontent.com/109303611/183444934-cd663dc5-8add-4897-be1e-d7ff03238900.JPG)

[Tela Banco de Dados Pessoa jurídica](https://user-images.githubusercontent.com/109303611/183444968-366dcbc2-9afc-48e4-85e2-00f5044ba12e.JPG)

[Tela análise de proposta](https://user-images.githubusercontent.com/109303611/183444983-6f3ca69f-c53c-4428-9814-5616e0cf0cb9.JPG)

___

### Resumo versão 1.2:

Modificar a __*versão 1.1*__ e melhorar o sistema de análise de crédito.

**Escopo para versão 1.2:**

- [x] Modificações:
    - [x] Alterar a moeda de saída para Real Brasileiro ignorando a pontuação padrão do python.
    - [x] Cadastrar o ID de usuários ao banco de dados pela com números aleatórios com a biblioteca random() para manipulação futura.
    - [x] Alterar o nome do menu Cadastrar para Cadastrar Usuário.
    - [x] Alterar o nome do menu Banco de Dados para Consultar Usuário.
    - [x] Criar um menu para remover usuários cadastrados.
    - [x] Otimizar funções.
    - [x] Alterar as ordens do Menu Principal.
        - [x] 1 para Proposta de Crédito.
        - [x] 2 para Cadastrar Usuário.
        - [x] 3 para Remover Usuário.
        - [x] 4 para Sair do Sistema.
    - [x] Alterar a sistemática de consultar usuários no menu. Inserindo dentro do menu Proposta de Crédito e Remover Usuário.

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário
* Lista

**Telas do Programa:**

[Tela Principal](https://user-images.githubusercontent.com/109303611/183923377-df639a48-7412-4868-ad3a-cb071c113737.JPG)

[Tela Proposta de Crédito](https://user-images.githubusercontent.com/109303611/183923474-acabc12a-b057-4951-9d29-c95e50639949.JPG)

[Tela Consulta de usuario dentro de Proposta de Crédito](https://user-images.githubusercontent.com/109303611/183923625-bc3c4db1-568d-4aa5-ad1d-52ca91cf2f26.JPG)

[Tela de Remover Usuário](https://user-images.githubusercontent.com/109303611/183923752-3098e190-ffbb-43cf-9b05-5c82d5ef4dd7.JPG)

[Tela Consulta de usuario dentro de Remover Usuario](https://user-images.githubusercontent.com/109303611/183923845-93024dab-c60a-4044-9266-8213af62fe01.JPG)

___

### Resumo versão 1.3:

Modificar a __*versão 1.2*__ e criar funções QUERY de dados dos bancos.txt.

**Escopo para versão 1.3:**

- [x] Modificações:
    - [x] Criar função para questionar os dados dos bancos.
    - [x] Modificar menu Proposta de Crédito.
        - [x] Criar sistemática de consulta por CPF.
        - [x] Caso CPF inexistente: iniciar cadastro de usuário.
        - [ ] Caso CPF existente: iniciar análise de proposta.
            - [ ] Criar regras de proposta de crédito.
        - [x] Criar sistemática de consulta por CNPJ.
        - [x] Caso CNPJ inexistente: iniciar cadastro de empresa.
        - [ ] Caso CNPJ existente: iniciar análise de proposta.
            - [ ] Criar regras de proposta de crédito.
    - [ ] Modificar menu Cadastrar Usuário.
        - [ ] Criar sistemática de consulta por CPF.
        - [ ] Caso CPF inexistente: iniciar cadastro de usuário. 
        - [ ] Caso CPF existente: informar que já existe.
    - [ ] Modificar menu Remover Usuário.
        - [ ] Criar sistemática de consulta por CPF.
        - [ ] Caso CPF inexistente: informar que usuário não existe. 
        - [ ] Caso CPF existente: informar mensagem de confirmação.
            - [ ] Caso resposta sim: remover usuario do banco de dados.



