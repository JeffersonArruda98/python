nome = str(input('qual é o seu nome? '))
if nome == 'Jefferson':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome =='Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino você tem!')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia, {}!'.format(nome))
