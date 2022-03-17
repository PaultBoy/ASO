#!/bin/bash
if [[ $# == 3 ]];then
    (cat $3 | cut -f $1 -d "$2") >> $HOME/mycutout.txt
    exit 0
else
    echo "Parámetros no correctos"
    exit 1