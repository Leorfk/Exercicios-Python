#       Tabuada
n = int(input('Qual tabuada deseja consultar ?'))
for c in range(1, 10+1):
    print('{} X {} = {}'.format(c, n, c*n))