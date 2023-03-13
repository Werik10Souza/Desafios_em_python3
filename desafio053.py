frase = str(input('Digite uma FRASE qualquer: '))
if str(frase) == ''.join(reversed(frase)):
    print('\nPALÍNDROMO')
else:
    print('\nNÃO é um PALÍNDROMO')
