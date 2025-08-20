import os
import sys
import pytest
from utils.cargar_variables_locales import cargar_variables_locales

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_carga_variables_locales():
    variables = cargar_variables_locales()
    # Validar variable de prueba
    assert 'PRUEBA' in variables
    assert variables['PRUEBA'] == 'testPrueba'
    # Validar que GOOGLE_REPORTING_CLIENT_EMAIL también se carga
    assert 'GOOGLE_REPORTING_CLIENT_EMAIL' in variables
    # Solo validar que la variable de password existe, sin mostrar su valor
    assert 'POSTGRES_MICRO_PA_CEM_PASSWORD' in variables
