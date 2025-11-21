salario = float(input('Qual é o salário do funcionário? '))

aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)

if salario <= 1250:
    print('O salário deste funcionário com o aumento é de {:.2f}'.format(aumento2))
else:
    print('O salário deste funcionário com o aumento é de {:.2f}'.format(aumento1))
