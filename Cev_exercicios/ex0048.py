'''mul = 0
for c in range(1, 500):
    if c % 3 ==0:
        mul += c
    soma = mul+ 1
print(soma)'''
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i %3 == 0:
        print(i, end=' ')
        soma += i
        cont += 1
print('\nA soma de todos os {} números multiplos de 3 éigual a {}'.format(cont, soma))