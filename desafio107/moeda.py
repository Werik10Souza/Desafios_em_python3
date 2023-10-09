
def aumentar(preco=0, taxa=0.0):
    res = preco + (preco * taxa/100)
    return (f'{res:.2f}')

def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return (f'{res:.2f}')

def dobro(preco=0):
    res = preco * 2
    return res

def metade(preco=0):
    res = preco / 2
    return res