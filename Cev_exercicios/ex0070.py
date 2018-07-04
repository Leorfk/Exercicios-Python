total = pc = cont = menor = 0
barato = ''
print('-' * 30)
print('PAPELARIA')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto R$'))
    cont += 1
    total += valor
    if valor > 1000:
        pc += 1
    op = ' '
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    while op not in 'SN':
        op = str(input('Adicionar ao carrinho ? [S/N]')).upper().strip()
    if op == 'N':
        break
print(f'Total da compra: R${total:.2f}')
print(f'Temos {pc} produto(s) custando mais de R$1.000.00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')
