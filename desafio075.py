
#*Desenvolva um programa que leia 'quatro valores' pelo teclado e guarde-os em uma tupla. No final, mostre:

#? A) Quantas vezes apareceu o valor 9?.

#? B) Em que posição foi digitado o primeiro valor 3?.

#? C) Quais foram os números 'pares'.

lista = ()

for lista01 in range(1):
    valor = int(input('Digite um valor inteiro qualquer: '))
    lista01 = valor
    for lista02 in range(1):
        valor = int(input('Digite um valor inteiro qualquer: '))
        lista02 = valor
    for lista03 in range(1):
        valor = int(input('Digite um valor inteiro qualquer: '))
        lista03 = valor
        for lista04 in range(1):
            valor = int(input('Digite um valor inteiro qualquer: '))
            lista04 = valor
    lista = lista01, lista02, lista03, lista04
print('\n', lista, '\n')

print('='*20)
print('parece o valor nove:')
print('\n', lista.count(9), 'vezes')
print('='*20)
print('\n', '='*40)
print('O valor três foi digitado na posição:')
print(lista.index(3))
print('='*40)
