""" 
def add_10_days(day):
    day = day + 10
    return day

day = 20
month = 12
year = 2021

#year += 1
day2 = 19
month2 = 11
year2 = 2019

day = add_10_days(day)
print(day)
day2 = add_10_days(day2)
print(day2) """

class Date:
    day = 0
    month = 0
    year = 0

st = "Hello world"


""" class Person:
    #Atributos de persona
    name = "Paquita"
    surname = "Salas"
    gender = "F"
    age = 55
    #Estos de arriba son los valores que se asignan por defecto

    def walk(self):
    def talk(self):
    def sleep(self):
    def run(self): """

with open('/home/aso/Ficheros python/sinacceso.txt', 'r') as f:
    lista = f.readlines()
    for i in lista:
        lista.append(i)

class Person:
    def __init__(self,name,surname,gender,age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
    def get_age(self):
        return self.age
    ps = Person("Paquita", "Salas", "F", 55)
    edad_paquita = ps.get_age()
    print(edad_paquita)