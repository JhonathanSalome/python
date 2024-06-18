def leiaInt(mensagem):  # leiaInt(def, function), recebe o parâmetro mensagem
    while True:  # while(enquanto) true(verdadeiro), loop infity, enquanto não digitar o número certo
        try:  # tente fazer isso(se não der problema)
            n = int(input(mensagem))
            # n(variável), int(inteiro), input(entrada), recebe mensagem
        except (ValueError, TypeError):
            # se der algum problema, mais de 1 erro(valor ou tipo) pode colocar em ()
            # ValueError(erro the value), TypeError(erro the type)
            print('\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')  # print formatado
            continue
            # continue(joga direto por while denovo, ele vai tentar mais uma vez, vai fica dando erro)
        except (KeyboardInterrupt):
            # se der algum problema, mais de 1 erro
            # KeyboardInterrupt(erro de digitação)
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')  # print formatado
            return 0  # retorna 0, valor padrão
        else:  # senão
            return n  # retorna n


def linha(tamanho=42):  # def(função) linha recebe parâmetro tamanho, 42(padrão)
    return '\033[1;40m-\033[m' * tamanho  # retorna '-' * tamanho


def cabeçalho(texto):  # def(function) cabeçalho recebe texto(parâmetro), essa def cabeçalho vai usa a def linha
    print(linha())  # print linha(function)
    print(texto.center(42))
    # print no texto, center(centralizar) em 42 caracteres
    print(linha())


def menu(lista):  # função def menu, parâmetro lista(vetor, list)
    cabeçalho(f'\033[1;96mMENU PRINCIPAL\033[m')  # chama cabeçalho(def)
    # print(lista)
    contador = 1  # contador começa com 1
    for item in lista:  # para cada item in(em) da lista
        print(f'\033[1;93m{contador}\033[m \033[1;96m-\033[m \033[1;93m{item}\033[m')
        # print formatado
        contador += 1  # contador recebe contador + 1, soma + 1
    print(linha())  # print linha(def, function)
    opc = leiaInt('\033[1;93mSua Opção: \033[m')
    # opção(variável) recebe leiaInt(function para ler um número inteiro)
    return opc  # retorna opc
