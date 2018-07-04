n = int(input('Digite um número:'))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *=c
print('{}'.format(f))