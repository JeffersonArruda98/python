kg = float(input('Digite seu peso:\n'))
altura = float(input('Digite sua altura\n'))

imc = kg / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} e seu estado é Abaixo do Peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f} e o seu estado é Peso Normal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f} e o seu estado é Sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f} e o seu estado é Obeso.'.format(imc))
else:
    print('Seu IMC é {:.2f} e o seu estado é Obesidade Mórbida.'.format(imc))
