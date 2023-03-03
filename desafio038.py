numero_a = int(input('Digite o primeiro número: '))
numero_b = int(input('Digite o segundo número: '))

if numero_a > numero_b:
    print('\nO primeiro valor {} é maior'.format(numero_a))
elif numero_a < numero_b:
    print('\nO segundo valor {} é maior'.format(numero_b))
elif numero_a == numero_b:
    print('\nOs números {} e {} são iguais'.format(numero_a, numero_b))
