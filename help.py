from time import sleep  # importar biblioteca sleep de forma global, apenas o method sleep
c = ('\033[m',  # c(name the list, she the global, pode utilizar no programa inteiro) \033[m(0 sem cores)
    '\033[1;97;41m',  # 1 - red
    '\033[0;30;42m',  # 2 - green
    '\033[1;33;43m',  # 3 - yellow
    '\033[0;97;44m',  # 4 - blue
    '\033[1;36;45m',  # 5 - cyan
    '\033[7;97m',     # 6 - white
    );  # não precisa carregar biblioteca porquê trabalha com padrão ANSI de cores


# def(ajuda) principal, recebe o comando que vai executar
def ajuda(com):  # def(function) ajuda(name the function), recebe parâmetro com(comando), comando
    """
    -> Função ajuda
    :param com: recebe com(comando)
    :return: sem retorno
    """
    título(f'Acessando o manual do comando \'{com}\'', 4)
    # dentro da def(função) posso chamar outra def(função)
    # dentro de ajuda(def) estou chamando título(def)
    # '(entre aspas simples)' \(barra pra escapar ele), 4(cor)
    print(f'{c[6]}', end='')  # c(list the cor), 6(cor), end=''(fim)
    help(com)  # recebe help do com(comando), obs manual
    print(f'{c[0]}', end='')
    sleep(2)  # sleep(fazer uma pausa, aguardo) 2(segundos)


# método ou def título mostra o título personalizado
def título(mensagem, cor=0):  # def(function) título(name the function) com parâmetro mensagem(mostrar uma mensagem) and cor(opcional) 0(padrão)
    """
    -> Função personaliza título
    :param mensagem: recebe mensagem
    :param cor: cor selecionada
    :return: sem retorno
    """
    # mensagem do tamanho das linhas
    tamanho = len(mensagem) + 4  # tamanho vai ser len de mensagem + 4, isso é, 2 de cada lado
    print(f'{c[cor]}', end='')  # c(list the cor), cor(cor and 0), end=''(fim)
    print('~' * tamanho)  # vai exibir '~' the tamanho the mensagem
    print(f'  {mensagem}')  # exibi mensagem
    print('~' * tamanho)
    print(f'{c[0]}', end='')  # c(list the cor), 0(cor, limpar as cores), end=''(fim)
    sleep(1)  # sleep(fazer uma pausa, aguardo) 2(segundos)


# Programa Principal
comando = ''  # comando(variável) type string 'vazia'
while True:  # while(enquanto) true(verdadeiro) loop infinity
    título('SISTEMA DE AJUDA PyHELP', 2)  # título(function), exibe algo, 2(cor)
    comando =str(input("Função ou Biblioteca > "))  # comando(variável), str(explicitar que está lendo uma string), input(function leia)
    if comando.upper() == 'FIM':  # se comando upper(em todas as letras maiúculas) for igual a 'FIM'
        break  # stop the program
    else:  # senão
        ajuda(comando)  # ajuda(function) do comando(function), função ajuda
título('ATÉ LOGO!', 1)  # titulo(funciton), 1(cor)
