num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\nO númeor {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
