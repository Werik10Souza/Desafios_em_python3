
#*Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou.

#*O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha informado corretamente.

def ficha(n = '', g=0):
    #!ESCOPO LOCAL
    g = 0
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    elif gols == '':
        return f'O jogador {n} fez {g} gol(s) no campeonato'
    else:
        return f'O jogador {n} fez {gols} gol(s) no campeonato'

#programa principal:
#!ESCOPO GLOBAL
nome = str(input('Nome do jogador: '))
gols = str(input('Números de gols: '))

#print(ficha(nome, gols))
#print(ficha(nome))
#print(ficha(gols))
#print(ficha())

