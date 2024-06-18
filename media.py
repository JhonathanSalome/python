ficha = list()  # ficha(é uma list) para cada aluno, lista composta, com 3 lista dentro
while True:  # while(enquanto), true(verdadeiro), loop infinity
    nome = str(input('\033[1;94mNome: '))  # nome(variável), str(explicitar que é string), input(entrada)
    nota1 = float(input('Primeia nota: '))  # nota1(variável), float(flutuante), input(entrada)
    nota2 = float(input('Segunda nota: \033[m'))
    média = (nota1+nota2)/2  # média(variável) recebe nota1 mais nota dividido por 2
    ficha.append([nome, [nota1, nota2], média])  # da append na list ficha([nome, [nota1, nota2], média]), list composta
    '''resp = str(input('Quer continuar? ))  # resp(variável) str(string)
    if resp == 'Nn':  # se resp for igual a Nn
        break'''  # stop the program
    resp = ' '  # resp string vazia
    while resp not in 'SN':  # while(enquanto) resp(variável) not(não) in(em) 'SN'
        resp = str(input('\033[1;93mQuer continuar? [S/N] \033[m')).strip().upper()[0]  # resp(variável), str(explicitar que é string), input(entrada)
        print('\033[1;91mDigite apenas S ou N \033[m')
    if resp == 'N':  # se rep(variável) ==(igual) N
        break  # stop the program
print('\033[1;40m-=\033[m'*13)  # exibe algo with formatação the cor
print(f'\033[1;91m{"No.":<4}\033[m\033[1;92m{"NOME":<10}{"MÉDIA":>8}\033[m')  # string formatada
# No.(número) 4(caracteres, formatado a left), NOME(with 10 a left), MÈDIA(with 8 a right)
print('\033[1;40m-\033[m'*26)  # exibe algo with formatação the cor
# mosta os dados
for índice, aluno in enumerate(ficha):  # para cada índice and aluno in(em) enumerate(ficha)
    print(f'\033[1;91m{índice:<4}\033[m\033[1;96m{aluno[0]:<10}{aluno[2]:>8.1f}\033[m')  # exibe algo with formatação
while True:  # while(enquanto) true(verdade), loop infinity
    print('\033[1;40m-\033[m'*26)
    opção = int(input('\033[1;33mMostra notas de qual aluno? (999 interrompe):\033[m '))  # opção(variável), int(inteiro), input(entrada)
    if opção == 999:  # se opção for igual 999
        print(f'\n\033[1;101mFINALIZANDO\033[m\n')
        break  # stop the program
    if opção <= len(ficha) - 1:
        ''' se opção for menor ou igual ao len de ficha menos 1, isso é, cadastrei o aluno 0, 1, 2, ele vai ser 0, 1 ou 2, não pode ser 3, 4, 5
            então, ele precisa ser menor que len ficha(quantidade de alunos cadastrados), - 1, porque o primeiro aluno é 0, o último é n - 1 '''
        print(f'\033[1;92mNotas de {ficha[opção][0]} são {ficha[opção][1]}\033[m')
        ''' ficha(variável composta ter três níveis de composição), opção(é o número do aluno), [0](é nome dele), [1](são as notas dele) '''
print('\033[1;101m<<< VOLTE SEMPRE >>>\033[m')  # exibe algo with formatação the cor
