viagem = float(input('Qual a distância da sua viagem em km?'))
if viagem <= 200:
    print('Sua viagem custará R$ {:.2f}'.format(viagem*0.50))
else:
    print('Sua viagem custará R${:.2f}'.format(viagem*0.45))