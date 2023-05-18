quantidade = 0
soma = 0

while True:
    numeros = int(input('Digite os valores da sua escolhar: '))
    if numeros == 999:
        break
    quantidade = quantidade + 1
    soma = soma + numeros

print('='*40)
print('Quantidade de vezes digitadas: {}'.format(quantidade))
print('A somar dos valores digitados: {}'.format(soma))
print('='*40)
