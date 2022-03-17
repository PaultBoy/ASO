Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> 
>>> print("Please, Hello World")
Please, Hello World
>>> 
>>> dir
<built-in function dir>
>>> ls
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> print "Hello World"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?
>>> i = 0
>>> print(i)
0
>>> i = 8
>>> type(i)
<class 'int'>
>>> i =8.5
>>> type(i)
<class 'float'>
>>> float i = 1
SyntaxError: invalid syntax
>>> i="Ahora esto es un string"
>>> type(i)
<class 'str'>
>>> i=True
>>> type(i)
<class 'bool'>
>>> input("Introduce lo que quieras:")
Introduce lo que quieras:hola
'hola'
>>> var = input("Introduce lo que quieras: ")
Introduce lo que quieras: hola
>>> print(var)
hola
>>> type(var)
<class 'str'>
>>> var=int(var)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    var=int(var)
ValueError: invalid literal for int() with base 10: 'hola'
>>> var = input("Introduce lo que quieras: ")
Introduce lo que quieras: 4
>>> var=int(var)
>>> type(var)
<class 'int'>
>>> var
4
>>> var=int(input("Introduce lo que quieras: "))
Introduce lo que quieras: 5
>>> type(var)
<class 'int'>
>>> print(type(var))
<class 'int'>
>>> print(var)
5
>>> a = 3
>>> print(a)
3
>>> print("El valor de una variable ",a," entre strings")
El valor de una variable  3  entre strings
>>> a=True
>>> print("El valor de una variable a ",a," entre strings")
El valor de una variable a  True  entre strings
>>> type(a)
<class 'bool'>
>>> 12/5
2.4
>>> 12//5
2
>>> 12%5
2
>>> 13%5
3
>>> i=6
>>> i=i+i
>>> i
12
>>> i=6
>>> i=i+1
>>> i
7
>>> i+=1
>>> print(i)
8
>>> print(3==3)
True
>>> 3!=2
True
>>> 1==2 and 3==4
False
>>> 1==2 or 3==4
False
>>> 1==1 or 3==4
True
>>> print(3+4)
