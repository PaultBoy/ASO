def clasifica_num(listInt, listPar, listImpar):
    #Ordeno la lista principal desde el principio
    listInt.sort()
    for i in listInt:
        if i%2 == 0:
            listPar.append(i)
        else:
            listImpar.append(i)
    print("Lista de pares: ",listPar)
    print("Lista de impares: ",listImpar)

def main():
    try:
        listVacPar= [] #list()
        listVacImpar= [] #list()
        listInteger = ["b",-1,7,6,5]
        clasifica_num(listInteger,listVacPar,listVacImpar)
    except TypeError:
        print("La lista sólo debe contener números")
main()