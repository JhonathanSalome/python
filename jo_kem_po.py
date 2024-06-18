from random import randint  # import random, biblioteca random
from time import sleep  # biblioteca de sleep
itens = ('Pedra', 'Papel', 'Tesoura')  # itens(list)
computador = randint(0, 2)
# computador(variável) recebe randint entre 0 and 2, computador randomizar um
# print(f'O computador escolheu {itens[computador]}')#exibe o selecionado
print('''Suas Opções
[1]Pedra
[2]Papel
[3]Tesoura\n''')  # print formatado
jogador = int(input('Qual a sua jogada? '))
# jogador(variável), int(inteiro), input(entrada)
print()
print('-=-'*20)  # print formatado
print(f'Computador jogo {itens[computador]}')  # print formatado
print(f'Jogador jogou {itens[jogador]}')
print('-=-'*20)  # print formatado
print('JO')  # print
sleep(1)  # pausa program in 1(segundo)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-'*20)
print()  # pula row
if computador == 0:  # se computador(variável) jogo pedra
    if jogador == 0:  # se jogador(variável) igual a 0
        print('EMPATE')  # print formatado
    elif jogador == 1:  # senão jogador(variável) igual a 1
        print('JOGADOR VENCE')  # print formatado
    elif jogador == 2:  # senão jogador(variável) igual a 2
        print('COMPUTADOR VENCE')  # prinf formatado
    else:  # senão
        print('\nOpção inválida')  # print formatado
elif computador == 1:  # senão computador jogo papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\nOpção inválida')
elif computador == 2:  # senão computador jogo tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\nOpção inválida')
