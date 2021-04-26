cont50 = cont20 = cont10 = cont1 = 0
while True:
    valor = int(input('Valor a sacar: R$'))
    if valor >= 50:
        while valor // 50:
            cont50 += 1
            valor -= 50
    if valor >= 20:
        while valor // 20:
            cont20 += 1
            valor -= 20
    if valor >= 10:
        while valor // 10:
            cont10 += 1
            valor -= 10
    if valor >= 1:
        while valor // 1:
            cont1 += 1
            valor -= 1
    if valor == 0:
        break
print(f'{cont50} notas de 50,00\n{cont20} notas de 20,00\n{cont10} notas de 10,00\n{cont1} notas de 1,00')