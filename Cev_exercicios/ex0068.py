from random import randint

vitoria = 0
while True:
    '''print('='*20)
    print('JOGO DE PAR OU IMPAR')
    print('='*20)'''
    pc = randint(1, 10)
    num = int(input('Digite um número: '))
    s = num + pc
    esc = ' '
    while esc not in 'PI':
       esc = str(input('Digite Par ou Impar:  ')).strip().upper()[0]
    print('='*30)
    print(f'Você escolheu {num} e o computador {pc}. Total {s}')
    print('PAR' if s%2==0 else 'IMPAR')
    if esc == 'P':
        if s % 2 == 0:
            print('Você VENCEU !!!')
            vitoria += 1
        else:
            print('Você PERDEU !!!')
            break
    if esc == 'I':
        if s % 2 == 1:
            print('Você VENCEU !!!')
            vitoria += 1
        else:
            print('Você PERDEU !!!')
            break
    print('+'*30)
    print('Vamos jogar novamente !!!')
print(f'Você venceu {vitoria} vezes')