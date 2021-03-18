from random import randint
comp = randint(0, 10)
print('Vamos jogar um jogo? Penso em um número de 0 a 10 e vc tenta adivinhar ;)')
print('--'*20)
tent = 0
acerto = False
while not acerto:
    palpite = int(input('Qual número pensei?'))
    tent = tent + 1
    if palpite == comp:
        acerto = True
    else:
        if palpite < comp:
            print('meu número é maior...')
        elif palpite > comp:
            print('meu número é menor...')
print('Acertou! e com apenas {} tentativas'.format(tent))
