
#*Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador e quantos GOLS ele marcou.

#*O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha informado corretamente.

def ficha(n = '', g = 0):
    print('-'*50)
    g = 0 #?ESCOPO GLOBAL 
    if nome == '':
        return(f'O jogador <desconhecido> marcou {gols} gol(s) no campeonato')
    elif gols == '':
        return(f'O jogador {n} marcou {g} gol(s) no campeonato')
    else:
        return(f'O jogador {n} marcou {gols} gol(s) no campeonato')


#?PROGRAMA PRINCIPAL
#!ESCOPO GLOBAL
nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input(f'Quantos gols o jogador {nome} marcou?: '))

print(ficha(nome))
