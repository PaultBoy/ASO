try:
    resultado = 2/0
    print(resultado)
except ZeroDivisionError:
    print("Esta operación es imposible de realizar")