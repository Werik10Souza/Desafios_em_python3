
#* Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
#* qual foi o MAIOR e o MENOR valores lindos. O programa deve perguntar do usuário se ele quer ou não continuar a digitar valores.

pergunta = 'SIM'
soma = 0
quantidade = 0
maior = 0
menor = 0
while pergunta in 'SIMsim': 
    numero = int(input('Digite um valor: '))
    pergunta = str(input('Quer continuar [SIM/NAO]: ')).upper()
    quantidade = quantidade + 1
    soma = soma + numero
    if quantidade == 1:
        maior = menor
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / quantidade

print('\nSOMA: {}'.format(soma))
print('Quantidade: {}'.format(quantidade))
print('MAIOR: {}'.format(maior))
print('MENOR: {}'.format(menor))
print('MÉDIA: {}'.format(media))
