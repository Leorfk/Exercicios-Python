'''import math
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
cq1 = math.pow(c1, 2)
cq2 = math.pow(c2, 2)
hip = cq1 + cq2
hp1 = math.sqrt(hip)
print('O valor da hipotenusa é {}'.format(hp1))'''
from math import hypot
ca = float(input('Digite o valor do catedo adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hi = hypot(ca, co)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
