from random import randint
from time import sleep
comp = randint(0, 5)
print('--=--' * 12)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('--=--' * 12)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if player == comp:
    print('Parabéns, você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não {}'.format(comp, player))
