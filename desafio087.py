
#*Aprimore o DESAFIO ANTERIOR(086), mostrando no final:

#?A)A SOMA de todos os VALORES PARES digitados.

#?B)A SOMA dos valores da TERCEIRA COLUNA.

#?C)O MAIOR valor da SEGUNDA LINHA.

matriz = []
numeros = []

par = 0
soma = 0

maior = 0

for valor in range(0,9):
    valor = int(input('Digite um valor inteiro: '))

    if valor not in numeros:
        numeros.append(valor)
        matriz.append(numeros[:])
        numeros.clear()
    if valor % 2 == 0:
        par = par + valor

print('\n',sorted(matriz), '\n')

print('M A T R I Z')
print('='*20)
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('='*20)
print('\n', 'SOMA dos valores PARES: {}'.format(par))

coluna_tres = matriz[2] + matriz[5] + matriz[8]

soma = coluna_tres[0] + coluna_tres[1]  + coluna_tres[2]

print('\nSOMA dos valores da coluna três: {}'.format(soma))

linha_dois =  matriz[3] + matriz[4] + matriz[5]

for valor in linha_dois:
    if valor > maior:
        maior = valor
print('\nO maior valor entre a linha dois: {}'.format(maior))
