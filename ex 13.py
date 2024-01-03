print("Vamos pintar uma parede!")
larg = float(input("Qual a largura da parede: "))
alt = float(input("Qual a altura da parede: "))

x = larg * alt
d = x / 2
print("A área em M² da sua parede é {} e a quantidade de tinta que você vai precisar gastar é {}".format(x, d))
