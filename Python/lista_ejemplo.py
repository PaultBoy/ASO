lst=[1,2,3,4,5]
print(lst)
lst2=[]
print(lst2)
lst3=list()
print(lst3)
for item in lst:
    print(item)

#Comprobar si un elemento está en la lista. Devuelve booleano
3.14 in lst
#Comprobar si un elemento no está en la lista. Devuelve booleano
3.14 not in lst

len(lst)
lst.append(8.0)
print(lst)

type(lst[5])
type(lst[4])
lst.insert(4, "Un string")
lst[0] = lst[3]*3
lst[3]
print(lst)
lst.remove(lst[6])
lst.remove("Un string")
print(lst)
del lst[0]
print(lst)