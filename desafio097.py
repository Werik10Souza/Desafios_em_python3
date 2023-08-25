
#*Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(), que receba um texto qualquer com PARÂMETRO e mostre uma mensagem com tamanho adaptável.
    #?EX:
        #*escreva('Olá, mundo!')
    #?SAÍDA:
     #*~~~~~~~~~~
     #*Olá, mundo!
     #*~~~~~~~~~~

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

#?PROGRAMA PRINCIPAL
print('-'*25)
print('ESCREVA LOGO ABAIXO ↓↓↓')
print('-'*25)

escreva(str(input(' ')))
