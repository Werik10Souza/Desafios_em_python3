
#*Crie um programa que LEIA NOME,ANO DE NASCIMENTO e CANTEIRA DE TRABALHO e cadastre-os (com IDADE) com um dicionário
#*se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO. Calcule e acrescente,
#*além da IDADE, com quantos anos a pessoa vai se aposentar?

from datetime import datetime

nome = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.now()
ano = ano_atual.year

carteira_trabalho = int(input('Carteira de Trabalho(0 não tenho): '))

idade = ano - ano_de_nascimento

if carteira_trabalho != 0:
    ano_contratacao = int(input('Ano de contratação: '))
    salario = int(input('Salário:R$'))
    carreira = {'Nome': nome, 
                'Idade' :  idade,
                'CPTS' : carteira_trabalho,
                'Contratação' : ano_contratacao,
                'Salário' : salario,
                'Aposentadoria' : 35 - (ano_de_nascimento - ano_contratacao)}

    print('='*110)
    print(carreira)
