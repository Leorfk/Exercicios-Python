n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('''\t\t\033[31mMENU\033[m
    [ 1 ]\tSoma
    [ 2 ]\tMultiplicação
    [ 3 ]\tMaior/Menor
    [ 4 ]\tOutros números
    [ 5 ]\tSair''')
    op = int(input('Opção desejada: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('{} X {} = {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        elif n1 < n2:
            print('O número {} é maior que o número {}'.format(n2, n1))
        else:
            print('Os números são iguais')
    elif op == 4:
        print('Digite novamente os números')
        n1 = int(input('Valor do primeiro número: '))
        n2 = int(input('Valor do segundo número: '))
        op ==0
    elif op == 5:
        print('Obrigado !!!')
    else:
        print('Valor inválido')
        op = int(input('Digite novamente sua opção'))
    print('-=-'*15)
print('Fim do programa')
