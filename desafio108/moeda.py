
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
 