#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas
#dos outros dois
reta1 = float(input('Primeira reta:'))
reta2 = float(input('Segunda reta:'))
reta3 = float(input('Terceira reta:'))
if reta1 < reta3 + reta2 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print('É possível formar triângulo com essas 3 retas!')
else:
    print('Não é possível formar um triângulo!')
