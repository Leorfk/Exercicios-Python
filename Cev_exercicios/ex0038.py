n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é {} e ele é  maior que o segundo número que é{}'.format(n1, n2))
elif n2 > n1:
    print('O segundo núemro é {} e ele é maior que o primeiro número que é {}'.format(n2, n1))
else:
    print('Os números são iguais!!!')
