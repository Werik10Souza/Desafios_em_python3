
#*Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOOL. O programa vai ler o NOME DO JOGADOR e 
#*QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será
#*guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.

nome = str(input('Nome do Jogador: '))
quantidades_partidas = int(input(f'Quantas partidas {nome} jogou?: '))

contador = 0
total = 0

lista_gols = []

while contador < quantidades_partidas:
    gols_partida = int(input(f'Quantos gols na partida{contador}?: '))
    lista_gols.append(gols_partida)
    contador = contador + 1
    total = total + gols_partida

analise = {'Nome' : nome,
           'Gols' : lista_gols,
           'Total' : total}

print('-='*30)
print(analise)
print('-='*30)

for k, v in analise.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {nome} jogou {contador} partidas')
for indice, valor in enumerate(lista_gols):
    print(f'    => Na partida {indice}, fez {valor} gols.')

print(f'Foi um total de {total} gols.')