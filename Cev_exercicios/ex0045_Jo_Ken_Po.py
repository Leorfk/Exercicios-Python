from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
while True:
    print('''
    ******************************
    ****       JOKENPO        ****
    ****    [ 0 ] Pedra       ****
    ****    [ 1 ] Papel       ****
    ****    [ 2 ] Tesoura     ****
    ******************************''')
    player = int(input('Qual a sua jogada ? '))
    while 0 < player > 2:
        player = int(input('Valor inválido digite novamente\nQual é a sua jogada ?'))
    sleep(1)
    print('\033[31mJO')
    sleep(1)
    print('\033[32mKEN')
    sleep(1)
    print('\033[33mPO\033[m')
    if player == pc:
        print('\033[4;33mEmpate')
    elif player == 0 and pc == 2 or player == 1 and pc == 0 or player == 2 and pc == 1:
        print('\033[4;36mO Jogador ganhou!!!')
    else:
        print('\033[4;31mO computador ganhou!!!')
    print('\033[1;30m+-'*30)
    print('\033[4;33mJogador escolheu {}\nO computador escolheu {}'.format(lista[player], lista[pc]))
    resp = str(input('Deseja jogar novamente [ S ] ou [ N ]?')).upper()
    if resp == 'N':
        break;
