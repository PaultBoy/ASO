import math
def triangulo(base, altura):
    return (base*altura)/2
def rectangulo(base, altura):
    return (base*altura)
def circunferencia(radio):
    return (math.pi*(radio**2))
def recoleccion_valores():
    try:
        opcion = int(input("Introduce la opción de área (1, 2 o 3): "))
        if opcion == 1:
            #Opción área del triángulo
            bass = float(input("Introduce la base del triángulo: "))
            alt = float(input("Introduce la altura del triángulo: "))
            print("Área: ",triangulo(bass, alt))
        elif opcion == 2:
            #Opción área del rectángulo
            bass = float(input("Introduce la base del rectángulo: "))
            alt = float(input("Introduce la altura del rectángulo: "))
            print("Área: ",rectangulo(bass, alt))
        elif opcion == 3:
            #Opción área de la circunferencia
            rad = float(input("Introduce el radio de la circunferencia: "))
            print("Área: ",circunferencia(rad))
        else:
            raise ValueError
    except ValueError:
        print ("Error de introducción de opciones.")
        exit()
def main():
    recoleccion_valores()
    exit()

main()