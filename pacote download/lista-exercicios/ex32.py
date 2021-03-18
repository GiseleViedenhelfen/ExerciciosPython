from datetime import date
ano = int(input('Escolha um ano:'))
if ano == 0:
    ano = date.today().year #esse comando analisa o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
