campeonato = ('Flamengo', 'Atlético-MG', 'São Paulo', 'Internacional', 'Grêmio', 'Palmeiras', 'Sport', 'Cruzeiro', 'Botafogo', 'Galinha Preta', 'Vasco', 'Fluminense', 'América-MG', 'Chapecoense', 'Santos', 'Vitória', 'Bahia', 'Paraná', 'Atlético-PR', 'Ceará')
op = 0
while op != 5:
    print('''
    __________________________________
    |     Lista do Brasileirão       |
    |--------------------------------|
    |   [ 1 ] Cinco primeiros        |
    |   [ 2 ] Zona de rebaixamento   |
    |   [ 3 ] Ordem alfabética       |
    |   [ 4 ] Posição do Chapecoense |
    |   [ 5 ] Sair                   |
    |________________________________|
    ''')
    op = int(input('Opção: '))
    if 1< op > 5:
        op = int(input('Digite novamente: '))
    if op == 1:
        print(campeonato[0:5])
    if op == 2:
        print(campeonato[-4:])
    if op == 3:
        times = list(campeonato)
        times.sort()
        print('Times por ordem alfabética')
        for i in range(0, len(times)):
            print(times[i])
        #print(sorted(campeonato)) forma feita sem converter tupla em lista
    if op == 4:
        for i in range(0, len(campeonato)):
            if campeonato[i] == 'Chapecoense':
                print(f'{i+1}º {campeonato[i]}')
    if op == 5:
        break