import math
import random
#print(math.sqrt(16))
#n=16
#res=math.sqrt(n)
#print(res)
#print(random.randint(10,40))

def main():
    num1=int(input("Introduce un número: "))
    num2=int(input("Introduce otro número: "))
    print(function_1(num1,num2))

def function_1(x,y):
    return x*y

main()