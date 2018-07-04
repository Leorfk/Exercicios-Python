print('='*30)
print('{:^30}'.format('TABUADA'))
print('='*30)
while True:
    t = int(input('Digite um número:'))
    for c in range(1, 11):
        print('{} X {} = {}'.format(t, c, t*c))
        c+=1
    esc = str(input('Deseja repetir [S/N] ')).strip().upper()
    if esc not in 'S':
        break