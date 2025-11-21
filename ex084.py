galera = list()
dado = list()
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
           maior = dado[1]
        if dado[1] < menor:
           menor = dado[1]
    resp = str(input('Quer continuar? [S/N] '))
    galera.append(dado[:])
    dado.clear()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'foram cadastradas um total de {len(galera)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de', end='')
for p in galera:
    if p[1] == maior:
       print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}kg. Peso de', end='')
for p in galera:
    if p[1] == menor:
       print(f' [{p[0]}]', end='')
print()
print('-=' * 30)
print(f'Os dados totais foram {galera}')