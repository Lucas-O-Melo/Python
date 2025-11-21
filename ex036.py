casa = float(input('Qual é o valor da Casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
pagamento = int(input('Em quantos anos você vai pagar? '))

prestacao = casa / (pagamento * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, pagamento), end='')
print(' a prestação será de R${:.2f} por mês'.format(prestacao))

if prestacao <= minimo:
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado!')