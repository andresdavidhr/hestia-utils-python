import os
import sys
import pytest
from utils.variables_locales import cargar_variables_locales, get_valor_variable_local, add_variable_local

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

def test_get_valor_variable_local_existente(monkeypatch):
    monkeypatch.setenv("TEST_VAR", "valor_test")
    assert get_valor_variable_local("TEST_VAR") == "valor_test"

def test_get_valor_variable_local_inexistente():
    assert get_valor_variable_local("NO_EXISTE") == ""

def test_add_variable_local():
    var_name = "TEST_VAR"
    var_value = "valor_prueba"
    add_variable_local(var_name, var_value)
    assert os.environ[var_name] == var_value
    assert get_valor_variable_local(var_name) == var_value