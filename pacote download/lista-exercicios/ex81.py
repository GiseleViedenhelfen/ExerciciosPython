lista = []
cont = 0
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    cont += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    if cont in "N":
        break
    if cont not in "SN":
        print("por favor,digite S ou N")
lista.sort(reverse=True)
print(lista)
print(f"foram digitados {cont} números")
if 5 in lista:
    print("O número 5 faz parte da lista!")
else:
    print("A lista não tem o número 5!")