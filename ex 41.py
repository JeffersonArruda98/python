from time import sleep
print('Olá, vamos iniciar o seu atendimento!')
sleep(1)
print('Só um segundo...')
sleep(3)
valor_casa = float(input('Qual é o valor da casa que você deseja?\n'))
valor_salario = float(input('Qual é a média salarial que você recebe?\n'))
tempo_financiamento = int(input('Em quantos anos você pretende fazer esse empréstimo?\n'))
print('Processando...')
sleep(3)
meses = tempo_financiamento * 12
prestacao = valor_casa / meses
limite = prestacao / valor_salario * 100

if limite <= 30:
    print('Parabéns, você foi aprovado!')
    print('Sua parcela ficou apenas R${:.2f} por mês.'.format(prestacao))
else:
    print('Seu financiamento foi negado!')
    