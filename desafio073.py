
#*Crie uma tupla preenchida com os 20 primeiros colocados da tabela do 'Campeonato Brasileiro de Futebol', na colocação. Depois mostre:

#?A) Apenas os 5 primeiros colocados.
#?B) Os últimos 4 colocados da tabela.
#?C) Uma lista com os times em ordem alfabética.
#?D) Em que posição na tabela está o time da Flamengo.


tabela = ('', 'Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminese', 'Internacional', 'Bragantino', 'Fortaleza', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba')

print('='*25)
print('{}'.format('Classificação Série A'))
print('='*25)

print('\nOs cinco primeiros colocados de 2023:\n')
print(tabela[1:6])

print('\nOs últimos quarto colocados de 2023:\n')
print(tabela[-4:])

print('\nOrdem Alfabéica:\n')
print(sorted(tabela))

print('Posição do Flamengo na tabela do campeonato brasileiro de 2023:\n')
print(tabela.index('Flamengo'))
