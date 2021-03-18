from datetime import date
contador = 0
totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(0, 3):
    nasc = int(input('Em que ano vc nasceu?'))
    contador = contador + 1
    idade = atual - nasc
    if idade >= 18: #a condição tem que estar dentro
        totmaior = totmaior + 1 #total maiores de idade
    else:
        totmenor = totmenor + 1
print('de {} pessoas, {} é/são maior(es) de idade e {} menor(es) de idade'.format(c, totmaior, totmenor))
# print que mostra o resultado precisa estar fora!