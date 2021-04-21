M = H = P = M1 = 0
sexo = ''
print('CADASTRO')
c = ''
while True:
    sexo = str(input('sexo [F/M]: ')).upper()
    if sexo != 'F':
        M += 1
    if sexo == 'M':
        H += 1
    idade = int(input('Idade [apenas números]: '))
    if idade > 18:
        P += 1
    if idade < 20 and sexo == 'F':
        M1 += 1
    c = str(input('Quer continuar? [S/N] ')).upper()
    if c == 'N':
        break
print(f'Foram cadastradas {P} pessoas maior(es) de 18 anos.\nDentre esses, {M1} mulher(es) menor(es) de 20 anos.')
