#!/bin/bash

if [[ $(whoami) == "root" ]];then
    echo "No ejecutes el script como superusuario"
    exit 1
elif [[ $# != 1 ]];then
    echo "Número de parámetros excesivo"
    exit 2
else
    case $1 in
        "-d")
            echo $(df -h)
            exit 0
            ;;
        "--disk")
            echo $(df -h)
            exit 0
            ;;
        "-m")
            echo $(free -h)
            exit 0
            ;;
        "--mem")
            echo $(free -h)
            exit 0
            ;;
        "--host")
            echo $(hostname)
            exit 0
            ;;
        "-h")
            echo $(hostname)
            exit 0
            ;;
        "-t")
            echo $(uptime | cut -f 4,5 -d " ")
            exit 0
            ;;
        "--time")
            echo $(uptime | cut -f 4,5 -d " ")
            exit 0
            ;;
        "--users")
            echo $(w | cut -f 4,5 -d " ")
            exit 0
            ;;
        "-u")
            echo $(w | cut -f 4,5 -d " ")
            exit 0
            ;;
        *)
            echo "Opción inválida"
            exit 3
            ;;
    esac
fi
