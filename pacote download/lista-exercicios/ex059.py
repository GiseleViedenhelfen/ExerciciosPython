from time import sleep
desistir = False
soma = 0
multiplicação = 0
maior = 0
primeiro = int(input('1º número:'))
segundo = int(input('2º número'))
while not desistir:
    print('-=-'*10)
    print('''
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    print('-=-'*10)
    escolha = int(input('Qual a opção:'))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(primeiro, segundo, primeiro + segundo))
    elif escolha == 2:
        print('O resultado da multiplicação de {} e {} é {}'.format(primeiro, segundo, primeiro * segundo))
    elif escolha == 3:
        if primeiro > segundo:
            maior = primeiro
        if primeiro < segundo:
             maior = segundo
        print('O maior número entre {} e {} é {}'.format(primeiro, segundo, maior))
        if primeiro == segundo:
            print('Os dois números são iguais...')
    elif escolha == 5:
        desistir = True
    elif escolha == 4:
        primeiro = int(input('1º número:'))
        segundo = int(input('2º número'))
    else:
        print('Opção inválida!')
    sleep(2)