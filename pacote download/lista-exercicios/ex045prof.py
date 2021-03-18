from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual número escolhe?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VC GANHOU')
    elif jogador == 2:
        print('VC PERDEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #papel
    if jogador == 0:
        print('VC PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VC GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('VC GANHOU')
    elif jogador == 1:
        print('VC PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
