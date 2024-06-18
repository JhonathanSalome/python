x = int(input('Digite um número inteiro: '))  # x(variável), int(inteiro), input(entrada)
print('''\nRscolha uma das bases para a conversão

[1] converter BINÁRIO
[2] converter OCTAL
[3] converter HEXADECIMAL''')

y = int(input('\nSua opção: '))  # y(variável), int(inteiro), input(entrada)
print()  # pula row
if y == 1:  # se y(variável) for igual a 1
    print(f'{x} convertido para BINÁRIO é {bin(x)}')  # print formatado
elif y == 2:
    print(f'{x} convertido para OCTAL é {oct(x)}')
elif y == 3:
    print(f'{x} convertido para HEXADECIMAL é {hex(x)}')
else:  # senão
    print('Opção inválida! Tente novamente')

print('\nFim do programa!\n')

