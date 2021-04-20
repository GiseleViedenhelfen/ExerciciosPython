cont = ''
t = n = 0
print('Digite um número positivo para ver sua tabuada!')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    cont = str(input('Quer continuar? S/N ')).upper()
    if c == 'N':
        break
