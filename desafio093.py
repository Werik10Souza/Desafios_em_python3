
#*Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOOL. O programa vai ler o NOME DO JOGADOR e 
#*QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será
#*guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.

nome = str(input('Nome do Jogador: '))
quantidades_partidas = int(input(f'Quantas partidas {nome} jogou?: '))

contador = 0

lista_gols = []

while contador < quantidades_partidas:
    gols_partida = int(input('Quantos gols na partida?: '))
    lista_gols.append(gols_partida)
    contador = contador + 1

print('\n',lista_gols)

#analise = {'Nome' : nome,
           #'Gols' : lista_gols,
           #'Toal' : total}
