lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um número: para a posição {c}:  ")))
    if c == 0:
        menor = menor = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]

print(f"foi formada a lista {lista}")
print(f"O menor valor foi {menor} ")
for i, v in enumerate(lista):
    if v == menor:
        print(f"na posição {i}")
print(f"no maior valor foi {maior}")
for i, v in enumerate(lista):
    if v == maior:
        print(f"na posição {i}")