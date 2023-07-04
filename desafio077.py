
#*Crie um programa que tenha uma tupla com 'várias palavras' (não usar acentos).
#*Depois disso, você deve mostrar, para cada palavra, quais são as suas 'vogais'.

palavras = ('CARRO', 'MOTO', 'SOLTEIRO', 'VOA',
            'CHUVA', 'ROÇA', 'MAR', 'LUTAR')

for p in palavras:
    print('\nA palavras {} termos '.format(p), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')