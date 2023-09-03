
#*Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou.

#*O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha informado corretomente.

def ficha(n=0,g=0):

    print('-'*40)

    if n == None:
        n = str('<DESCONHECIDO>')
    if g == None:
        g = int(0)
    return(f'O jogador {n}, marcou {g} gols')

#?PROGRAMA PRINCIPAL
nome = str(input('Digite o nome do jogador: ').strip())
gols = int(input(f'Quantos gols o jogador {nome} marcou?: '))

print(ficha(n = nome, g = gols))
