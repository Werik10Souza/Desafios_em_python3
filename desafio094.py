
#*Crie um programa que leia NOME, SEXO e IDADE de VÁRIOS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO
#*e todos os dicionários em uma LISTA. No final, mostre:
#?A) Quantas pessoas foram cadastradas.
#?B) A média de idade do grupo.
#?C) Uma lista com todas as mulheres.
#?D) Uma lista com todas as pessoas com idade acima da média.

contador = 0
soma_idades = 0

lista = []

while True:
    nome = str(input('\nNome: '))
    sexo = str(input('Sexo [M/F]: ').upper().strip() [0])
    idade = int(input('Idade: '))
    contador = contador + 1
    soma_idades = soma_idades + idade

    dados = {'Nome' : nome,
             'Sexo' : sexo,
             'Idade' : idade}
    
    lista.append(dados.copy())

    resposta = str(input('\nQuer continuar [S/N]: ').upper().strip() [0])

    if resposta == 'N':
        break

media = soma_idades / contador

print('-='*40)
print(f'O grupo tem {contador} pessoas.')
print(f'A média de idade é de {media} anos.')
print(lista)
