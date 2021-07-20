def ficha(jogador='<desconhecido>', gol=0):
    if jogador == '':
        return f'o jogador <desconhecido> fez {gol} gol(s)'
    if gol == '':
        return f'o jogador {jogador} fez 0 gol(s)'
    if jogador == '' and gol == '':
        return f'o jogador <desconhecido> fez 0 gol(s)'
    else:
        return f'o jogador {jogador} fez {gol} gol(s)'

jogador = str(input('nome do jogador: '))
gol = str(input('Quantos gols fez(em números): '))
print(ficha(jogador, gol))
