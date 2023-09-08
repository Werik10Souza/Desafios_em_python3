
#*Crie um programa que tenha a FUNÇÃO leiaInt(), que vai funcionar de forma semelhente á função input() da python, só que fazendo VALIDAÇÃO para aceitar apenas um valor número.

#?EX:
#? n = leiaInt('Digite um n: ')

def leiaInt(mensagem):
    situacao = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            situacao = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if situacao:
            break
    return valor
            
#*PROGRAMA PRINCIPAL
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
