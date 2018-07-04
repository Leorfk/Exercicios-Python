print('='*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('CÉDULAS DISPONIVEIS 100, 50, 20, 10, 5, 2')
print('='*30)
saque = int(input('Saque: R$'))
tot = saque
maiornota = 100
contnota = 0
while True:
    if tot >= maiornota:
        tot-= maiornota
        contnota+= 1
    else:
        if contnota > 0:
            print(f'{contnota} nota(s) de R${maiornota}')
        if maiornota == 100:
            maiornota = 50
        elif maiornota == 50:
            maiornota = 20
        elif maiornota == 20:
            maiornota = 10
        elif maiornota == 10:
            maiornota = 5
        elif maiornota == 5:
            maiornota = 2
        contnota = 0
        if tot == 0:
            break
print(f'Valor do saque R${saque}')