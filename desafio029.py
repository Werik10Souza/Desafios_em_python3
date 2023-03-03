velocidade = float(input('Digite a velocidade do carro: '))
if velocidade >= 80.01:
    multa = (velocidade - 80) * 7
    print('Você foi MULTADO! Velocidade do carro {} KM/H, com base na velocidade a multa é igual á {:.2f} Reais'.format(velocidade, multa))

else:
    print('FIM')
