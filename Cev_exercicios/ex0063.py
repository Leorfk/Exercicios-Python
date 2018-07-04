'''print('_'*30)
print('Sequência de Fibonacci')
print('_'*30)
t = int(input('Quantos termos deseja ver: '))
t1 = 0
t2 = 1
print('=-'*30)
print('{} - {} -'.format(t1, t2), end='')
cont =3
while cont <= t:
    t3 = t1 + t2
    print(' {} - '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont+= 1
print('Acabou !!!')'''
t = int(input('Quantidade de termos: '))
c1 = 0
c2 = 1
print('+='*100)
print('{} - {} '.format(c1, c2),end='')
cont = 3
for cont in range(1, t):
    c3 = c1 +c2
    print('- {} '.format(c3),end='')
    c1 = c2
    c2 = c3
    cont+=1
print('\n')
print('+='*100)
print('\nFim')
