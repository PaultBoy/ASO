#!/bin/bash
read -p "Introduce un número por teclado: " num1
while [[ ! num1 =~ [0-9]+ ]]; do
    read -p "Introduce un NÚMERO por teclado: " num1
done
read -p "Introduce otro número por teclado: " num2
while [[ ! num2 =~ [0-9]+ ]]; do
    read -p "Introduce otro NÚMERO por teclado: " num2
done

if [[ $num1 == $num2 ]];then
    echo "$num1 es igual a $num2"
elif [[ $num1 < $num2 ]];then
    echo "$num1 es menor que $num2"
else
    echo "$num1 es mayor que $num2"
fi
