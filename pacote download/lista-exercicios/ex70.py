total = MB = c = mil = 0
barato = '' # para calcular o mais barato e nomear o mais barato precisa de variaveis diferentes!
while True:
    nome = str(input('Nome do Produto: '))
    preço = int(input('Qual o Preço? R$ '))
    c += 1
    total += preço
    if preço > 1000:
        mil += 1
    if c == 1:
        MB = preço
        barato = nome
    else:
        if preço < MB:
            MB = preço
            barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastrados {c} produto(s)\nO mais barato foi {barato} e a quantia de produtos de mais de R$ 1.000,00 foi {mil}\nO preço total foi R${total}')