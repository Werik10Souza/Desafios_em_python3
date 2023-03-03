nome_completo = str(input('Digite o seu nome completo: ')).strip()

nome_completo.lower()
print('O nome completo com todas as letras minúsculas: {}'.format(nome_completo.lower()))

nome_completo.upper()
print('O nome completo com todas as letras maiúsculas: {}'.format(nome_completo.upper()))

len(nome_completo)
print('Ao total tem: {}'.format(len(nome_completo) - nome_completo.count(' ')))

var = nome_completo.find(' ')
print('O primeiro nome tem: {}'.format(var))
