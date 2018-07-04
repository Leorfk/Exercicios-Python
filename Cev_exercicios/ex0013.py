sal = float(input('Digite o valor do sálario: R$'))
ns = sal*1.15
au = ns-sal
print('Seu novo sálario é de R${:.2f}, você recebeu um aumento de R${:.2f}'.format(ns, au))
