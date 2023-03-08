from time import sleep
for numero in range(1, 500):
    if numero % 2 == 1:
        print(numero)
        sleep(1)
        multiplo = numero / 3
print('FIM')
soma = multiplo + multiplo
print('\nA soma dos múltiplos de três é igual {:.0f}'.format(soma))
