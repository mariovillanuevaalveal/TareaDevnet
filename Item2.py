from math import *
def calculo(radio):
    radioCiunferencia = radio * pi
    return radioCiunferencia

loop=True
print ("Este programa calcula el radio de una circunferencia")
print ("Para salir Escriba 'q' o 'Q'")

try:
    while loop :
        radio = float(input("Ingrese el radio de la circunferencia: "))
        print("El radio de la circunferencia es : {0:.6f}".format(calculo(radio)))
        respuesta = input("Desea otra operación : ")
        if respuesta=="q" or respuesta=="Q":
            loop=False
        else:
            loop= True
except:
        print("Hubo un error al ingresar datos.\n Programa Terminado")
