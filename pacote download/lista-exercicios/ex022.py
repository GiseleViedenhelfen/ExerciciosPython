nome = str(input('Digite seu nome completo:')).strip()
print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('Se colocarmos todas em minúsculas, ficará: {}'.format(nome.lower()))
print('Ao todo, seu nome possui {} letras.'.format(len(nome)))
dividido = nome.split()
div = dividido[0]
print('O seu primeiro nome tem {} letras.'.format(len(div)))
