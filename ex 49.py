print('======= Loja Law =======')
valor = float(input('Preço das compras:\nR$ '))
print('Qual a forma de pagamento?\n'
      '[ 1 ] - Á vista em espécie;\n'
      '[ 2 ] - Á vista no cartão;\n'
      '[ 3 ] - Em 2x no cartão;\n'
      '[ 4 ] - Em 3x ou mais no cartão.')
opcao = int(input('Qual é a opção de pagamento?\n'))

um = valor - (10 / 100 * valor)
dois = valor - (5 / 100 * valor)
x = valor / 2

if opcao == 1:
    print('Você ganhou 10% de desconto!!')
    print('O valor total da sua compra ficou R${:.2f}'.format(um))
elif opcao == 2:
    print('Você ganhou 5% de desconto!!')
    print('O valor total da sua compra ficou R${:.2f}'.format(dois))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(x))
elif opcao == 4:
    divisao = int(input('Em quantas vezes você quer parcelar? (em até 10x)\n'))
    xs = valor / divisao
    print('Sua compra será parcelada em {:.0f}x de R${:.2f}.'.format(divisao, xs))
else:
    print('Você escolheu a opção errada, tente novamente.')