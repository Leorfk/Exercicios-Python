a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b+c and b < a+c and c < a+b:
    print('Os segmentos acima podem formar um triângulo')
    if a == b == c:
        print('E este triângulo é equilátero, pois tem todos os lados iguais')
    elif a == b or a == c or b == c or c == b:
        print('E este triângulo é Isóceles, pois ele possui dois lados iguais')
    elif a != b and a != c and b != a and b != c:
        print('E este triângulo é escaleno, pois possui todos os lados diferentes')
else:
    print('Os segmentos acima não podem formar um triângulo')
print('-=-'*30)