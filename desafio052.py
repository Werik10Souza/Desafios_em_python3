total = 0
numero = int(input('Digite um número: '))
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(contador), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('É por isso ele é PRIMO!!')
else:
    print('E por isso ele NÃO É PRIMO!!')
