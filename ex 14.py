preco = int(input("Qual o total da sua compra? "))

x = 5 * preco / 100
total = preco - x
print("Seu desconto de 5% foi de R${}.".format(x))
print("Seu valor final é R${}.".format(total))