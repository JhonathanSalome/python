cores = {'pretofundo': '\033[1;40m',
         'vermelhoclarofonte': '\033[1;91m',
         'amareloclarofonte': '\033[1;93m',
         'cyanfonte': '\033[1;36m',
         'cyanclarofonte': '\033[1;96m', 'fim': '\033[m'
         }  # cores(name the dicionário)


print(f'{cores["pretofundo"]}-=-{cores["fim"]}'*12)  # cores(dicionário)[name the cor]
print('{:^41}'.format(' \033[1;96mPROGRAMA CALCULADORA\033[m ')) # {41 len the exibição}, format(método formata o especificado)
print(f'{cores["pretofundo"]}-=-{cores["fim"]}'*12)
while True:  #whil(enquanto) true(veerdadeiro), loop infinity
    a = float(input(f'{cores["vermelhoclarofonte"]}Informe 1 número: {cores["fim"]}'))  # a(variável), float(flutuante), input(entrada), cores(dicionário), [name the cor]
    b = float(input(f'{cores["vermelhoclarofonte"]}Informe 2 número: {cores["fim"]}'))
    print(f'''\n{cores["pretofundo"]}Escolha uma opção...{cores["fim"]}{cores["amareloclarofonte"]}\n
[1]Soma
[2]Subtração
[3]Multiplicação
[4]Divisão
[5]Divisão inteira
[6]Raiz quadrada
[7]Raiz ao cubo
[8]Exponenciação
[9]!Fatorial
[10]PA Progressão Aritmédica
[11]Programa Média
[12]^
[13]Tabuada
[14]Maior
[15]Menor
[16]Igual
[17]Diferente
[18]Sair, Fim do programa!{cores["fim"]}
''')
    op = int(input(f'{cores["cyanfonte"]}Digite sua escolha: '))  # op(variável), int(inteiro), input(entrada), cores(dicionário), [name the cor]
    print()  # pular row
    print(f'{cores["pretofundo"]}-=-{cores["fim"]}'*15)
    print()
    if op == 1:
        print(f'{a} + {b} = {a+b}\n')
    #soma

    elif op == 2:
        print(f'{a} - {b} = {a-b}\n')
    #subtração

    elif op == 3:
        print(f'{a} * {b} = {a*b}\n')
    #multiplição

    elif op == 4:
        print(f'{a} / {b} = {a/b}\n')
    #divisão

    elif op == 5:
        print(f'{a} // {b} = {a//b}\n')
    #divisão inteira

    elif op == 6:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digite novamente\n')
        a = float(input(f'Informe 1 número: {cores["fim"]}'))
        print(f'\nRaiz quadrada de {a} é {a**(1/2)}\n')
    #raiz quadrada

    elif op == 7:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digite novamente\n')
        a = float(input(f'Informe 1 número: {cores["fim"]}'))
        print(f'\nRaiz cubica de {a} é {a**(1/3)}\n')
    #raiz cubica

    elif op == 8:
        print(f'{a} ** {b} = {a**b}\n')
    #exponenciação

    elif op == 9:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digital navamente\t{cores["fim"]}')
        a = int(input(f'\n{cores["amareloclarofonte"]}Informe 1 número: {cores["fim"]}'))
        c = 0
        f = 1
        for c in range(1, a):
            f *= a
            a -= 1
        print(f'fatorial é {f}')
        print()
    #fatorial

    elif op == 10:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digite novamente\n')
        a = int(input('Primeiro termo: '))
        b = int(input('Razão: '))
        c = int(input(f'ir até aonde: {cores["fim"]}'))
        decimo = a+(c-1)*b
        print()
        #print('-=-'*20)
        for c in range(a, decimo+b, b):
            print(f'{c}', end=' -> ')
        print('Acabou\n')
     #PA progressão aritmédica
     
    elif op == 11:
         print(f'Nota 1: {a} + Nota 2: {b} = {(a+b)/2}\n')
    #média
    
    elif op == 12:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digite novamente\n')
        a = int(input('Informe 1 número: '))
        b = int(input(f'\nInforme 2 número: {cores["fim"]}'))
        print(f'\n{a} ^ {b} = {a^b}\n')
    #^
    
    elif op == 13:
        print(f'{cores["vermelhoclarofonte"]}Erro{cores["fim"]}\n{cores["amareloclarofonte"]}Digite novamente\n')
        a = int(input('Valor da tabuada: '))
        b = int(input(f'Quantidades de vezes da tabuada: {cores["fim"]}'))
        print()
        for c in range(0, b+1):
            print(f'{a:1} x {c} = {a*c}')
        print()
    #tabuada

    elif op == 14:
        if a > b:
            print(f'{a} Maior que {b}\n')
        elif a < b:
            print(f'{a} Menor que {b}\n')
        elif a == b:
            print(f'{a} e {b}, são números iguais\n')
    #maior

    elif op == 15:
        if a < b:
            print(f'{a} Menor que {b}\n')
        elif a>b:
            print(f'{a} Maior que {b}\n')
        elif a == b:
            print(f'{a} e {b}, são números iguais\n')
    #menor

    elif op == 16:
        if a == b:
            print(f'{a} e {b}, são iguais\n')
        elif a != b:
            print(f'{a} e diferente de {b}\n')
    #igual
    
    elif op == 17:
        if a != b:
            print(f'{a} e diferente de {b}\n')
        elif a == b:
            print(f'{a} e igual a {b}\n')
    #diferente
    elif op == 18:
        print('{:^47}'.format(f' {cores["vermelhoclarofonte"]}Fim do Programa!{cores["fim"]} '))
        print()
        print(f'{cores["pretofundo"]}-=-{cores["fim"]}'*15)
        break
    #break
    print(f'{cores["pretofundo"]}-=-{cores["fim"]}'*15)