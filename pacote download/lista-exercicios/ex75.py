v1 = int(input('Digite um número[1 - 10]:'))
v2 = int(input('Digite um número[1 - 10]:'))
v3 = int(input('Digite um número[1 - 10]:'))
v4 = int(input('Digite um número[1 - 10]:'))
tupla = (v1, v2, v3, v4)
par = 0
if 3 in tupla:
    print(f' o numero 3 apareceu pela 1ª vez na posição {tupla.index(3)}')
else:
    print('não foi digitado o nº 3')
if 9 in tupla:
    print(f'O número 9 aparece {tupla.count(9)} vez(ezes)')
else:
    print('não foi digitado o nº 9')
print('Os valores pares foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
