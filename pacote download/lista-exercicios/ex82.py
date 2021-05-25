lista = []
impar = []
par = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    cont = (str(input("Quer continuar? [S/N]"))).upper()
    if cont in "N":
        break
    if cont not in "SN":
        print("por favor,digite S ou N")
for l in lista:
    if l % 2 == 0:
        par.append(l)
    else:
        impar.append(l)
print(f"A lista é {lista}")
print(f"Os pares são {par}")
print(f"Os ímpares são {impar}")