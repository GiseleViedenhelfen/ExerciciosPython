classificação = ('Corinthians','Palmeiras','Santos', 'Grêmio','Cruzeiro','Flamengo','Vasco da Gama',
                 'Chapecoense','Atlético-MG','Botafogo','Athletico-PR','Bahia','São Paulo','Fluminense',
                 'Sport','Vitória','Coritiba','Avaí','Ponte Preta','Atlético-GO')
print('Os 5 primeiros colocados foram:')
print(classificação[0:5])
print('Os 4 últimos colocados foram:')
print(classificação[16:21])
print('Os times em ordem alfabética são:')
print(sorted(classificação))
print(f'O Chapecoense ficou em {classificação.index("Chapecoense")+1} lugar')
