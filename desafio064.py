
#* Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
#* condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag).

numero = 0
contador = 0
soma = 0

numero = int(input('Digite seu número de preferencia: '))
while numero != 999:
    soma = soma + numero
    contador = contador + 1
    numero = int(input('Digite seu número de preferencia: '))
print('A quantidade dos valores digitados é igual {}'.format(contador))
print('A soma dos valores é igual {}'.format(soma))
