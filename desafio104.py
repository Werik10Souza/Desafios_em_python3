
#*Crie um programa que tenha a FUNÇÃO leiaInt(), que vai funcionar de forma semelhente á função input() da python, só que fazendo VALIDAÇÃO para aceitar apenas um valor número.

#?EX:
#? n = leiaInt('Digite um n: ')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033mERRO!Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor

#*PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
