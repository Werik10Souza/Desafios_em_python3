salario_funcionario = float(input('Quanto você ganhar  por mês?: '))
if salario_funcionario > 1250:
    aumento_salario_superior = (salario_funcionario * 0.1) + salario_funcionario
    print('O novo salário do funcionario: {:.2f}'.format(aumento_salario_superior))
else:
    if salario_funcionario <= 1250:
        aumento_salario_inferiores = (salario_funcionario * 0.15) + salario_funcionario
        print('O novo salário do funcionario: {:.2f}'.format(aumento_salario_inferiores))
