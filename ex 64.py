maior = 0
menor = 0
for i in range(1, 6,):
    peso = float(input('Peso da {} pessoa: '.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O peso maior é o {}Kg.'.format(maior))
print('O menor peso é o {}Kg.'.format(menor))
