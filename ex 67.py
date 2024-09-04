# Programa que simula uma fila de banco

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)}')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operacoes = input('Operações (F, A ou S): ').upper()
    for operacao in operacoes:
        if operacao == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'\nCliente {atendido} atendido.')
            else:
                print('Fila vázia! Ninguém para atender.')
        elif operacao == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif operacao == 'S':
            break
        else:
            print(f'\nOperação inválida: {operacao}')
    if operacao == 'S':
        break
