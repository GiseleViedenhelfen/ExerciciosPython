n = 0
cont = 0
soma = 0
print('Este programa lerá quantos números digitar e fazer a soma entre eles...\n[Para que pare apenas digite 999]')
#n = int(input('Digite um número:')) #repetir fora do while faz nao contar a 'condição de parada, porém pra mim não funcionou!
while n != 999:
    n = int(input('Digite um número:'))
    soma = soma + n
    cont = cont + 1
print('Foram digitados {} números.'.format(cont - 1))
print('A soma deles foi {}'.format(soma - 999))
