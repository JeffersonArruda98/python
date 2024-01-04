sal = float(input("Quanto você recebia? R$ "))

x = 15 * sal / 100
total = sal + x

print("Seu aumento foi de R$ {:.2f}".format(x))
print("Salário atual de R$ {:.2f}.".format(total))
