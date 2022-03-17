#Preguntar cuántas personas hay en el aula, a cada una preguntar su nombre y saludarles a cada uno.

numPers=input("Hola, ¿cuántos estáis en el aula?: ")
nombres=[]
while not numPers.isnumeric():
    numPers=input("Hola, ¿cuántos estáis en el aula?: ")
else:
    numPers = int(numPers)
    for i in range(numPers):
        nombre=input("¿Cómo te llamas?: ")
        nombres.append(nombre)
    print("Hola,", nombres)