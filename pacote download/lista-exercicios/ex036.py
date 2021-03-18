valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos vc pretende pagá-la?'))
prestacao = valor / (anos * 12)
minimo = sal * 30 / 100
if prestacao <= minimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
