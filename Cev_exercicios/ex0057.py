sexo = str(input('Digite o seu sexo : ')).strip().upper()[0]
while sexo not in 'MF':
    print('Valor inválido')
    sexo = input('Digite novamente [M/F] ').upper().strip()[0]
print('Sexo {} registrado'.format(sexo))
