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


def aumentar(v=0, d=0.0):
    c = v / d
    r = v  + c
    return r

def diminuir(v=0, d=0.0):
    c = v / d
    r = v + c
    return r

def metade(v=0):
    r = v / 2
    return r

def dobro(v=0):
    r = v * 2
    return r

def moeda(v=0, moeda='R$'):
    r = (f'R${v}'.replace('.', ','))
    return r
