cont = n = soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'a soma dos {cont} números digitados foi {soma}')
