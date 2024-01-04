dias = int(input("Quantos dias você alugou o carro? "))
km = int(input("Quantos KM você percorreu? "))

diaria = dias * 60
distancia = km * 0.15
total = diaria + distancia

print("O custo pelo aluguel de {} dias é de R$ {:.2f}.".format(dias, diaria))
print("O custo pela Quilometragem de {}KM rodado é de R$ {:.2f}.".format(km, distancia))
print("Somando tudo, o total é de R$ {:.2f}".format(total))
