from time import sleep
from utils.logger import get_logger


def fsleep(seconds):
    """
    Pausa la ejecución del programa durante un tiempo específico con logging automático.
    """
    logger = get_logger()
    logger.info(f"Durmiendo durante {seconds} segundos...")
    sleep(seconds)
