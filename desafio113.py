def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')

def leiaFloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')

#*Programa principal:
inteiro = leiaInt('Digite um múmero inteiro: ')
print(f'\033[0;32mVocê digitou o número inteiro {inteiro}\033[m')

real = leiaFloat('Digite um número flutuante: ')
print(f'\033[0;32mVocê digitou o número flutuante {real}\033[m')
