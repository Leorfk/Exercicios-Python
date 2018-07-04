s = cont = 0
while True:
    n = int(input('Digite um número [999 STOP]: '))
    if n ==999:
        break
    cont+= 1
    s +=n
print(f'Você digitou {cont} e a somatória deles é igual á {s}')
