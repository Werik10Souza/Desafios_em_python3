
#*Desenvolva um programa que leia 'quatro valores' pelo teclado e guarde-os em uma tupla. No final, mostre:

#? A) Quantas vezes apareceu o valor 9?.

#? B) Em que posição foi digitado o primeiro valor 3?.

#? C) Quais foram os números 'pares'.

numero01 = int(input('Digite qualquer número inteiro da sua preferência: '))
numero02 = int(input('Digite qualquer número inteiro da sua preferência: '))
numero03 = int(input('Digite qualquer número inteiro da sua preferência: '))
numero04 = int(input('Digite qualquer número inteiro da sua preferência: '))

tupla = (numero01, numero02, numero03, numero04)

print('\n', tupla)

print('\n','='*60)
print('\nQuantas vezes vezes apareceu o valor 9?: {} VEZ(ES)'.format(tupla.count(9)))
if 3 in tupla:
    print('Em qual posição foi digitado o primeiro valor 3? {}ª posição'.format(tupla.index(3)))
else:
    print('O valor 3 NÃO foi digitado em nenhuma posição')
print('Quais foram os números PAR(ES)?', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
print('\n', '='*60)