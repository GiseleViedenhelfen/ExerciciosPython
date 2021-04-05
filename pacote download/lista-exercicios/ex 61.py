print('PA com While:')
print('-=' * 10)
TI = int(input('Digite o primeiro termo da PA: '))
R = int(input('Digite a razão da PA: '))
termo = TI
cont = 1
while cont <= 10:
    print('{} ;'.format(termo), end='')
    termo = termo + R
    cont = cont + 1
print('Fim')