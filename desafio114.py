

#*Crie um código em python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site pudim com sucesso!\033[0;32m')
