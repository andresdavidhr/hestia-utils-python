import unittest
from utils.logger import setup_logger

class TestLogging(unittest.TestCase):
    def test_logger_info(self):
        logger = setup_logger(f"Iniciando proceso Prueba")
        try:
            # - Loggers personalizados
            logger.title("Esto es un titulo")
            logger.salto()
            # - Loggers por defecto
            logger.info("Esto es info")
            logger.error("Esto es un error")
            logger.debug("Esto es un debug")
            logger.critical("Esto es un critical")
            logger.warning("Esto es un warning")

        except Exception as e:
            self.fail(f"Logger lanzó una excepción: {e}")

if __name__ == "__main__":
    unittest.main()
