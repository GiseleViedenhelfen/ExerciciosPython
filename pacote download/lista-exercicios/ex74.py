from random import randint
menor = maior = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {n}')
print(f'o menor valor sorteado foi {max(n)} e o menor foi {min(n)}')