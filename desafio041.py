ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print('-=-'*35)
print('Você se encaixar na categoria de acordo com seu ano de nascimento, veja abaixo a sua cotegoria')
print('-=-'*35)

idade01 = 2023 - ano_nascimento
idade02 = 2023 - ano_nascimento


if idade01 <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade01 >= 10 and idade02 <= 14:
    print('CATEGORIA: INFANTIL')
elif idade01 >= 15 and idade02 <= 19:
    print('CATEGORIA: JUNIOR')
elif idade01 > 19 and idade02 <= 20:
    print('CATEGORIA:: SÊNIOR')
elif idade01 >= 21:
    print('CATEGORIA: MASTER')
