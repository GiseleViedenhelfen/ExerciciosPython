contar = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} número inteiro:'.format(c)))
    if num % 2 == 0:
        soma = soma + num
        contar = contar + 1
print('A soma dos números pares informados é {}'.format(soma))

#print precisa ficar alinhado no for, se ficar dentro ele vai foder tudo!