from random import randint
import time
pc = randint(0,5)# Sorteio do número
print('-=-'*30)
print('Tente adivinhar o número escolhido pela máquina!!!!!!')
print('-=-'*30)
jogador = int(input('Digite um número entre 0 e 5: '))
while jogador > 5:
    print('Valor iválido digite novamente !!!')
    jogador = int(input('Digite um numero entre 0 e 5: '))
print('Comparando resultados...')
time.sleep(3)
if jogador == pc:
    print('Acertou, parabéns!!!')
else:
    print('Oloco meu, ERROU!!!!')
print('A máquina escolheu o número {} e você escolheu o número {}'.format(pc, jogador))
