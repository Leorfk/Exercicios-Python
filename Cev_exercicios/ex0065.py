continua = n = cont = maior = menor = soma = 0
while continua != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont+=1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Deseja continuar [S/N] ?')).strip().upper()
media = soma / cont
print('A média entre os {} números digitados foi {}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
