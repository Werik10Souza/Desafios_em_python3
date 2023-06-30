
#*Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
#*Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

contagem_extensao = ('Zero', 'Um', 'Dois', 'Três', 'Quarto', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Desezoito', 'Dezenove', 'Vinte')

teclado  = int(input('\nDigite um numero entre 0 e 20: '))

print('\n')
print(contagem_extensao[teclado])
