from time import sleep
largura = float(input('Digite a Largura:\n'))
comprimento = float(input('Digite o Comprimento:\n'))
tubo = largura / 0.70

print()

metros = largura * comprimento
perfil = (largura + comprimento) * 2 / 6
mao_obra = metros * 17

print('Carregando...')
print()
sleep(2.5)

print('░░░░░░░░░░░░ LISTA DE MATERIAIS ░░░░░░░░░░░░\n')

if metros < 50:
    print('1 Kg de Arame 18.')
else:
    print('2 Kg de Arame 18.')

print()

print('A metragem do Ambiente é de:\n{:.2f}'.format(metros))
print()
print('A quantidade de Perfil F é:\n{:.2f}'.format(perfil))
print()
print('A quantidade de Perfil Tubo é:\n{:.2f}'.format(tubo))
print()
print('A mão de obra é:\nR${:.2f}'.format(mao_obra))