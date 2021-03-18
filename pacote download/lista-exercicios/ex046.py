from time import sleep
import emoji
print('\033[32m CONTAGEM REGRESSIVA PARA A VIRADA DO ANO!\033[m')
for c in range(11, 0, -1):
    print(c)
    sleep(1)
print('FELIZ 2020!!!')
sleep(1)
print(emoji.emojize('\033[31m:fireworks:\033[m'*8, use_aliases=True))
