t = int(input('Digite o termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
c2 = 0
mais = 10
while mais !=0:
    c2 += mais
    while cont <= c2:
        print(t, end='-')
        t +=r
        cont+=1
    mais = int(input('\nQauntos termos mais deseja ver ?'))
print('Foram mostrados {} termos de uma PA'.format(c2))