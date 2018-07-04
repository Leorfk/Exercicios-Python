from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if ano - nasc >=18:
  #      print('Você é maior de idade')
        maior += 1
    else:
    #    print('Você é menor de idade')
        menor += 1
print('Maiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))
