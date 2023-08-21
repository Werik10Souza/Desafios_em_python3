
#*Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(), que receba um texto qualquer com PARÂMETRO e mostre uma mensagem com tamanho adaptável.
    #?EX:
        #*escreva('Olá, mundo!')
    #?SAÍDA:
     #*~~~~~~~~~~
     #*Olá, mundo!
     #*~~~~~~~~~~

print('-'*20)
print('ESCREVA AQUI EMBAIXO')
print('-'*20)

def escreva(texto):
    texto = str(input(' '))
    print('~'*len(texto))
    print(texto)
    print('~'*len(texto))

escreva('texto')
