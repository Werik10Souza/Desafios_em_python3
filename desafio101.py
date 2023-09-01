
#*Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma pessoa retornanda um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIA nas eleições.

def voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade <= 17:
        return(f'Com {idade} anos: VOTO NEGADO')
    else:
        if idade >= 18 and idade <= 64:
            return(f'Com {idade} anos: VOTO OBRIGATÓRIO')
        else:
            return(f'Com {idade} anos: VOTO OPCIONAL')

ano_nasc = int(input('Em qual ano você nasceu?: '))
print(voto(ano_nasc))
