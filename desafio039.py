ano_nascimento = int(input('Digite o seu ano de nascimento: '))

idade = 2023 - ano_nascimento
tempo01 = 18 - idade
tempo02 = idade - 18

if idade <= 17:
    print('\nAinda vai se alistar ao serviço militar')
    print('\nFALTA: {} ano(s)'.format(tempo01))
elif idade == 18:
    print('\nHora de se alistar')
elif idade > 19:
    print('\nPassou do tempo do alistamento')
    print('\nPassou do prazo á {} ano(s)'.format(tempo02))

