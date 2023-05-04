
#* Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#* O programa encera quando ele disser que quer mostrar 0 termos.

from time import sleep
an = 0
primeiro_termo = 0
razao = 0
contador = 0
encerramento = 0

primeiro_termo = int(input('Insira o valor do primeiro termo da PA: '))
razao = int(input('Insira o valor da razão da PA: '))

an = primeiro_termo + (10 - 1) * razao

while contador <= 10:
    an = primeiro_termo + (10 - 1) * razao
    contador = contador + 1
    print(an + contador)
    sleep(2)
print('='*50)

print('\nQUER CONTINUAR[1] ou ENCERRAR[0]? Digite LOGO ABAIXO')
encerramento = int(input('DESEJA: ', '\n'))

if encerramento == 1: #*CONTINUAR
    an = primeiro_termo + (10 - 1) * razao
    while contador <= 20:
        an = primeiro_termo + (10 - 1) * razao
        contador = contador + 1
        print(an + contador)
        sleep(2)
elif encerramento == 0: #*ENCERRA
    print('\nFIM DA OPERAÇÃO!')
else:
    print('\nVALOR INVÁLIDOR!')
