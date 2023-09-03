
#*Crie um programa tenha uma FUNÇÃO FATORIAL() que receba dois parâmetro: o primeiro que indique o número a calcular e o outro chamado SHOW, que será um valor LÓGICO(OPCIONAL) indicando se será mostrado ou não na tela processo de cálculo do fatorial.

def fatorial(num, show=False):

    """
    fatorial(num, show = False)
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculodo.
    :param show: (Opcional) mostrar ou não a contra.
    :return: O valor do fatorial de número num.
    """

    print('-'*40)

    contador = num
    f = 1

    while contador > 0:
        if show:
            print(f'{contador}', end=' ')
            if contador > 1:
                print(' X ', end=' ')
            else:
                 print(' = ', end=' ')

        f = f * contador
        contador = contador - 1
    return(f'{f}')


#?PROGRAMA PRINCIPAL:
#print(fatorial(5))
#print(fatorial(5, show=True))
#help(fatorial)
