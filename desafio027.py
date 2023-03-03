nome_completo = str(input('Digite o seu nome completo: ')).strip()

nome = nome_completo.split()

print('Primeiro: {}'.format(nome[0]))
print('Último: {}'.format(nome[len(nome) - 1]))
