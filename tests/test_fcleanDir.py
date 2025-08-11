import os
import tempfile
import time
import shutil
import unittest
from utils.fcleanDir import fcleanDir

class TestFCleanDir(unittest.TestCase):
    def setUp(self):
        # Crear un directorio temporal para pruebas
        self.test_dir = tempfile.mkdtemp()
        # Crear archivos de diferentes edades
        self.old_file = os.path.join(self.test_dir, "old.log")
        self.new_file = os.path.join(self.test_dir, "new.log")
        with open(self.old_file, "w") as f:
            f.write("antiguo")
        with open(self.new_file, "w") as f:
            f.write("nuevo")
        # Cambiar la fecha de modificación del archivo antiguo a hace 40 días
        old_time = time.time() - (40 * 86400)
        os.utime(self.old_file, (old_time, old_time))

    def tearDown(self):
        # Eliminar el directorio temporal y su contenido
        shutil.rmtree(self.test_dir)

    def test_elimina_archivos_antiguos(self):
        # Solo debe eliminar el archivo viejo
        result = fcleanDir(self.test_dir, "*.log", diasBorrar=35)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.old_file))
        self.assertTrue(os.path.exists(self.new_file))

    def test_no_elimina_si_diasBorrar_cero(self):
        # No debe eliminar nada si diasBorrar <= 0
        result = fcleanDir(self.test_dir, "*.log", diasBorrar=0)
        self.assertFalse(result)
        self.assertTrue(os.path.exists(self.old_file))
        self.assertTrue(os.path.exists(self.new_file))

    def test_directorio_inexistente(self):
        # Si el directorio no existe, debe devolver False
        result = fcleanDir("/ruta/que/no/existe", "*.log", diasBorrar=35)
        self.assertFalse(result)

    def test_patron_no_coincide(self):
        # Si el patrón no coincide, no debe eliminar nada
        result = fcleanDir(self.test_dir, "*.txt", diasBorrar=35)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.old_file))
        self.assertTrue(os.path.exists(self.new_file))

if __name__ == "__main__":
    unittest.main()