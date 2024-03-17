media = 0
nomeVelho = ''
mulherNova = 0
maiorIdadeH = 0
for i in range(1, 5):
    print('------- {} Pessoa -------'.format(i))
    print('Qual é o seu nome? ')
    nome = str(input())
    print('Qual é a sua idade? ')
    idade = int(input())
    print('Qual seu sexo (M/F)? ')
    sexo = str(input())
    media += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherNova += 1
soma = media / 4
print('A idade média e de {:.0f}'.format(soma))
print('O nome do mais velho é {} e tem {} anos.'.format(nomeVelho, maiorIdadeH))
print('Ao total são {} com menos de 20 anos.'.format(mulherNova))
