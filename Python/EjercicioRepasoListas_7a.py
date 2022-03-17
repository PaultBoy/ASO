numpersonas=int(input("Hola, ¿cuántos estáis en el aula?: "))
list=[]
string="Hola"
for i in range(numpersonas):
    nombre=input("¿Cómo te llamas?: ")
    list.append(nombre)
for j in range(len(list)):
    string= string +", " +list[j]
print(string)