#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
#nesses casos percebo que sempre vai precisar atribuir valores
#ao que desejo pra ser possível fazer os if's dentro do laço...
for c in range(1, 6):
    peso = float(input('Digite o seu peso em kg:'))
    if c == 1: #se for a primeira pessoa
        maior = peso
        menor = peso
    else: #se não for a primeira pessoa
        if peso > maior:
            maior = peso #se essa pessoa for mais pesada que a primeira, o peso dela é atribuído a 'maior'
        elif peso < menor:
            menor = peso #mesma ideia do anterior
print('O maior peso foi {:.1f}kg e o menor peso foi {:.1f}kg'.format(maior, menor))