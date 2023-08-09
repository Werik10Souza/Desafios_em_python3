
#*Crie um programa que leia NOME, SEXO e IDADE de VÁRIOS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO
#*e todos os dicionários em uma LISTA. No final, mostre:
#?A) Quantas pessoas foram cadastradas.
#?B) A média de idade do grupo.
#?C) Uma lista com todas as mulheres.
#?D) Uma lista com todas as pessoas com idade acima da média.

galera = []
pessoa = {}

soma = 0
media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper() [0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
    print()
print('D) Uma lista com idade acima da media.')
for p in galera:
    if p['idade'] >= media:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
print()
