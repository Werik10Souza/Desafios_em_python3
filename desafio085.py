
#*Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA que mantenha separados os valores PARES e IMPARES. No final, mostre os valores PARES e IMPARES em ordem CRESCENTE.

valores = [[], []]

for valor in range(0,7):
    numero = int(input('Digite o valor: '))
    if numero not in valores:
        if numero % 2 == 0:
            valores[0].append(numero)
        elif numero % 2 != 0:
            valores[1].append(numero)

print('\n',valores)

print('\n','='*20)
print('PAR: ',sorted(valores[0]))
print('IMPAR: ',sorted(valores[1]))
