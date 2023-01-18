import os


def escolher_jogada(nome_jogador):
    jogada_jogador = input(
        f'{nome_jogador} - Escolha sua jogada: ').strip().lower()
    if jogada_jogador == '1':
        jogada_jogador = 'pedra'
    elif jogada_jogador == '2':
        jogada_jogador = 'papel'
    elif jogada_jogador == '3':
        jogada_jogador = 'tesoura'
    return jogada_jogador


def iniciar():
    os.system('cls')
    print('-' * 30)
    print(f'\t{cores.ciano}JOKENPÔ{cores.fim}')
    print('-' * 30)
    print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n[4] - Finalizar')


def mecanica_jogo(jogada_jogador, jogada_bot):
    if jogada_jogador == jogada_bot:
        return (f'{cores.amarelo}EMPATOU!{cores.fim}')
    elif (
            (jogada_jogador == 'pedra' and jogada_bot == 'tesoura') or
            (jogada_jogador == 'papel' and jogada_bot == 'pedra') or
            (jogada_jogador == 'tesoura' and jogada_bot == 'papel')):
        return (f'{cores.verde}GANHOU!{cores.fim}')
    elif (
            (jogada_jogador == 'pedra' and jogada_bot == 'papel') or
            (jogada_jogador == 'papel' and jogada_bot == 'tesoura') or
            (jogada_jogador == 'tesoura' and jogada_bot == 'pedra')):
        return (f'{cores.vermelho}PERDEU!{cores.fim}')


#### cores ####
class cores:
    ciano = '\033[1;36m'
    amarelo = '\033[1;33m'
    fim = '\033[0m'
    verde = '\033[92m'
    vermelho = '\033[91m'
