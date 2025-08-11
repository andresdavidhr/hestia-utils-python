#!/bin/bash
# Script para ejecutar todos los tests de Python del proyecto

if python3 -m unittest discover tests > /dev/null 2>&1; then
	echo OK
else
	echo ERROR
fi
