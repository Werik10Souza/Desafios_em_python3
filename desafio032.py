from datetime import date
ano = int(input('Digite qualquer ANO da sua preferencia, se você quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano digitado {} é BISSEXTO!!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))