
#* Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
#* qual foi o MAIOR e o MENOR valores lindos. O programa deve perguntar do usuário se ele quer ou não continuar a digitar valores.

contador = 0
media = 0
soma = 0
maior = 0
menor = 0
pergunta = 'sim'

while pergunta == 'sim':
    numero = int(input('\nDigite um número inteiro da sua escolhar: '))
    pergunta = str(input('\nDigite [sim/nao], para continuar: ')).strip().upper()
    while pergunta != 'sim' and pergunta != 'nao':
        pergunta = str(input('\nDigite [sim/nao], para continuar: ')).strip()
    soma = soma + numero
    contador = contador + 1
    media = soma / contador
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print('\nMEDIA: {:.2f}'.format(media))
print('MAIOR: {}'.format(maior))
print('MENOR: {}'.format(menor))
