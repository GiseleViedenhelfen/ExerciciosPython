print('Escolha três números diferentes')
print('-'*40)
prim = float(input('Primeiro número:'))
seg = float(input('Segundo número:'))
ter = float(input('Terceiro e último número'))
print('-'*40)
#maior número
if prim > seg and prim > ter:
    print('O número {} é o maior'.format(prim))
if seg > prim and seg > ter:
    print('O número {} é o maior'.format(seg))
if ter > seg and ter > prim:
    print('O número {} é o maior'.format(ter))
#menor número
if prim < seg and prim < ter:
    print('O menor número é {}'.format(prim))
if seg < prim and seg < ter:
    print('O menor número é {}'.format(seg))
if ter < prim and ter < seg:
    print('O número {} é o menor'.format(ter))
