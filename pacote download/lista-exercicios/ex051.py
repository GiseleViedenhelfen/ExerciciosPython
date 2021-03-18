from time import sleep
print('escolha o primeiro termo e a razão da PA...')
sleep(1)
T = int(input('primeiro termo:')) #tem que ter a sinalização de não ser um str!
R = int(input('razão:'))
D = T + (10-1)*R
for c in range(T, D + R, R):
    print('{}'.format(c))
print('Aí estão!')