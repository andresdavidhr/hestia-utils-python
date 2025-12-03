
import os
import sys
import subprocess
from utils.fconvert import convert_crlf_to_lf

TESTS_LIST = [
    'tests/test_dependencias.py',
    'tests/test_estructura.py',
    'tests/utils',
    'tests/models',
    'tests/controllers',
    'tests/metadata',
    'tests/test_main.py'
]

if __name__ == "__main__":
    total = len(TESTS_LIST)
    print(f"Realizamos conversión de ficheros a LF en {os.path.dirname(__file__)}")
    convert_crlf_to_lf(os.path.dirname(__file__))
     
    print(f"Se van a ejecutar {total} conjuntos de tests.")
    for idx, test_path in enumerate(TESTS_LIST, 1):
        print(f"[{idx}/{total}] - Revisión de {test_path}")
        result = subprocess.run([sys.executable, '-m', 'pytest', test_path], cwd=os.path.dirname(__file__))
        if result.returncode != 0:
            print(f"ERROR - No ha pasado las pruebas de {test_path}.")
            sys.exit(result.returncode)
