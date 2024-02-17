vel = int(input('Qual é a velocidade do seu carro?'))
total = (vel - 80) * 7
if vel <= 80:
    print('Você está na velocidade permitida.')
else:
    print('Você foi mutado por estar acima da velocidade permitida.')
    print('A multa total foi de R${:.0f}!'.format(total))
