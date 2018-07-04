numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    i = int(input('Digite um número entre Zero e Vinte: '))
    while i < 0 > 20:
        i = int(input('Valor inválido, digite novamente um número entre Zero e Vinte: '))
    print(f'O número digitado foi {i} e ele escrito por extenso fica assim:\033[36m {numeros[i]}')
    resp = str(input('\033[mDeseja ver outro número [S] ou [N]?'))
    if resp == 'N':
        break