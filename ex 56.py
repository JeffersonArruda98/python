i = int(input('Inicio da contagem:\n'))
f = int(input('Fim da contagem:\n'))
soma = 0
for c in range(i, f, 3):
    soma += c
    print(c)
print('A soma total dos números ímpares é de {}.'.format(soma))
