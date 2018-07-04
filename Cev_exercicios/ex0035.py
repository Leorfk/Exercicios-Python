from time import sleep
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta:'))
c = float(input('Digite o valor da terceira reta:'))
print('-=-'*30)
print('Verificando se formam um triângulo...')
print('-=-'*30)
sleep(3)
if a < b+c and b < a+c and c < a+b:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
print('-=-'*30)
