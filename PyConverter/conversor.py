def conversor(escala):
    if(escala == 1):
        numero = int(input('\nDigite a temperatura que deseja converter de Celsius para Fahrenheit: '))
        return (numero * 9/5) + 32
        #Celsius para Fahrenheit.
    else:
        numero = int(input('\nDigite a temperatura que deseja converter de Fahrenheit para Celsius: '))
        return (numero - 32) * 5/9
        #Fahrenheit para Celsius.