from utils.flog import flog
from io import StringIO
import sys

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
