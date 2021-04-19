print('Digite números inteiros e obtenha a média de todos\ne também o maior e menor valor escolhido!\n')
resp = 'S'
soma = média = menor = maior = quant = 0
while resp != 'N':
    num = int(input('digite um número:'))
    quant = quant + 1
    soma = soma + num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar?[S/N]')).upper()
média = soma / quant
print(('vc digitou {} números e a soma deles é {}').format(quant, soma))
print(('A média entre eles é {}').format(média))
print(('O menor número foi {} e o maior foi {}').format(menor, maior))
