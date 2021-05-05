palavras = ('aula', 'xicara')
for p in palavras:
    print(f'\n a palavra "{p}" tem as vogais:', end=' ')
    for l in p: #cada palavra da tupla é uma lista, podendo fazer novamente o for
        if l in 'aeiou':
            print(l, end=' ')
