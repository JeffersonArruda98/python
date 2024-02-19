num = int(input('Digite um número:\n'))
print('Escolha qual base você quer converter:\n'
              '1 - Binário;\n'
              '2 - Octal;\n'
              '3 - Hexadecimal.')
x = int(input('Sua opção: '))
if x == 1:
    print('O número {} convertido para Binário é {}.'.format(num, bin(num)[2:]))
elif x == 2:
    print('O número {} convertido para Octal é {}.'.format(num, oct(num)[2:]))
elif x == 3:
    print('O número {} convertido para Hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Você digitou errado! Tente novamente...')
