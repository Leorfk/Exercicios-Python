n1 = int(input('Digite o valor de N1: '))
n2 = int(input('Digite o valor de N2: '))
n3 = int(input('Digite o valor de N3: '))
n4 = int(input('Digite o valor de N4: '))
tupla = (n1, n2, n3, n4)
print(tupla)
if tupla.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('Não foi encontrado nenhum número 3')
else:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3)+1}º posição')

for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i])