nasc = int(input('Qual é o ano em que você nasceu?\n'))
idade = 2024 - nasc
falta = 18 - idade
passou = idade - 18
if idade == 18:
    print('Já está na hora de se alistar.')
elif idade > 18:
    print('Já passou {} anos do tempo de se alistar.'.format(passou))
elif idade < 18:
    print('Ainda falta {} anos para se alistar.'.format(falta))
