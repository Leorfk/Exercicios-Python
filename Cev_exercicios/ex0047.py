'''cont = 0
for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' ')
        cont += 1
print('\n\nExistem {} números par entre 1 e 50'.format(cont))'''
for n in range(2, 51, 2):
    print(n, end=' ')