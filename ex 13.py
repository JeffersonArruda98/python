print("Vamos pintar uma parede!")
larg = float(input("Qual a largura da parede: "))
alt = float(input("Qual a altura da parede: "))

area = larg * alt
tinta = area / 2
print("A área em M² da sua parede é {}M² e a quantidade de tinta que você vai precisar gastar é {}L de tinta.".format(area, tinta))
