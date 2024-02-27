nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota2 + nota1) / 2

if media < 5:
    print('Sua média foi {}, Você está reprovado!'.format(media))
elif media <= 6.9:
    print('Sua média foi {}, Você está de recuperação!'.format(media))
else:
    print('Sua média foi {}, Parabéns, você passou!'.format(media))
