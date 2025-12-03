
import pytest
import io
import sys
import os
import glob
import time
from utils.logger import setup_logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

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
    logger.info("Esto es info", pintar=True)  # Log the info message
    logger.error("Esto es un error", pintar=True)
    logger.debug("Esto es un debug", pintar=True)
    logger.critical("Esto es un critical", pintar=True)
    logger.warning("Esto es un warning", pintar=True)
    output_true = sys.stdout.getvalue()
    sys.stdout = stdout_original
    time.sleep(1)
    logs = glob.glob(os.path.join(logs_dir, "process_TestLogger01_*.log"))
    assert logs, "No se generó el archivo de log para TestLogger"
    log_file = logs[0]
    with open(log_file, encoding="utf-8") as f:
        contenido = f.read()
        assert "Esto es un titulo" in contenido
        assert "Esto es info" in contenido, f"No se encontró 'Esto es info' en el log.\nLog:\n{contenido}"
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

def test_logger_exception_pinta_traza(tmp_path):
    logger = setup_logger("TestLogger03", True)
    logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    try:
        raise ValueError("Error de prueba para logger")
    except ValueError as e:
        logger.exception(True, f"Excepción capturada: {str(e)}")
        time.sleep(1)
        logs = glob.glob(os.path.join(logs_dir, "process_TestLogger03_*.log"))
        assert logs, "No se generó el archivo de log para la excepción"
        log_file = logs[0]
        with open(log_file, encoding="utf-8") as f:
            contenido = f.read()
        assert "Excepción capturada: Error de prueba para logger" in contenido
        assert "ValueError" in contenido or "Traceback" in contenido
        # Cerrar handlers y eliminar log
        for handler in logger.handlers:
            handler.close()
        logger.handlers.clear()
        for _ in range(3):
            try:
                os.remove(log_file)
                break
            except Exception:
                time.sleep(0.2)
        assert not os.path.exists(log_file), f"El fichero de log {log_file} no se eliminó correctamente tras excepción controlada."
    except Exception as e:
        pytest.fail(f"Excepción inesperada: {type(e)} - {e}")
