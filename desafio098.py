
#*Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(), que receba três PARÂMETROS: INICIO, FIM e PASSO e realizar a contagem.

#*Seu programa tem que realizar TRÊS CONTAGENS através da função criada:

#?a) De 1 até 10, de 1 em 1
#?b) De 10 até 0, de 2 em 2
#?c) Uma contagem PERSONALIZADA.

def contador():
    print('-='*30)
    print('Contagem de 1 até 10, de 1 em 1')
    for x in range(1,11,1):
        print(x, end=' ')
    print('FIM!')
    print('-='*30)
    print('Contagem de 10 até 0, de 2 em 2')
    for y in range(10,-2,-2):
        print(y, end=' ')
    print(' FIM!')
    print('-='*30)
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for t in range(inicio, fim, passo):
        print(t, end=' ')
    print(' FIM!')

contador()
