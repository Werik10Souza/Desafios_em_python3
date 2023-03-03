print('-'*20)
print('CONVERSÃO DE BASES:')
print('[1] - BINÁRIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL')
print('-'*20)

numero = int(input('\nDigite um número que deseja: '))
base = int(input('Informe a base de conversão desejada: '))

if base == 1:
    print('\nO número {}, foi convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('\nO número {}, foi convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('\nO número {}, foi convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\nO número informado é invalido')
