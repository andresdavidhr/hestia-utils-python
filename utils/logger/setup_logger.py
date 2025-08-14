"""
Configuración principal del sistema de logging
"""

import logging
from pathlib import Path
from datetime import datetime

from utils.flog import flog

from .custom_logger import CustomLogger
from .handlers import HeaderFileHandler

def setup_logger(process_id=None, pintar_log=True):
    """
    Configura el logger usando logger.yaml

    Args:
        process_id: ID del proceso para incluir en el nombre del archivo
        pintar_log: Booleano para mostrar o no la traza en consola/log
    """
    # Niveles personalizados
    if not hasattr(logging, 'HEADER'):
        logging.addLevelName(25, 'HEADER')
    if not hasattr(logging, 'TITLE'):
        logging.addLevelName(26, 'TITLE')
    if not hasattr(logging, 'SALTO'):
        logging.addLevelName(28, 'SALTO')

    logger_name = "ProcessManager"
    # Eliminar el logger del manager si ya existe para forzar la clase personalizada
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]
    # Establecer la clase del logger personalizado
    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger(logger_name)
    # Limpiar handlers existentes para reconfigurar
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)

    # Formatador
    formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Console handler personalizado para HELPER
    class HelperStreamHandler(logging.StreamHandler):
        def emit(self, record):
            # Mostrar salto como línea vacía
            if record.levelname == 'SALTO':
                flog(pintar_log, "")
                return
            # Mostrar personalizados igual que los estándar
            if record.levelname in ('HEADER', 'TITLE', 'SEPARADOR'):
                msg = self.format(record)
                flog(pintar_log, msg)
                return
            super().emit(record)

    console_handler = HelperStreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Solo crear file handler si tenemos process_id y pintar_log es True
    if process_id and pintar_log:
        # Formato de fecha YYYYMMDD_HHMMSS
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = f"logs/process_{process_id}_{timestamp}.log"

        # Crear directorio
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        # File handler personalizado
        file_handler = HeaderFileHandler(
            log_file,
            backupCount=35,
            encoding='utf-8',
            process_id=process_id
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.info(f"Log iniciado para proceso {process_id}: {log_file}", pintar=pintar_log)

    return logger
