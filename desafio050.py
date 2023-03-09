soma = 0
par = 0
impa = 0
for numero in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    par += numero
    if numero % 2 == 1:
        impa += numero
soma = par - impa
print('\nA soma dos números PARES: {}'.format(soma))
print('\nFIM!')
