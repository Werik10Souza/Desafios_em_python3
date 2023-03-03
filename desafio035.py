lado_a = int(input('Digite o valor da reta: '))
lado_b = int(input('Digite o valor da reta: '))
lado_c = int(input('Digite o valor da reta: '))

if lado_a + lado_b > lado_c:
    print('\nAs três retas PODE forma um TRIÂNGULO')
else:
    if lado_a + lado_b <= lado_c:
        print('\nAs três retas NÃO pode forma um TRIÃNGULO')

print('\nFIM')
