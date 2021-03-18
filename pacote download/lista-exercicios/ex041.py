from datetime import date
nasc = int(input('Em que ano vc nasceu?'))
categoria = date.today().year
idade = categoria - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM!')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
