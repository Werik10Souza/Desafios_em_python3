
#* Faça um  programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter
#* um valor correto.

masculino = 'M'
feminino = 'F'
sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite qual é o seu SEXO [M/F]: ').strip().upper())
    if sexo != 'M' and sexo != 'F':
        print('\nINCORRETO! O valor {}, não correspondente a M ou F...'.format(sexo))
        
masculino = 'M'
feminino = 'F'
if sexo == 'M':
    print('\nA letra " {} " informada, corresponde ao sexo MASCULINO'.format(sexo))
else:
    print('\nA letra " {} " informada, corresponde ao sexo FEMININO'.format(sexo))