import os
from utils.flog import flog
from io import StringIO
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_flog_activo_true():
    captured = StringIO()
    sys_stdout = sys.stdout
    sys.stdout = captured
    flog(True, "mensaje de prueba")
    sys.stdout = sys_stdout
    assert captured.getvalue().strip() == "mensaje de prueba"

def test_flog_activo_false():
    captured = StringIO()
    sys_stdout = sys.stdout
    sys.stdout = captured
    flog(False, "no debe verse")
    sys.stdout = sys_stdout
    assert captured.getvalue().strip() == ""
