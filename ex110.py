
def aumentar(v=0, a=0):
    d = a/100
    c = v / d
    r = v + c
    return r

def diminuir(v=0,t=0):
    d = t/100
    c = v / d
    r = v - c
    return r

def dobro(v=0):
    r = v * 2
    return r

def metade(v=0):
    r = v / 2
    return r

def resumo(v=0, a=0, t=0):
    print('-'*40)
    print(' RESUMO DOS VALORES')
    print('-'*40)
    print(f'A metade de {v} é igual {metade(v)}')
    print(f'O dobro de {v} é igual {dobro(v)}')
    print(f'{a}% de aumento do valor {aumentar(v)}')
    print(f'{t}% reduzindo do valor {diminuir(v)}')
    print('-'*40)