from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} terá {}anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar neste ano')
elif idade < 18:
    print('Ainda falta {} anos para chegar a sua hora, soldado'.format(18-idade))
elif idade > 18:
    print('Você ja deveria ter se alistado a {} anos'.format(idade - 18))
