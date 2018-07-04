dias = int(input('Quantos dias utilizou o carro ?'))
km = float(input('Quantos KM rodou ?'))
diac = dias*60
kmc = km*0.15
total = diac+kmc
print('O valor a ser pago é de : R${:.2f}'.format(total))
