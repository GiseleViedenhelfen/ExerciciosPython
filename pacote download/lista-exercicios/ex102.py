def fatorial(a=1, show=False):
    '''
    Função para calcular o fatorial de um número.

    :param a: o número que será feito o fatorial
    :param show: determina se a pessoa quer ou não mostrar o processo. Por padrão, False
    :return: retorna o fatorial do param a
    '''
    f = 1
    f2 = 1
    for c in range(a, 0, -1):
        f2 *= c
    v = ''
    if show == True:
        for c in range(a, 0, -1):
            f *= c
            if c == 1:
                print(f'1 = {f} ')
            else:
                v = f'{c} x '
                print(v, end='')
    else:
        return print(f2)




r1 = fatorial(3, False)
