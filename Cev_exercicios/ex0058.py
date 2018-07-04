from random import randint
import time
tent = 0
pc = randint(0,10)# Sorteio do número
print('-=-'*30)
print('Tente adivinhar o número escolhido pela máquina!!!!!!')
print('-=-'*30)
jogador = int(input('Digite um numero entre 0 e 10: '))# Número escolhido pelo usuário
print('Comparando resultados...')
time.sleep(1)
while jogador != pc:
        if jogador < pc:
                print('Errou o valor é maior')
                jogador = int(input('Tente novamente!!!\nDigite um número entre 0 e 10: '))
        elif jogador > pc:
                print('Errou o valor é menor')
                jogador = int(input('Tente novamente!!!\nDigite um número entre 0 e 10: '))
        tent +=1
print('\nAcertou, Parabéns')
print('A máquina escolheu o número {} e você escolheu o número {}'.format(pc, jogador))
print('Tentativas {} '.format(tent+1))
