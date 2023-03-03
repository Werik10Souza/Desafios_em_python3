reta01 = int(input('Digite o valor da reta: '))
reta02 = int(input('Digite o valor da reta: '))
reta03 = int(input('Digite o valor da reta: '))

if reta01 < reta02 + reta03 and reta02 < reta01 + reta03 and reta03 < reta01 + reta02:
    print('As retas de cima PODEM FORMAR um triângulo ', end='')
    if reta01 == reta02 and reta02 == reta03:
        print('Equilátero!')
    elif reta01 != reta02 and reta02 != reta03 and reta03 != reta01:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo')
