from random import choice
from funçoes import *
from time import sleep


jogadas = ['pedra', 'papel', 'tesoura']

nome_jogador = input('Digite seu nome: ')
while True:
    iniciar()
    jogada_jogador = escolher_jogada(nome_jogador)
    jogada_bot = choice(jogadas)

    if jogada_jogador == '4' or jogada_jogador == 'finalizar':
        print(f'{cores.vermelho}Encerrando o jogo...{cores.fim}')
        input(f'{cores.amarelo}Aperte qualquer tecla para continuar...{cores.fim}')
        exit()
    elif jogada_jogador in jogadas:
        resultado_do_jogo = mecanica_jogo(jogada_jogador, jogada_bot)
        print(f'{cores.ciano}JO...')
        sleep(1)
        print('KEN..')
        sleep(1)
        print(f'PÔ..{cores.fim}')
        sleep(1)
        print(f'{resultado_do_jogo} - bot escolheu: {jogada_bot}, {nome_jogador} escolheu: {jogada_jogador}')
        input(f'{cores.amarelo}Aperte qualquer tecla para continuar...{cores.fim}')
    else:
        print(f'{cores.amarelo}Resposta invalida, reiniciando o jogo{cores.fim}')
        sleep(2)
