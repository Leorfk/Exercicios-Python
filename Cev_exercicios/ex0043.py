peso = float(input('Informe o seu peso: (Kg) '))
altura = float(input('Informe a sua altura: (m) '))
imc = peso / altura**2
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:#    >=18.5 imc <=25 o Python aceita este tipo de entrada
    print('Você está no peso ideal')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso\nÉ melhor se cuidar!!!')
elif imc >= 30 and imc < 40:
    print('Você está Obeso(a)\nVocê precisa melhorar o seu estilo de vida !!!!')
elif imc >=40:
    print('Você está com obesidade morbida !!!!\nPor favor procure um médico !!!!')
print('IMC: {:.2f}'.format(imc))
