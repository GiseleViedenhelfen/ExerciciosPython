peso = float(input('Quantos kg vc pesa? kg:'))
alt = float(input('Qual a sua altura? em metros. ex:1.60'))
imc = peso / (alt **2)
if imc < 18.5:
    print('Seu IMC é {:.1f} e corresponde à magra'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e corresponde a normal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}, vc está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f} e indica obesidade '.format(imc))
else:
    print('Seu IMC é {:.1f} e indica obesidade mórbida'.format(imc))
