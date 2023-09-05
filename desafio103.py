
#*Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou.

#*O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha informado corretomente.

def ficha(n = 0, g = 0):
    print('-'*40)
    
    if ficha(n,g):
        return(f'O jogador {n} marcou {g} gols')
    elif ficha(n):
        return(f'O jogador {n} marcou {g} gols')
    elif ficha(g):
        if n == 0:
            n = str(' <DESCONHECIDO> ')
        return(f'O jogador {n} marcou {g} gols')
    elif ficha():
        if n == 0:
            n = str(' <DESCONHECIDO> ')
        return(f'O jogador {n} marcou {g} gols')

#?PROGRMA PRINCIPAL
nome = str(input('Digite o nome do jogador: '))
gols = int(input(f'Quantos gols o jogador {nome} marcou?: '))

ficha(nome, gols)
#ficha(nome)
#ficha(gols)
#ficha()
