from time import sleep
seg = int(input('Quantos segundos ? '))
for c in range(seg, -1, -1):
    print(c)
    sleep(1)
print('\033[7;31;40mFeliz ano novo !!!\033[m')