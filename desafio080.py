
#*Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma lista. JÁ , mostre a  POSIÇÃO CORRETA de inserção(sem usar o sort()).
#*No final, mostre a LISTA ORDENADA na tela.

valores = []

for contador in range(0,5):
    numero = int(input('Digite o valor: '))
    if contador == 0: #O número zero(0), significa o ÍNDICE/POSIÇÃO
        valores.append(numero)
    elif numero > valores[-1]:
        valores.append(numero)
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                break
print('\nOs valores digitados em ordem foram {}'.format(valores))
