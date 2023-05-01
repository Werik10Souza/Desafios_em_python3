
#* Faça um programa que leia um número qualquer e mostre o seu fatorial.
#* EX:
#*  5! = 5 X 4 X 3 X 2 X 1 = 120

numero = int(input('Digite um número da sua preferencia: '))
contador = 1
fatorial = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1 
print('\nFATORIAL = {}'.format(fatorial))