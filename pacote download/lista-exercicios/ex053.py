frase = str(input('Digite uma frase e confira se ela é um  palíndromo:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
último = len(junto) - 1
inverso = ''
#inverso = [::-1] SOLUÇÃO SEM O FOR!
#print('A frase {} junta é {} e tem {} letras.'.format(lista, junto, último))
for c in range(último, -1, -1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('A frase {} é palindromo ficando\n = {}'.format(frase, inverso))
else:
    print('A frase {} não é palíndromo.\nDetrás para frente fica:  {}'.format(frase, inverso))