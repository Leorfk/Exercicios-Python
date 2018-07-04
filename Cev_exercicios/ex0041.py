from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade == 20:
    print('Sênior')
else:
    print('Master')
print('Idade do atleta {}'.format(idade))
