distancia = float(input('Qual foi a distância percorrida?: '))
if distancia > 200:
    valor_maior = distancia * 0.45
    print('Distãncia percorrida {}, valor da passagem R${:.2f}'.format(distancia, valor_maior))
else:
    valor_menor = distancia * 0.50
    print('Distância percorrida {}, valor da passagem R${:.2f}'.format(distancia, valor_menor))
