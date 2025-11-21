viagem = int(input('Qual será a distância da sua viagem? '))

v1 = viagem * 0.50
v2 = viagem * 0.45

if viagem <= 200:
    print('Sua viagem custará R${}'.format(v1))
else:
    print('Sua viagem custará R${}'.format(v2))
