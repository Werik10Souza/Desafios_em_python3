
#*Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles e o MAIOR.

from time import sleep

def maior(* numeros):
    contador = 0
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador = contador + 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#?PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
