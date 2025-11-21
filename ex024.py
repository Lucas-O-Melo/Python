'''cid = str(input('Digite o nome de uma Cidade: '))
if 'Santo' in cid:
    print('True')
else:
    print('False')'''

cid = str(input('Digite o nome de uma Cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')