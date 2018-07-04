homem = mulher = mais18 = 0
while True:
    print('='*30)
    print('Cadastro de pessoa fisica')
    print('='*30)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if idade > 18:
        mais18 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja cadastrar outra pessoa [S/N] ?')).upper().strip()
    if op == 'N':
        break
print(f'''Cadastro Finalizado !!!
{homem} Homens cadastrados
{mulher} mulheres com menos de 20 anos
{mais18} pessoas com mais de 18 anos''')