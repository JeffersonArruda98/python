from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('Suas opções:\n'
      '1 - Pedra;\n'
      '2 - Papel;\n'
      '3 - Tesoura.')
jogador = int(input('Qual é a sua jogada?\n'))
print('Computador jogou {}.'.format(item[computador]))
print('Jogador jogou {}.'.format(item[jogador]))

if computador == 0:
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador venceu.')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida.')

elif computador == 0:
    if jogador == 0:
        print('Computador venceu.')
    elif jogador == 1:
        print('Empate.')
    elif jogador == 2:
        print('Jogador venceu.')
    else:
        print('Jogada inválida.')

elif computador == 0:
    if jogador == 0:
        print('Jogador venceu.')
    elif jogador == 1:
        print('Computador venceu.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')

