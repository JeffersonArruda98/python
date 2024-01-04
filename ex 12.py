real = int(input("Quantos reais você tem na carteira? R$ "))

dolar = real / 4.92
print("Sabendo que a cotação atual é de U$4,92")
print("Com R$ {:.2f} você tem U$ {:.2f}.".format(real, dolar))
