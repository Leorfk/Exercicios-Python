c = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 STOP]: '))
    if n != 999:
        soma +=n
        c +=1
print('Você digitou {} números e a soma entre ele é {}'.format(c, soma))
