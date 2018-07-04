km = int(input('Digite a distância da sua viagem: '))
if km <= 200:
    print('O valor da sua viagem será de R${:.2f}'.format(km*0.5))
else:
    print('O valor da sua viagem será de R${:.2f}'.format(km*0.45))
print('Você viajou {}km'.format(km))