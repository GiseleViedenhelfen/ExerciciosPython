v = float(input('Qual a velocidade está? em km/h'))
multa = 7*(v - 80)
if v > 80:
    print('Você está acima da velocidade permitida!')
    print('Sua multa custará R${:.2f}.'.format(multa))
