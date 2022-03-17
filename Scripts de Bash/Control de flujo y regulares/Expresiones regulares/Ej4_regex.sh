#!/bin/bash

awk '{ if ($1 != "#"){
        if ($1 ~ /^[0-9]{4}[B-DF-HJ-NPR-TV-Z]{3}$/){
            print "Matrícula"; 
        }
        else if ($1 ~ /^[0-9]{8}[A-HJ-NP-TV-Z]{1}$/){
            print "DNI";
        }
        else if ($1 ~ /^[0-9]{9}$/){
            print "Número de teléfono";
        }
        else if ($1 ~ /^((([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))$/){
            print "IP";
        }

     } 
    }' Ej_validar_regex.txt
  