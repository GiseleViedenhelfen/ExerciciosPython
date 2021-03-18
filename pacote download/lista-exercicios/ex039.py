from datetime import date
nasc = int(input('Em que ano vc nasceu?'))
sexo = str(input('Vc é homem ou mulher?')).strip().lower()
ano = date.today().year #ano atual da máquina
idade = ano - nasc
if sexo == 'homem' and idade == 18:
    print('Esse ano vc precisa se alistar no serviço militar...')
elif sexo == 'homem' and idade > 18:
    saldo1 = idade - 18 #descobrir quantos anos a mais de 18
    ali1 = ano - saldo1 #descobrir qual ano deveria ter se alistado
    print('Vc já deveria ter se alistado há {} ano(s).'.format(saldo1))
    print('Seu alistamento foi no ano {}.'.format(ali1))
elif sexo == 'homem' and idade < 18:
    saldo2 = 18 - idade #descobrir quantos anos a menos de 18
    ali2 = ano + saldo2 #descobrir qual ano deverá se alistar
    print('Ainda faltam {} ano(s) para o seu alistamento obrigatório.'.format(saldo2))
    print('Seu alistamento será no ano {}'.format(ali2))
else:
    print('Vc não precisa se alistar!')
