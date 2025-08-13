import os
import tempfile
import time
import shutil
import pytest
from utils.fcleanDir import fcleanDir

@pytest.fixture
def test_dir():
    dirpath = tempfile.mkdtemp()
    old_file = os.path.join(dirpath, "old.log")
    new_file = os.path.join(dirpath, "new.log")
    with open(old_file, "w") as f:
        f.write("antiguo")
    with open(new_file, "w") as f:
        f.write("nuevo")
    # Cambiar la fecha de modificación del archivo antiguo a hace 40 días
    old_time = time.time() - (40 * 86400)
    os.utime(old_file, (old_time, old_time))
    yield dirpath, old_file, new_file
    # Eliminar el directorio temporal y su contenido
    shutil.rmtree(dirpath)

def test_elimina_archivos_antiguos(test_dir):
    dirpath, old_file, new_file = test_dir
    # Solo debe eliminar el archivo viejo
    result = fcleanDir(dirpath, "*.log", diasBorrar=35)
    assert result
    assert not os.path.exists(old_file)
    assert os.path.exists(new_file)

def test_no_elimina_si_diasBorrar_cero(test_dir):
    dirpath, old_file, new_file = test_dir
    # No debe eliminar nada si diasBorrar <= 0
    result = fcleanDir(dirpath, "*.log", diasBorrar=0)
    assert not result
    assert os.path.exists(old_file)
    assert os.path.exists(new_file)

def test_directorio_inexistente():
    # Si el directorio no existe, debe devolver False
    result = fcleanDir("/ruta/que/no/existe", "*.log", diasBorrar=35)
    assert not result

def test_patron_no_coincide(test_dir):
    dirpath, old_file, new_file = test_dir
    # Si el patrón no coincide, no debe eliminar nada
    result = fcleanDir(dirpath, "*.txt", diasBorrar=35)
    assert result
    assert os.path.exists(old_file)
    assert os.path.exists(new_file)