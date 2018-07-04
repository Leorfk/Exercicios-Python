# Palindromo
frase = str(input('escreva algum texto: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]#  Feito sem for
'''inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('A frase {} ao contrário é {}'.format(junto, inverso))
if inverso == junto:
    print('É um PALINDROMO')
else:
    print('NÃO é um PALINDROMO')