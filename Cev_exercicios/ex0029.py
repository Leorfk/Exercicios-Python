km = int(input('Digite a velocidade em que o carro passou: '))
multa = (km-80)*7
print('-='*50)
if km >80:
    print('Parabéns, Você foi multado no valor de R${} por ter excedido o limite de velocidade que é de 80km/h'.format(multa))
else:
    print('Parabéns, continue dirigindo em segurança')
print('-='*50)
print('Você estava a {}km/h'.format(km))
