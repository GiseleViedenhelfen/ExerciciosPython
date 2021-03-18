cidade = str(input('Qual o nome da sua cidade?')).strip()
CIDADE = cidade.upper()
dividido = CIDADE.split()
SANTO ='SANTO' in dividido[0]
print('{} começa com a palavra SANTO? {}'.format(cidade, SANTO))