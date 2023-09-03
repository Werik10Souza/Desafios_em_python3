
#*Crie um programa tenha uma FUNÇÃO FATORIAL() que receba dois parâmetro: o primeiro que indique o número a calcular e o outro chamado SHOW, que será um valor LÓGICO(OPCIONAL) indicando se será mostrado ou não na tela processo de cálculo do fatorial.

def fatorial(num, show=0):
    
    contador = num
    f = 1
    while contador > 0:
        print(f'{contador}', end=' ')
        if contador > 1:
            print(' X ', end=' ')
        else:
            print(' = ', end=' ')
        f = f * contador
        contador = contador - 1
    return(f'{f}')

#?PROGRAMA PRINCIPAL:
print(fatorial(num = 5))
