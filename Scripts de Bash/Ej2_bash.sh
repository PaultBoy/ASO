#!/bin/bash

par1=$1
par2=$2

if [[ ${#par1} == 0 || ${#par2} == 0 ]]; then
    echo "Error. No se han introducido parámetros correctamente"
    exit 1
else
    if [[ $par1 == $par2 ]]; then
        echo "Ambos strings son iguales"
    else
        echo "Cada string es diferente"
    fi
fi

exit 0