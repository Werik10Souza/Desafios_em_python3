
#*Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA que mantenha separados os valores PARES e IMPARES. No final, mostre os valores PARES e IMPARES em ordem CRESCENTE.

valores = []
par = []
impar = []

for valor in range(0,7):
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
    if numero not in par:
        if numero % 2 == 0:
            par.append(numero)
    if numero not in impar:
        if numero % 2 != 0:
            impar.append(numero)
    valores.append(par[:])
    valores.append(impar[:])

print('\n','='*20)
print('PAR: ',sorted(par))
print('IMPAR: ',sorted(impar))
