mercado = ('Leite 1L', 3.29,
           'Arroz 5Kg', 13.49,
           'Feijão 1Kg', 2.97,
           'Macarrão 1Kg', 1.89,
           'Corote 300ml', 2.99,
           'Vodka 1L', 5.36,
           'Cerveja', 2.99)
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*38)
for i in range(0, len(mercado)):
    if i % 2 == 0:
        print(f'{mercado[i]:.<30}',end='')
    else:
        print(f'R${mercado[i]: >6.2f}')
print('-'*38)