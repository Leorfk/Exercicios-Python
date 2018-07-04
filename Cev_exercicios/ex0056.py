si = 0
mih = 0
homemv = ''
cf = 0
for p in range(1, 5):
    print('-'*5,'{}ºPESSOA'.format(p),'-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo  [M/F]: ')).strip()
    si += idade
    if p == 1 and sexo in 'Mm':
        mih = idade
        homemv= nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        homemv = nome
    if sexo in 'Ff' and idade < 20:
        cf += 1
mi = si // p
print('A média de idade do grupo é {}'.format(mi))
print('O homem mais velho tem {} anos e se chama {}'.format(mih, homemv))
print('O grupo tem {} mulheres com menos de 20 anos'.format(cf))