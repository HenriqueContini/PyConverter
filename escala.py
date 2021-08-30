def seletor_de_escala():
    print('O que deseja fazer?')
    print('Digite 1 para converter de graus Celsius para Fahrenheit.')
    print('Digite 2 para converter de graus Fahrenheit para Celsius.')
    escala = int(input('\nDigite o número da conversão que deseja fazer: '))

    if(escala == 1 or escala == 2):
        return escala
    else:
        print('Opção inválida!\n')
        seletor_de_escala()