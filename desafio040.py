nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))

media01 = (nota_01 + nota_02) / 2
media02 = (nota_01 + nota_02) / 2


if media01 <= 4.9:
    print('\nMédia = {}'.format(media01))
    print('\nREPROVADO')
elif media01 > 5.0 and media02 < 6.9:
    print('\nMédia = {}'.format(media01))
    print('\nRECUPERAÇÃO')
elif media01 >= 7.0:
    print('\nMédia = {}'.format(media01))
    print('\nAPROVADO')
