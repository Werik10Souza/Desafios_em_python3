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

