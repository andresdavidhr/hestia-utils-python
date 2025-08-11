import unittest
from utils.flog import flog
from io import StringIO
import sys

class TestFlog(unittest.TestCase):
    def test_flog_activo_true(self):
        captured = StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured
        flog(True, "mensaje de prueba")
        sys.stdout = sys_stdout
        self.assertEqual(captured.getvalue().strip(), "mensaje de prueba")

    def test_flog_activo_false(self):
        captured = StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured
        flog(False, "no debe verse")
        sys.stdout = sys_stdout
        self.assertEqual(captured.getvalue().strip(), "")

if __name__ == "__main__":
    unittest.main()
