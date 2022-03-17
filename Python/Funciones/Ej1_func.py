import math
def triangulo(base, altura):
    return (base*altura)/2
def rectangulo(base, altura):
    return (base*altura)
def circunferencia(radio):
    return (math.pi*(radio**2))
def recoleccion_valores():
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
    else:
        #Opción área de la circunferencia
        rad = float(input("Introduce el radio de la circunferencia: "))
        print("Área: ",circunferencia(rad))
    #else:
        #Cualquier número que no se corresponda con 1, 2, 3
        #print("Opción incorrecta")

def main():
    recoleccion_valores()
    exit()

main()