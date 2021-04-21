from random import randint
print('JOGO DE PAR OU ÍMPAR!')
jogador = soma = 0
escolha = ''
vitoria = 0
while True:
    jogador = int(input('escolha um número:'))
    escolha = str(input('Par ou Ímpar? [P/I]')).upper()
    computador = randint(1, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'vc jogou {jogador} e o computador {computador}, a soma dos valores é {soma}. PAR!')
        if escolha == 'P':
            vitoria += 1
        if escolha == 'I':
            break
    if soma % 2 != 0:
        print(f'vc jogou {jogador} e o computador {computador}, a soma dos valores é {soma}. ÍMPAR!')
        if escolha == 'I':
            vitoria += 1
        if escolha == 'P':
            break
print(f'vc teve {vitoria} acerto(s). Parabéns!')