from msg_inicial import msg_inicial
from escala import seletor_de_escala
from conversor import conversor
from exibe_resultado import exibe_resultado

#Mensagem inicial
msg_inicial()

#Escolhe escala
escala = seletor_de_escala()

#Converte os graus para a escala escolhida
resultado = conversor(escala)

#Exibe resultado da conversão
exibe_resultado(resultado)