
#*Faça um programa que mostra a tabuaba, de vários números, um de cada vez, para cada valor digitado pelo usuário. O
#*programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um valor: '))
    if numero <= -1:
        break
    print('\n{} X {} = {}'.format(numero, 1, numero*1))
    print('{} X {} = {}'.format(numero, 2, numero*2))
    print('{} X {} = {}'.format(numero, 3, numero*3))
    print('{} X {} = {}'.format(numero, 4, numero*4))
    print('{} X {} = {}'.format(numero, 5, numero*5))
    print('{} X {} = {}'.format(numero, 6, numero*6))
    print('{} X {} = {}'.format(numero, 7, numero*7))
    print('{} X {} = {}'.format(numero, 8, numero*8))
    print('{} X {} = {}'.format(numero, 9, numero*9))
    print('{} X {} = {}'.format(numero, 10, numero*10))
print('\n')
print('-'*40)
print('FIM DO PROGRAMA!')
print('-'*40)