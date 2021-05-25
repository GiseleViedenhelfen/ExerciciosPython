lista = []
while True:
    n = (int(input("Digite um número:")))
    if n in lista:
        print("Esse numero já foi escolhido anteriormente")
    else:
        lista.append(n)
        print("Valor adicionado!")
    cont = (str(input("Quer continuar? [S/N]"))).upper()
    if cont in "N":
        break
    if cont not in "SN":
        print("por favor,digite S ou N")
lista.sort()
print(f"em ordem a lista fica: {lista}")
print("Fim")