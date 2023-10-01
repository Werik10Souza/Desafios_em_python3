def aumentar(v=0, d=0.0, sit=False):
    if sit:
        c = v / d
        r = v  + c
    return r

def diminuir(v=0, d=0.0, sit=False):
    if sit:
        c = v / d
        r = v + c
    return r

def metade(v=0,sit=False):
    if sit:
        r = v / 2
    return r

def dobro(v=0, sit=False):
    if sit:
        r = v * 2
    return r

def moeda(v=0, sit=False):
    if sit:
        r = (f'R${v}')
    return r
