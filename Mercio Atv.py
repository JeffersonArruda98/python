import time
print("Está Chovendo?")
r1 = input()
if r1 == "Sim":
    print("Você tem um guarda-chuva?")
    r2 = input()
    if r2 == "Sim":
        print("Saia.")
    else:
        print("Espere um pouco.")
        time.sleep(3)
        print("Está chovendo?")
        r3 = input()
        while r3 != "Não":
            print("Espere um pouco.")
            time.sleep(3)
            print("Está chovendo?")
            r3 = input()
        print("Saia.")
else:
    print("Saia.")
