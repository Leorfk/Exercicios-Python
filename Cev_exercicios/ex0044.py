print('{:=^40}'.format(' LOJAS INK '))# {:^40} é usado para deixar um determinado número de espaços
prod = float(input('Qual o valor da compra: R$'))
print('''Qual a forma de pagamento ?
[ 1 ] A vista Dinheiro/Cheque
[ 2 ] A vista no cartão
[ 3 ] Parcelado ''')
op = int(input('\nOpção: '))
if op == 1:
    total = prod * 0.90
elif op == 2:
    total = prod * 0.95
elif op == 3:
    print('''Em quantas vezes será parcelado ?
    [ 1 ] 2X no cartão
    { 2 ] 3X ou mais vezes no cartão''')
    card = int(input('Opção de parcela: '))
    if card == 1:
        total = prod * 1
        parcela = total / 2
        print('Sua compra será parcelada em 2X de R${}'.format(parcela))
    elif card == 2:
        nparc = int(input('Número de parcelas: X'))
        total = prod * 1.2
        parcela = total / nparc
        print('Sua compra será parcelada em {}X de R${:.2f}'.format(nparc, parcela))
else:
    total = prod
    print('\033[4;31mOpção inválida de pagamento\033[m')
print('A sua compra de R${:.2f} vai sair por R${:.2f}'.format(prod, total))
