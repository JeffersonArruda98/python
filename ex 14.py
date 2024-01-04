preco = int(input("Qual o total da sua compra? R$ "))

x = preco * 5 / 100
total = preco - x
print("Seu desconto de 5% foi de R${:.2f}.".format(x))
print("Seu valor final é R${:.2f}.".format(total))
