nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2
print('A média para notas {:.1f} e {:.1f} é {}.'.format(nota1, nota2, media))
if media < 5:
    print('\033[31m Vc foi reprovado!')
elif 6.9 >= media >= 5:
    print('Vc está em recuperação...')
else:
    print('\033[33m Vc foi aprovado, parabéns!')
