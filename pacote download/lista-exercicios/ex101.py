def voto(a):
    from datetime import date #importa só dentro da função
    atual = date.today().year
    v = atual - a
    if 17 < v < 64:
        return f'com {v} anos o voto é obrigatório'
    if 16 > v:
        return f'com {v} anos não é permitido votar'
    if 65 < v or 18 > v > 15:
        return f'com {v} anos o voto é facultativo'


r1 = resp = int(input('Ano de nascimento: '))
print(voto(resp))

