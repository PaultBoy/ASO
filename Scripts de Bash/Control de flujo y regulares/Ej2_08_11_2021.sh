#!/bin/bash
if [[ $# != 1 ]]; then
    echo "No se han introducido suficientes o demasiados parámetros"
    exit 2
fi
ping -c 1 $1
if [[ $? == 0 ]];then
    echo "El host $1 tiene conectividad"
    exit 0
else
    echo "El host $1 no contesta"
    exit 1
fi