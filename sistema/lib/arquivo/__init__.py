from ex115.lib.interface import *
# importa do ex115 a lib(name the pasta), interface(name the pasta), *(importa tudo)

# manipulação do file

# verifica se o file exite
def arquivoExiste(nome):
    '''def arquivoExiste(function) recebe parâmetro nome do arquivo,
    verifica e retorna True or False'''
    try:  # -> tratamento de error, tente fazer isso
        a = open(nome, 'rt')  # rt, ler arquivo de texto
        ''' tentar abrir o arquivo
        a recebe open(função open tentar abrir um arquivo),
        passando parâmetro nome do arquivo que é nome,
        vou tentar abrir para leitura de arquivo texto,
        rt(reading e text), rt(tentar open arquivo em modo texto) '''
        a.close()  # fecha a(variável)
    except FileNotFoundError:
        # except, qualquer problema que der
        # FileNotFoundError, se o arquivo não foi encontrado, umas das exceções
        return False  # retorna falso
    else:  # senão
        return True  # retorna True


# create um file new
def criarArquivo(nome):
    # def(function) criarArquivo(name the def)
    # recebe parâmetro nome do arquivo
    try:  # testar
        a = open(nome, 'wt+')
        ''' a(variável) vai ser open(abrir), manda criar nome do arquivo
        wt(escrever um arquivo de text, gravação de arquivo texto)
        +(é, se o arquivo não existi ele cria, cria arquivo caso não exista) '''
        a.close()  # fechar a
    except:  # se der algum erro
        print('\033[1;31mHouve um erro na criação do arquivo!\033[m')  # print formatado
    else:  # senão
        print(f'\033[33mArquivo {nome} criado com sucesso!\033[m')


# ler file
def lerArquivo(nome):
    # lerArquivo(def, função), recebe parâmetro nome do arquivo
    try:  # tratamento de exceção, tenta fazer
        a = open(nome, 'rt')
        ''' a(variável) recebe tenta open(abrir) o arquivo,
        ler o conteúdo do arquivo, name the file como,
        rt(leitura de arquivo texto) '''
    except:  # se der algum problema
        print('\033[31mErro ao ler o arquivo!\033[m')  # print formatado
    else:  # se não, se deu tudo certo, se open no file(arquivo)
        print('\033[33m\033[m')  # print formatado
        cabeçalho('PESSOAS CADASTRADAS')  # cabeçalho(def)
        for linha in a:  # para cada linha in(em) dentro a(arquivo)
            dado = linha.split(';')
            ''' dado vai ser linha split(dividir os dados, separar por ;)
            e dado vai ser uma lista '''
            dado[3] = dado[3].replace('\n', '')
            ''' dado 1, idade, receba dado 1 tirando '\n'
            replace, substituir '\n' por '' nada '''
            print(f'Nome {dado[0]:<10} idade {dado[1]} anos rg {dado[2]} cpf {dado[3]}')
            # print formatado
        # print(a.read())  # read(ler tudo) ou(or) readlines, de a(variável)
        # readlines, pega as linhas do arquivo e joga dentro de uma lista
    finally:  # finalmente, dando certo ou errado fecha o file
        a.close()  # a(variável) close(fechar)


def cadastro(arq, nome='desconhecido', idade=0, rg=000000000, cpf=00000000000):
    ''' cadastro(def, function)
    recebe os parâmetro nome do arquivo é arq,
    nome(padrao=desconhecido) da pessoa, idade(padrão=0) and
    rg padrão 000000000, cpf padrão 00000000000,
    parâmetro padrão caso chama function de forma errada '''
    try:  # tentar open o arquivo
        a = open(arq, 'at')
        ''' a(variável) recebe open(abrir)
        o nome do meu arquivo é arq,
        vou tentar abrir ele pra colocar mais dados
        at(append, colocar coisas dentro do arquivo,
        arquivo de texto), que é arq '''
    except:  # se der algum erro, mostra na tela
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
        # print formatado
    else:  # senão, se deu tudo certo
        try:  # tentar, erro no arquivo
            a.write(f'{nome};{idade};{rg};{cpf}\n')
            # write(escreve) dentro do a(file)
        except:  # se der um erro
            print('\033[31mHouve um ERRO na hora de escrever os dados!\033[m')
            # print formatado
        else:  # senão
            print(f'Novo registro de {nome} adicionado.')
            a.close()  # a(variável) close(fechar)
