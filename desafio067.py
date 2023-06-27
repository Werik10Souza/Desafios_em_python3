
#*Faça um programa que mostra a tabuaba, de vários números, um de cada vez, para cada valor digitado pelo usuário. O
#*programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um valor: '))
    if numero <= 0:
        break
    for contador in range(1, 11):
        print('{} X {} = {}'.format(numero, contador, numero*contador))
print('\n')
print('-'*40)
print('FIM DO PROGRAMA!')
print('-'*40)