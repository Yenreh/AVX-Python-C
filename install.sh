#!/bin/bash
echo "Instalando dependencias"
echo "¿Qué versión de python 3 tienes instalada? (3.7, 3.8, 3.9, 3.10, 3.11 o 3.12)"
echo "1) 3.7"
echo "2) 3.8"
echo "3) 3.9"
echo "4) 3.10"
echo "5) 3.11"
echo "6) 3.12"
read -p "Selecciona una opción: " option
case $option in
    1)
    version=3.7
    ;;
    2)
    version=3.8
    ;;
    3)
    version=3.9
    ;;
    4)
    version=3.10
    ;;
    5)
    version=3.11
    ;;
    6)
    version=3.12
    ;;
    *)
    echo "Opción no válida"
    exit 1
    ;;
esac


echo "Instalando dependencias para $version"
pip$version install -r requirements.txt