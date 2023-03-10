enesimo_termo = 0
primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a RAZÃO da P.A: '))
for primeiro_termo in range(enesimo_termo+1, 9):
    enesimo_termo = primeiro_termo + (10 - 1) * razao
    print(enesimo_termo)
