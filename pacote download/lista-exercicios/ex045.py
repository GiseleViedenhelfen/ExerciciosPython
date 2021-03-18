from random import choice   #Para selecionar um elemento aleatório de uma sequência não vazia, podemos usar choice(seq).
                            #Com randint(), somos limitados a selecionar números de uma série.
                            #choice(seq) nos permite escolher um número de qualquer sequência quisermos.
from time import sleep
print('Vamos jogar [pedra, papel ou tesoura]?')
escolha = str(input('escolha um dos três:')).lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
ppt = ['pedra', 'papel', 'tesoura']
computador = choice(ppt)
#empate
if computador == 'pedra' and escolha == 'pedra' or computador == 'papel' and escolha == 'papel' or computador == 'tesoura' and escolha == 'tesoura':
    print('Eu também escolhi {}... Empatamos!'.format(computador))
#papel
elif escolha == 'papel' and computador == 'pedra' or escolha == 'tesoura' and computador == 'papel':
    print('Eu escolhi {}... Vc ganhou!'.format(computador))
elif computador == 'papel' and escolha == 'pedra' or computador == 'tesoura' and escolha == 'papel':
    print('Eu escolhi {}, GANHEI!'.format(computador))
#tesoura e pedra
elif escolha == 'pedra' and computador == 'tesoura':
    print('Eu escolhi {}... Vc ganhou!'.format(computador))
elif 'pedra' in computador and 'tesoura' in escolha:
    print('Eu escolhi {}, GANHEI!'.format(computador))