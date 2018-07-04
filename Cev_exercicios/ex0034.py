sal = float(input('Digite o seu salário: '))
if sal > 1250.00:
    au = sal * 0.1
    ns = sal * 1.1
    print('O aumento foi de R${:.2f} e o novo salário é de R${:.2f}'.format(au, ns))
else:
    au = sal *0.15
    ns = sal *1.15
    print('O aumento foi de R${:.2f} e o novo salário é de R${:.2f}'.format(au, ns))
print('Salário antigo R${:.2f}'.format(sal))
