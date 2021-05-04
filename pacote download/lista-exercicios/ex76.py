lista = ('Pão', 5.00, 'Leite', 3.00, 'Frango', 15.00)
for pos in range(0, len(lista)):
    if pos % 2 == 0:# se a posição é par = é nome
        print(f'{lista[pos]:.<30}', end='')
    else: #se a posição é impar o item é preço
        print(f' R${lista[pos]:>8.2f}')