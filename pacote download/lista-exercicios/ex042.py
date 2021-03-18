print('\033[1;36m Digite 3 valores de retas e analisaremos se é possível formar um triângulo com elas')
print('\033[33m -=- \033[m'*30)
r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta:'))
r3 =float(input('Terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível a formação de um triângulo a partir dessas retas!')
    print('Será do tipo...')
    print('\033[33m -=- \033[m'*30)
    if r1 == r2 and r2 == r3: #não pode elif pq ou forma ou não!
        print('\033[32m EQUILÁTERO!\033[m')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('\033[35m ESCALENO\033[m')
    #minha resolução abaixo para isósceles
    #elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
        #print('\033[31m ISÓSCELES!\033[m')
    else:
        print('\033[31m ISÓSCELES!\033[m')
    #resolução do professor para isósceles!
else:
    print('Essas 3 retas não podem formar um triângulo...')

