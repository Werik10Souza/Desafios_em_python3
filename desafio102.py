
#*Crie um programa tenha uma FUNÇÃO FATORIAL() que receba dois parâmetro: o primeiro que indique o número a calcular e o outro chamado SHOW, que será um valor LÓGICO(OPCIONAL) indicando se será mostrado ou não na tela processo de cálculo do fatorial.

def fatorial(num, show=0):#SHOW OPCIONAL

    """
    fatorial(num, show = False)
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculodo.
    :param show: (Opcional) mostrar ou não a contra.
    :return: O valor do fatorial de número num.
    """

    print('-'*40)

    contador = num #O contador vai receber o número que for inserido no parâmentro
    f = 1

    while contador > 0:
        if show: #Essa linha determinar se vai aparecer ou não o cálculo
            print(f'{contador}', end=' ')
            if contador > 1:#Quanto o contador for MAIOR que um, execute
                print(' X ', end=' ')
            else:
                 print(' = ', end=' ')
        f = f * contador # f -> FATORIAL vezes(X) o contador
        contador = contador - 1 #Vai conta do MAIOR para o MENOR número
    return(f'{f}') #Valor da multiplicação feita na linha 27


#?PROGRAMA PRINCIPAL:
#print(fatorial(5))
#print(fatorial(5, show=True))
#help(fatorial)
