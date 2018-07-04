t = int(input('Digite o termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = t + (10 - 1)*r
for c in range(t, d+1, r):
    print(c, end='-')
print('Fim')