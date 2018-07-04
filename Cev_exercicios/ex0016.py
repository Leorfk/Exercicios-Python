'''import math
num = float(input('Digite um número'))
conv = math.floor(num)
print('O numero arredondado é {}'.format(conv))'''
from math import trunc
num = float(input('Digite um número'))
print('O número digitado foi {} e ele arredondado é {}'.format(num, trunc(num)))
#Da para fazer sem a biblioteca usando o int ex: .format(num, int(num))
