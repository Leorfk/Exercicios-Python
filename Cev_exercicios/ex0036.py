from time import sleep
sal = float(input('Qual o valor do salário ? \033[1;36mR$'))
casa = float(input('\033[mQual o valor da casa ? \033[4;31mR$'))
anos = int(input('\033[mEm quantos anos será parcelado ? '))
parcelas = anos*12
valor = casa/parcelas
renda = sal*0.3
print('\033[1;30mAnalisando condições de financiamento...\033[m')
sleep(3)
if renda < valor:
    print('Financiamento negado\nSalário R${:.2f}\n30% do seu salário R${:.2f}\nValor da parcela R${:.2f}'.format(sal, renda, valor))
elif renda > valor:
    print('Parabéns !!!\nO seu financiamento foi Aprovado')
    print('Sua casa será parcelada em {} veses no valor de R${:.2f} por mês'.format(parcelas, valor))