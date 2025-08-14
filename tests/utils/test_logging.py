import pytest
from utils.logger import setup_logger
import io
import sys
import os
import glob
import time

@pytest.fixture(autouse=True)
def limpiar_logs_residuales_fixture():
    yield
    logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    logs = glob.glob(os.path.join(logs_dir, "process_TestLogger*.log"))
    for f in logs:
        try:
            os.remove(f)
        except Exception:
            pass

def test_logger_info_true():
    logger = setup_logger("TestLogger01", True)
    logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    stdout_original = sys.stdout
    sys.stdout = io.StringIO()
    logger.title(True, "Esto es un titulo")
    logger.salto(True)
    logger.info("Esto es info", pintar=True)
    logger.error("Esto es un error", pintar=True)
    logger.debug("Esto es un debug", pintar=True)
    logger.critical("Esto es un critical", pintar=True)
    logger.warning("Esto es un warning", pintar=True)
    output_true = sys.stdout.getvalue()
    assert "Esto es un titulo" in output_true
    assert "Esto es info" in output_true
    sys.stdout = stdout_original
    time.sleep(1)
    logs = glob.glob(os.path.join(logs_dir, "process_TestLogger01_*.log"))
    assert logs, "No se generó el archivo de log para TestLogger"

def test_logger_info_false():
    logger = setup_logger("TestLogger02", False)
    logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    stdout_original = sys.stdout
    sys.stdout = io.StringIO()
    logger.title(False, "Esto es un titulo")
    logger.salto(False)
    logger.info("Esto es info", pintar=False)
    logger.error("Esto es un error", pintar=False)
    logger.debug("Esto es un debug", pintar=False)
    logger.critical("Esto es un critical", pintar=False)
    logger.warning("Esto es un warning", pintar=False)
    output_false = sys.stdout.getvalue()
    assert output_false == ""
    sys.stdout = stdout_original
    time.sleep(1)
    logs = glob.glob(os.path.join(logs_dir, "process_TestLogger02_*.log"))
    assert not logs, "Se generó el archivo de log para TestLogger cuando no debía"
