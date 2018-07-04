
num = 0
n = int(input('Digite um número: '))
for c in range(1,n + 1):
    if n % c ==0:
        print('\033[36m', end=' ')
        num += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi dividido por {} números'.format(n, num))
if num == 2:
    print('E ele é PRIMO')
else:
    print('E ele NÃO é primo')