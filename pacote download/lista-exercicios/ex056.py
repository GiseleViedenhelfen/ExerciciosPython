#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e
#quantas mulheres têm menos de 20 anos.
feminino = 0
masculino = 0
mulhermenor20 = 0
somaidade = 0
maioridadeh = 0
nomehv = '' #pra receber str tem que ser nesse molde de aspas!
for c in range(1, 5):
    print('======== {}ª PESSOA ========='.format(c))
    nome = str(input('Digite o seu nome:')).strip()
    print('-=-'*20)
    idade = int(input('Digite sua idade:'))
    print('-=-'*20)
    sexo = int(input('Sexo [1] M/ [2] F:'))
    somaidade = somaidade + idade
    if sexo == 1:
        masculino = masculino + 1
        if c == 1:
            maioridadeh = maioridadeh + idade
            nomehv = nome
        else:
            if idade > maioridadeh:
                maioridadeh = idade
                nomehv = nome
    if sexo == 2:
        feminino = feminino + 1
        if idade < 20:
            mulhermenor20 = mulhermenor20 + 1
    if sexo != 1 and sexo != 2:
        print('opção inválida!')
print('Temos {} mulheres e {} homens'.format(feminino, masculino))
print('Dentre as {} mulheres, {} tem menos de 20 anos'.format(feminino, mulhermenor20))
print('Dentre os {} homens, {} é o mais velho'.format(masculino, nomehv))
print('A média das idades dadas é {:.1f}'.format(somaidade/2))
