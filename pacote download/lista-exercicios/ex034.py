salario = float(input('Qual o seu salário? R$'))
if salario >= 1250:
    print('Você ganhará um aumento de 10%, ficando com um total de R$ {:.2f}.'.format(salario + (salario * 10/100)))
else:
    print('Você ganhará um aumento de 15%, ficando com R$ {:.2f}'.format(salario + (salario * 15/100)))
