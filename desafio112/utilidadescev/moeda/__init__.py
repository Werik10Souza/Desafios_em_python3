def aumentar(v=0, p=0, formatar=False):
    resultado = v + (v * (p / 100))
    return moeda(resultado) if formatar else resultado

def diminuir(v=0, p=0, formatar=False):
    resultado = v - (v * (p / 100))
    return moeda(resultado) if formatar else resultado

def metade(v=0, formatar=False):
    resultado = v / 2
    return moeda(resultado) if formatar else resultado

def dobro(v=0, formatar=False):
    resultado = v * 2
    return moeda(resultado) if formatar else resultado

def moeda(v=0):
    return f'R${v:.2f}'

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*40)
    print(' RESUMO DOS VALORES'.center(30))
    print('-'*40)
    print(f'A metade de {preco} é igual \033[0;32m\t{metade(preco, True)}\033[m')
    print(f'O dobro de {preco} é igual \033[0;32m\t{dobro(preco, True)}\033[m')
    print(f'{taxaa}% de aumento do valor \033[0;32m\t{aumentar(preco, taxaa, True)}\033[m')
    print(f'{taxar}% reduzindo do valor \033[0;32m\t\t{diminuir(preco, taxar, True)}\033[m')
    print('-'*40)
