n = int(input('escolha um número:'))
if n % 2 == 0:#números pares não tem resto na divisão. não funciona importar math!
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))
