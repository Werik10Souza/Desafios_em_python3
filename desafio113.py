def leiaInt(mensagem): #Função leiaInt: Essa função permite ao usuário digitar um número inteiro. Ela recebe um argumento chamado mensagem, que é uma string que você deseja exibir ao solicitar a entrada do usuário.
    while True:  #Laço while True: Iniciamos um loop infinito com while True, o que significa que ele continuará pedindo a entrada até que o usuário forneça um valor válido.
        try: #tenta 
            valor = int(input(mensagem)) #tenta converter a entrada do usuário em um número inteiro usando.
            return valor #Se o usuário fornecer um valor válido que pode ser convertido em um número inteiro, o código sairá do loop e retornará o valor.
        except ValueError: #Se o usuário fornecer um valor que não pode ser convertido em um número inteiro.
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m') #informar ao usuário que a entrada foi inválida.

def leiaFloat(mensagem): #permite ao usuário digitar um número de ponto flutuante (número real).
    while True:  #Laço while True: Iniciamos um loop infinito com while True, o que significa que ele continuará pedindo a entrada até que o usuário forneça um valor válido.
        try: #tenta 
            valor = float(input(mensagem)) #tenta converter a entrada do usuário em um número flutuante usando.
            return valor #Se o usuário fornecer um valor válido que pode ser convertido em um número flutuante, o código sairá do loop e retornará o valor.
        except ValueError: #Se o usuário fornecer um valor que não pode ser convertido em um número flutuante.
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')  #informar ao usuário que a entrada foi inválida.

#*Programa principal:
inteiro = leiaInt('Digite um múmero inteiro: ')
print(f'\033[0;32mVocê digitou o número inteiro {inteiro}\033[m')

real = leiaFloat('Digite um número flutuante: ')
print(f'\033[0;32mVocê digitou o número flutuante {real}\033[m')
