num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
num3 = float(input('Digite o terceiro número:\n'))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('Os números acima formam um triangulo ', end='')
    if num1 == num2 == num3:
        print('Equilatero!')
    elif num1 != num2 != num3 != num1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Não foi possível formar um triangulo com os dados informados. tente novamente.')

