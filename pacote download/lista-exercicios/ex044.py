valor = (float(input('Qual o valor do produto? R$')))
print('''Existem algumas opções de pagamento...
Opção 1: à vista dinheiro ou cheque
Opção 2: à vista no cartão
Opção 3: em até 2x no cartão
Opção 4: 3x ou mais no cartão''')
print('\033[32m-=-\033[m'*20)
condição = str(input('Qual das opções é a escolhida?')).lower()
if 'um' in condição or condição == '1':
    print('O valor R$ {:.2f} receberá um desconto de 10% ficando R${:.2f}'.format(valor, valor - valor * 10/100))
elif 'dois' in condição or condição == '2':
    print('O valor R${:.2f} receberá um desconto de 5% ficando R${:.2f}'.format(valor, valor - valor * 5/100))
elif 'três' in condição or condição == '3' or 'tres' in condição:
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(valor/2))
    print('O valor R${:.2f} não receberá desconto, mas também não terá juros!'.format(valor))
elif 'quatro' in condição or condição == '4':
    parcelas = int(input('Quantas parcelas? escreva em numerais!'))
    print('O valor R${:.2f} receberá 20% de juros, ficando em R${:.2f}'.format(valor,  valor + valor * 20/100))
    print('Vc pagará em {} parcelas de R$ {:.2f} cada'.format(parcelas, (valor + valor*20/100)/parcelas))

else:
    print('Pfv escolha uma das opções acima.')
