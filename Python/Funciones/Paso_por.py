#Paso por valor
#def double(num):
#	num = num * 2
#n = 10
#double(n)
#print(n) #n=10
#Paso por referencia
#def double(num):
#	num=num*2
#	return num
#n = 10
#n = double(n)
#print(n) #n=20

#Ejemplo 2 paso por referencia
#Viene a probar que las listas siempre se pasan por referencia
#def double(numbers):
#    for num in range(0,len(numbers)):
#        numbers[num] *= 2
#nums = [10, 20, 50]
#double(nums)
#print(nums)
#Las variables normales no se pasan normalmente por referencia
#num=15
#def doub(num1):
#    num1=num1*2

#doub(num)
#print(num)

def multiply(x, y):
    return x*y
a = 3
b = 5
res=multiply(a,b)
#print(res)
print(multiply(a,b))

def sumar(c, z):
    pass
def restar(o, p):
    pass