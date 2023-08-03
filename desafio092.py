
#*Crie um programa que LEIA NOME,ANO DE NASCIMENTO e CANTEIRA DE TRABALHO e cadastre-os (com IDADE) com um dicionário
#*se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO. Calcule e acrescente,
#*além da IDADE, com quantos anos a pessoa vai se aposentar?

nome = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de Nascimento: '))

carreira = {'Nome': nome, 'Idade' : 2023 - ano_de_nascimento}

print(carreira)
