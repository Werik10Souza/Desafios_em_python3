
#* Crie um programa que leia dois valores e mostre um MENU na tela:
#* [1]-SOMAR   [2]-Multiplicar      [3]-Maior    [4]-Novos números    [5]-Sair do programa
#* Seu programa deverá realizar a operação solicitada em cada caso.

numero_A = float(input('Digite um número qualquer: '))
numero_B = float(input('Digite outro número qualquer: '))
escolha = 0
soma = 0
multiplicar = 0
while escolha != 5:
    print('''
    [1]-SOMAR
    [2]-MULTIPLICAR
    [3]-MAIOR
    [4]-NOVOS NÚMEROS
    [5]-SAIR DO PROGRAMA
    ''')
    escolha = int(input('Insira o número desejado: '))
    if escolha == 1:
        soma = numero_A + numero_B
        print('A soma dos valores {} e {} é igual -> {} '.format(numero_A, numero_B, soma))
    elif escolha == 2:
        multiplicar = numero_A * numero_B
        print('A multiplicação dos valores {} e {} é igual -> {:.2f}'.format(numero_A, numero_B, multiplicar))
    elif escolha == 3:
        if numero_A > numero_B:
            print('O MAIOR número é {}'.format(numero_A))
        else:
            print('O MAIOR número é {}'.format(numero_B))
    elif escolha == 4:
        numero_A = float(input('Digite o novo número: '))
        numero_B = float(input('Digite um novo número: '))
print('ENCERRADO OPERAÇÕES...FIM!!!')
