
#*Reescreva a função leiaInt() que fizemos no  desafio104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie tmbém uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(mensagem):
    situacao =  False
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


#*Programa principal:
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
