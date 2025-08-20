#!/bin/bash
# Script para ejecutar todos los tests de Python del proyecto

export PYTHONPATH=$(pwd)

TESTS_LIST=(tests/test_estructura.py tests/utils)
COUNT=1
TOTAL=${#TESTS_LIST[@]}

for TEST in "${TESTS_LIST[@]}"; do
    echo "[$COUNT/$TOTAL] - Revisión de $TEST"
    pytest "$TEST"
    if [ $? -ne 0 ]; then
        echo "ERROR - No ha pasado las pruebas de $TEST."
        exit 1
    fi
    COUNT=$((COUNT+1))
done
