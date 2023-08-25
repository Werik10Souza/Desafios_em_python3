
#*Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(), que receba três PARÂMETROS: INICIO, FIM e PASSO e realizar a contagem.

#*Seu programa tem que realizar TRÊS CONTAGENS através da função criada:

#?a) De 1 até 10, de 1 em 1
#?b) De 10 até 0, de 2 em 2
#?c) Uma contagem PERSONALIZADA.

from time import sleep

def contador(i, f, p):
    if p < 0:
        p = p + (-1)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont = cont + p
        print('FIM!')

#?PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
