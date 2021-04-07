print('Calcularemos a seguir a sequencia de Fibonacci') #soma o último e penúltimos termos para criar o prox.
n = int(input('Quantos termos quer ver?'))
T1 = 0 #por padrão começa com 0 e 1!
T2 = 1
print('{} - {}'.format(T1, T2), end='')
cont = 3 #começa no 3 pq o 1º e 2º termo já foram mostrados
while cont <= n:
    T3 = T1 + T2 #essa substituição fará que a contagem caminhe, sendo possível fazer o T2 e T3 mudarem
                 #conforme a quantia de termos.
    print(' - {}'.format(T3), end='') #só vai o T3 pq os dois primeiros já estão fixos
    T1 = T2
    T2 = T3
    cont = cont + 1  # se faz isso para que cada termo seja adicionado, se n o while não poderá fazer a contagem se
    # segue sendo menor que o 'n'
print(' - Fim')
