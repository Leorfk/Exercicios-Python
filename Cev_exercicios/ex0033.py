a = int(input('Digite N1: '))
b = int(input('Digite N2: '))
c = int(input('Digite N3: '))
#   Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#   Verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))
