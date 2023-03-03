peso = float(input('Qual é o seu peso atual?: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('\nAbaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('\nPeso Ideal')
elif IMC >= 25 and IMC < 30:
    print('\nSobrepeso')
elif IMC >= 30 and IMC < 40:
    print('\nObesidade')
elif IMC >= 40:
    print('\nObesidade Mórbida')
    