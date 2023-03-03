primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('MAIOR: {}'.format(maior))

menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('MENOR: {}'.format(menor))
