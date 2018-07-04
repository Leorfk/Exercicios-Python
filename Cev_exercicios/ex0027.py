nome = str(input('Digite o seu nome: ')).strip()
separa = nome.split()
print('Muito prazer, {}'.format(separa[0]))
print('O seu ultimo nome é {}'.format(separa[-1]))
