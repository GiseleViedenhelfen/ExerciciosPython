print('PA com While:')
print('-=' * 10)
TI = int(input('Digite o primeiro termo da PA: '))
R = int(input('Digite a razão da PA: '))
termo = TI
cont = 1
total = 0
MT = 10
while MT != 0:
    total = total + MT
    while cont <= total:
        print('{} ;'.format(termo), end='')
        termo = termo + R
        cont = cont + 1
    print('Pausa')
    MT = int(input('Quantos termos vc ainda quer ver?'))
print('a PA mostrada teve {} termos mostrados!'.format(cont - 1))




