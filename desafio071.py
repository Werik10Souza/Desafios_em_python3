
#*Crie um programa que simule o funcionamento de CAIXA ELETRÔNICO. No inicio, perguente ao usuário, qual será o VALOR
#*A SER SACADO(número inteiro) e o programa vai informar quantas CÉLULAS de cada valor serão entregues.
#? OBS: Considere que o caixa possui células de R$50, R$20, R$10 e R$1

valor_sacado = 0

while True:
    print('='*50)
    print('CAIXA ELETRÔNICO')
    print('='*50)
    print('Digite o valor desejado AQUI EMBAIXO!!!!!')
    valor_sacado = int(input('\nDIGITE: '))
    cinquenta = valor_sacado/30
    vinte = cinquenta / 10
    dez = vinte/ 9
    um = dez / 1
    break
print('\n')
print('='*50)
print('QUANTIDADE DE R$50: {:.0f}'.format(cinquenta))
print('QUANTIDADE DE R$20: {:.0f}'.format(vinte))
print('QUANTIDADE DE R$10: {:.0f}'.format(dez))
print('QUANTIDADE DE R$1: {:.0f}'.format(um))
print('='*50)
