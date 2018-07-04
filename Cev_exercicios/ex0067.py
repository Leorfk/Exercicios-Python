print('-'*20)
print('TABUADA')
print('-'*20)
while True:
    c = 0
    num = int(input('Qual tabuada deseja ver ?'))
    if num < 0:
        break
        print('-'*20)
    while c <= 9:
        c += 1
        print(f'{num} X {c} = {num * c}')
    print('-'*20)
print('FIM DO PROGRAMA')
