num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases númericas abaixo:')
print('1 = binário')
print('2 = octal')
print('3 = hexadecimal')
escolha = int(input('Qual a opção escolhida?'))
if escolha == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))#2: para cortar o que não é número, mas indicação da categoria
elif escolha == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))#2: para cortar o que não é número, mas indicação da categoria
elif escolha == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))#2: para cortar o que não é número, mas indicação da categoria
else:
    print('pfv, escolha uma opção válida!')
