num = int(input('Digite um número entre 0 e 9999:'))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('O número {:.0f} se divide em'.format(num))
print('milhar:{}'.format(m))
print('centena:{}'.format(c))
print('dezena:{}'.format(d))
print('unidade:{}'.format(u))
