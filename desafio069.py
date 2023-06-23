
#*Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
#*se o usuário QUER ou NÃO continuar. No final, mostre:

#?A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
#?B) QUANTOS HOMENS FORAM CADASTRADOS.
#?C) QUANTOS MULHERES TEM MENOS DE 20 ANOS.

idade = 0
sexo = ''
continuar = 'N'
pessoas = 0
homens = 0
mulheres_menos_vinte = 0

while True:
    idade = int(input('Quantos anos, você possuir atualmente?: '))
    sexo = str(input('Qual é o seu sexo[M/F]?: ').upper().strip())
    print('\n=============================================')
    if(idade > 18):
        pessoas = pessoas + 1
    if(sexo == 'M'):
        homens = homens + 1
    if(idade < 20):
        mulheres_menos_vinte = mulheres_menos_vinte + 1
    continuar = str(input('\nQuer continuar á cadastrar?[S/N]: ').upper().strip()[0])
    if(continuar == 'N'):
        break
print('\n========================================')
print('\nPessoas com MAIS de 18 anos: {}'.format(pessoas))
print('\nHomens cadastrados: {}'.format(homens))
print('\nMulheres com menos de 20 anos: {}'.format(mulheres_menos_vinte))
print('========================================')
print('\nFIM DO PROGRAMAR!!!')
