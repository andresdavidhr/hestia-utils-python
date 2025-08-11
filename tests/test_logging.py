import unittest
from utils.logging import setup_logger, get_logger

class TestLogging(unittest.TestCase):
    def test_logger_info(self):
        setup_logger()
        logger = get_logger()
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
