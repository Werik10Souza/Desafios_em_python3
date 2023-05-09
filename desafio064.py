
#* Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
#* condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag).

numero = soma = 0
contador = -1
while numero != 999:
    contador = contador + 1
    soma = soma + numero
    numero = int(input('Digite um número [999 para parar]: '))
print('A soma é de {} e a quantidade é de {}'.format(soma, contador))
