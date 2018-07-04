n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Parabéns!!!!\n\nVocê foi aprovado\nMédia: \033[36m{}\033[m'.format(m))
elif m >= 5 and m <=6.9:
    print('Atenção!!!\n\n Você está de recuperação sua média foi \033[32m{}'.format(m))
elif m <= 4.9:
    print('Você foi reprovado\nTe vejo no proximo semestre\nMédia: \033[31m{}'.format(m))