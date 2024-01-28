from math import hypot
c1 = int(input("Quanto mede o cateto adjacente: "))
c2 = int(input("Quanto mede o cateto oposto: "))
hi = hypot(c1, c2)
print("A hipotenusa vai medir {:.2f}".format(hi))
