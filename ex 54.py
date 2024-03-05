import time

n = int(input('Contagem regressiva:\n'))
for c in range(n, 0, -1):
    print(c)
    time.sleep(1)
print('Feliz ANO NOVO!')
