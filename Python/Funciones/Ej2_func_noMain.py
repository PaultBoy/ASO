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

listVacPar= [] #list()
listVacImpar= [] #list()
listInteger = [2,-1,7,6,5]
clasifica_num(listInteger,listVacPar,listVacImpar)
