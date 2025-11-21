velocidade = int(input('Qual a velocidade do seu carro? '))

limite = 80
multa = (velocidade - limite) * 7

if velocidade > limite:
    print('Você passou do limite de velocidade e foi multado em R${}!'.format(multa))
else:
    print('Você esta dentro do limite de velocidade!')
