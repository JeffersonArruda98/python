r1 = float(input('Primeira medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('os segmentos acima NÃO PODEM FORMAR triângulo')
