import random
total = 0
num = int(input('Digite um número inteiro:'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='') #divisível: azul
        total = total + 1
    else:
        print('\033[32m', end='') #não divisível: verde
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi dividido {} vezes'.format(num, total))
if total > 2:
    print('Não é um número primo')
else:
    print('É um número primo')