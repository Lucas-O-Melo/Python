n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

print('O maior número é {}, e o menor número é {}!'.format(maior, menor))