
#*Crie um programa que simule o funcionamento de CAIXA ELETRÔNICO. No inicio, perguente ao usuário, qual será o VALOR
#*A SER SACADO(número inteiro) e o programa vai informar quantas CÉLULAS de cada valor serão entregues.
#? OBS: Considere que o caixa possui células de R$50, R$20, R$10 e R$1

print("="*45)
print("{:^45}".format('CAIXA ELETRÔNICO'))
print("="*45)
valor = int(input("Digite o valor quer queira sacar: "))
cedula = 50
total_cedula = 0
while True:
    if valor >= cedula:
        valor = valor - cedula
        total_cedula = total_cedula + 1
    else:
        if total_cedula > 0:
            print('\nA quantidade {} cédula(s) de R${}'.format(total_cedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if valor == 0:
            break
print('\nFIM!!!')