#tabuada com laço!
num = int(input('Escolha um número de 1 a 10:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
