#ler sexo 'M' ou 'F'. Se não for, digitar de novo!
Feminino = ''
Masculino = ''
sexo = ''
sexo = str(input('Qual seu sexo? M/F:')).upper().strip()
while sexo not in 'FM':
    sexo = str(input('Opção inválida! escolha M ou F: ')).upper().strip()
print('Sexo {} registrado!'.format(sexo))
