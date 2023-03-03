frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparace {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu na posição {} na primeira vez'.format(frase.find('A') + 1))
print('A letra A apraceu na posição {} pela última vez'.format(frase.rfind('A') + 1))
