numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'em binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'em octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'em hexadecimal é {hex(numero)[2:].upper()}')





