maior = 0
menor = 0

for cinco in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(cinco)))
    if cinco == 1: 
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nO maior peso lido foi de \033[32m{}Kg'.format(maior))
print('O menor peso lido foi de \033[33m{}Kg'.format(menor))