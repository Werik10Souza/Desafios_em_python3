
#*Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista.

#*Depois disso, mostre:

#?A) QUANTOS números foram digitados.

#?B) A lista de valores, ordenada de forma DECRESCENTE.

#?C) Se valor 5 foi digitado e está ou não na lista.

numeros = []
resposta = 'N'
contador = 0

while True:
    numero = int(input('\nDigite um valor: '))
    contador = contador + 1
    if numero not in numeros:
        numeros.append(numero)
    resposta = str(input('\nQuer continuar[S/N]?: ').upper().strip() [0])
    if 5 in numeros:
        print('\nO número 5 está na posição {}'.format(numeros.index(5)))
    elif 5 not in numeros:
        print('\nNÃO FOI DIGITADO AINDA NA LISTA, O VALOR CINCO!')
    if resposta in 'qwertyuiopadfghjklçzxcvbmQWERTYUIOPADFGHJKLÇZXCVBM':
        print('\nDigite os valores correspodente[S/N]!\n')
        resposta = str(input('\nQuer continuar[S/N]?: ').upper().strip() [0])
    if resposta == 'N':
        break

numeros.sort(reverse=True)
print(numeros)
print('\nFoi {} a quantidade de números digitadas pelo usuario.'.format(contador))