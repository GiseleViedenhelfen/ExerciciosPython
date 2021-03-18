from random import randint
computador = randint(0, 5) #faz o computador escolher aleatoriamente
print('Vamos jogar um jogo? Penso em um número e vc tenta adivinhar ;)')
print('--'*20)
esc = int(input('Qual o nº?')) #jogador tenta adivinhar
if esc == computador:
    print('vc acertou!')
else:
    print('mais sorte na próxima! Pensei no n {} e não no {}...'.format(computador, esc))
