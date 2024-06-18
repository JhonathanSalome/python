import ex115.lib.interface
from ex115.lib.interface import *
from ex115.lib.arquivo import *
# importa do ex115 a lib(name the pasta), interface(name the pasta), *(importa tudo)
from time import sleep
# importa biblioteca sleep

arq = 'cadastro.txt'  # arq(variável) recebe cadastro.txt(name the file)
# verificar se determinado arquivo existe

if not arquivoExiste(arq):  # se não arquivoExiste, parâmetro arq
    # então só vai criar arquivo, se arquivo não existe
    criarArquivo(arq)  # chama o criarArquivo(def), nome do arquivo é arq

# if arquivoExiste(arq):  # se arqExiste, passando o arq
    # antes de mostra o menu, verificar se o aquivo existe
    # print('\033[0;33mArquivo encontrado com sucesso!\033[m')
    # print formatado
# else:  # senão, o arquivo não existe
    # print('\033[0;31mArquivo não encontrado!\033[m')

while True:  # while(enquanto) true(verdadeiro), loop infinity
    # resposta recebe menu saber a resposta dessa pessoa,
    # chama menu é passa uma lista pra dentro dele
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    # resposta(variável) recebe menu(def) que está dentro de uma interface
    if resposta == 1:  # se resposta for igual 1
        # opção listar o conteúdo de um arquivo
        lerArquivo(arq)  # chama lerArquivo(def), recebe arq(parâmetro)
    elif resposta == 2:  # se não resposta for igual a 2
        #  opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')  # chama cabeçalho
        nome = str(input('Nome: '))
        # nome(variável) recebe str(string), input(entrada)
        idade = leiaInt('Idade: ')
        # idade(variável) recebe leiaInt(def, vai ler uma idade como número inteiro)
        rg = leiaInt('RG: ')
        cpf = leiaInt('CPF: ')
        cadastro(arq, nome, idade, rg, cpf)
        ''' passa arq, nome and idade para cadastro(def)
        passa os parâmetro nome do arquivo é arq, nome e idade que vai cadastar '''
    elif resposta == 3:  # se não resposta for igual a 3
        cabeçalho('Saindo do sistema... Até logo!')  # cabeçalho(def)
        break  # stop the program
    else:  # senão
        print('\033[31mERRO! Digite uma opção válida!\033[m')  # print formatado
    sleep(1.5)  # dormi em 1.5 segundos
