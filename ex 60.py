primeiro = int(input('Digite um termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end=' → ')
print('Acabou!')
