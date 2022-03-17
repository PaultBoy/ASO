#!/bin/bash
num1=0
num2=0
read -p "Introduce un número: " num1
read -p "Introduce otro número: " num2

if [[ $num1 == $num2 ]]; then
    echo "$num1 y $num2 son iguales"
else
    if [[ $num1 < $num2 ]]; then
    echo "$num2 es mayor que $num1"
    else
        echo "$num1 es mayor que $num2"
    fi
fi