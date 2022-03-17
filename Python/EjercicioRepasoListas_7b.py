numpersonas=int(input("Hola, ¿cuántos estáis en el aula?: "))
list=[]
string="Hola, "
for i in range(numpersonas):
    nombre=input("¿Cómo te llamas?: ")
    list.append(nombre)
string= string+ ", ".join(list)
print(string)