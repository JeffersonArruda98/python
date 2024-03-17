from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoas in range(1, 8, 1):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - ano
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} peassoas maiores de idade.'.format(totalMaior))
print('e também tivemos {} pessoas menores de idade.'.format(totalMenor))
