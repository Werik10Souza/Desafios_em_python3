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

def moeda(preco=0):
    res = f'R${preco:.2f}'
    return res

def resumo(v=0, a=0, t=0):
    print('-'*40)
    print(' RESUMO DOS VALORES')
    print('-'*40)
    print(f'A metade de {v} é igual {moeda(metade(v))}')
    print(f'O dobro de {v} é igual {moeda(dobro(v))}')
    print(f'{a}% de aumento do valor {moeda(aumentar(v))}')
    print(f'{t}% reduzindo do valor {moeda(diminuir(v))}')
    print('-'*40)
