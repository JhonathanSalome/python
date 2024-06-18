time = list()  # time(name list)
jogador = dict()  # jogador dicionário
partidas = list()  # partidas the list

while True:  # while(enquanto), true(verdadeiro), loop infinity
    jogador.clear()
    # apagar jogador antes de ler os dados dele, para poder limpar porque a cada laço vai ler os dados de um mesmo jogador
    jogador['nome'] = str(input('\033[1;31mNome do jogador: \033[m'))  # name vai recebe o que viem do teclado, str(string)
    tot = int(input(f'Quantas partidas \033[1;31m{jogador["nome"]}\033[m jogou? '))  # tot(variável), int(inteiro)
    partidas.clear()  # esvaziar antes de ler

    # ler quantos gols ele fez em cada uma das partidas
    # contador para ler a quantidade das partidas
    for contador in range(0, tot):  # para cada contador in(em) range(alcance) entre 0 até total
        partidas.append(int(input(f'    \033[1;32mQuantos gols na partida {contador + 1}º? \033[m')))
        ''' dar um append na lista da partidas, append(para adicionar um item), esse item vai ser o gols que foi feito em cada partida '''
    jogador['gols'] = partidas[:]
    # jogador['gols'(name da chave)] recebe uma cópia[:] de partidas(list), isso é,
    # fazer com que a list vai pra dentro do dict
    jogador['total'] = sum(partidas)  # jogador['total'(name the chave)] recebe sum(soma), do que ta em partida(list)
    time.append(jogador.copy()) # jogar o jogador dentro do time
    # cópia do jogador, dentro do time, .copy(cópia) porquê é um dicionário

    while True:  # loop infinity
        resp = str(input('\033[1;33mQuer continuar? [S/N] \033[m')).upper()[0]
        ''' resp(variável) =, str(string), input(entrada), upper(maiúscula), [0](apenas um caracter) '''
        if resp in 'NS':  # se resp in(em) 'SN'
            break  # stop
        print('\033[1;31mERRO! Responda apenas S ou N.\033[m')
    if resp in 'N':  # se resp in(em) 'N'
        break  # stop the program
print('\033[1;46m-=\033[m' * 25)

# cabeçalho, # resultados
print('\033[1;36mcod \033[m', end='')
for elemento in jogador.keys():  # para cada elemento in(em) jogador(list).keys(chaves)
    print(f'\033[1;31m{elemento:<15}\033[m', end='')  # exibe algo formatado
print()
print('\033[1;46m-=\033[m' * 25)

# fazer tabela
for keys, values in enumerate(time):  # para cada keys(chaves), values(valores) in(em) enumerate(time)
    print(f'\033[1;35m{keys:>3} \033[m', end='')  # exibe algo formatado
    for dado in values.values():  # para cada d(dado) in(em) values.values
        print(f'\033[1;33m{str(dado):<15}\033[m', end='')  # str(string) do dado, end=''(fim)
    print()

while True:  # loop infinity
    busca = int(input('\033[1;38mMostra dado de qual jogador? (999 para parar) \033[m'))
    print('\033[1;46m=\033[m' * 42)
    # chave de busca(busca), int(inteiro), input(entrada)
    if busca == 999:  # fleg, se busca for igual a 999
        break  # stop the program
    if busca >= len(time):  # se busca for maior and igual que, len(tamanho) do time(list)
        print(f'\033[1;31mERRO! Não existe jogador com código {busca}!\033[m')
    else:  # senão
        print(f' \033[1;33m-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:\033[m')
        ''' nome do jogador está dentro de time(list), o time tem um índice numérico da busca
        e dentro dele eu tenho outro elemento que é o nome, está dentro do dicionário '''
        for índice, gols in enumerate(time[busca]['gols']):
            ''' para cada índice, gols in(em) enumerate de time da busca, do campo gols
            quantidade de gols em cada partida '''
            print(f'    \033[1;92mNo jogo {índice} fez {gols} gols.\033[m')  # print formatado
    print('\033[1;46m=\033[m' * 42)
print('\033[1;38m <<VOLTE SEMPRE!>> \033[m')
