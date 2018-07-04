num = int(input('Digite um número inteiro:'))
while True:
    print('''Escolha uma das bases para a conversão: 
    [ 1 ] Converter para BINÁRIO
    [ 2 ] Converter para OCTAL
    [ 3 ] Converter para HEXADECIMAL''')
    op = int(input('Sua opção:  '))
    if op == 1:
        print('O número {} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
    elif op == 2:
        print('O número {} convertido para octal é igual a {}'.format(num, oct(num))[2:])
    elif op == 3:
        print('O número {} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
    else:
        print('Valor inválido sua anta')
        print('+'*30)
    esc = str(input('Deseja fazer outra conversão [S/N] ?')).upper().strip()
    if esc == 'N':
        break
print('FIM')