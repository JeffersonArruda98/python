from math import radians, sin, cos, tan
ang = int(input("Digite o ângulo que você deseja: "))

sen = sin(radians(ang))
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, sen))
cos = cos(radians(ang))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cos))
tg = tan(radians(ang))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(ang, tg))