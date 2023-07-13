
#*Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista.

#*Depois disso, crie DUAS LISTAR EXTRAS que vão contar apenas os valores PARES e os VALORES ÍMPARES digitados.
#*respectivamente.

#*Ao final, mostre o conteúdo das TRÊS LISTAS geradas.

lista = []
resposta = 'N'
par = []
impar = []

while True:
    numero = int(input('\nDigite um valor: '))
    if numero not in lista:
        lista.append(numero)
    if numero % 2 == 0:
        if numero not in par:
            par.append(numero)
    if numero % 2 != 0:
        if numero not in impar:
            impar.append(numero)
    resposta = str(input('\nQuer continuar[S/N]?: ').upper().strip() [0])
    if resposta == 'N':
        break
print('\n', lista)
print('\nPAR: {}'.format(par))
print('\nÍMPAR: {}'.format(impar))
