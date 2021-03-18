nome = str(input('Digite o seu nome:')).strip()
NOME = nome.upper()
SILVA = 'SILVA' in NOME
print('{} tem SILVA? {}'.format(nome, SILVA))
