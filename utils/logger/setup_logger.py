"""
Configuración principal del sistema de logging
"""

import logging
from pathlib import Path
from datetime import datetime

from utils.flog import flog

from .config import load_config
from .custom_logger import CustomLogger
from .handlers import HeaderFileHandler

def setup_logger(process_id=None):
    """
    Configura el logger usando logger.yaml

    Args:
        process_id: ID del proceso para incluir en el nombre del archivo
    """
    config = load_config()
    log_config = config['logging']


    logger_name = "ProcessManager"

    # Eliminar el logger del manager si ya existe para forzar la clase personalizada
    if logger_name in logging.Logger.manager.loggerDict:
        del logging.Logger.manager.loggerDict[logger_name]

    # Establecer la clase del logger personalizado
    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger(logger_name)

    # Agregar los niveles personalizados si no existen
    if not hasattr(logging, 'HEADER'):
        logging.addLevelName(25, 'HEADER')  # Entre INFO (20) y WARNING (30)
    if not hasattr(logging, 'TITLE'):
        logging.addLevelName(26, 'TITLE')   # Entre HEADER (25) y WARNING (30)
    if not hasattr(logging, 'HELPER'):
        logging.addLevelName(27, 'HELPER')  # Entre TITLE (26) y WARNING (30)
    if not hasattr(logging, 'SALTO'):
        logging.addLevelName(28, 'SALTO')   # Nivel para salto de línea

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
                flog("")
                return
            # Mostrar personalizados igual que los estándar
            if record.levelname in ('HEADER', 'TITLE', 'SEPARADOR'):
                msg = self.format(record)
                flog(msg)
                return
            # Mostrar todos los niveles personalizados
            if record.levelno >= 25 and record.levelname not in ('INFO','WARNING','ERROR','DEBUG','CRITICAL'):
                msg = self.format(record)
                flog(msg)
                return
            super().emit(record)

    console_handler = HelperStreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Solo crear file handler si tenemos process_id
    if process_id:
        # Formato de fecha YYYYMMDD_HHMMSS
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = f"logs/process_{process_id}_{timestamp}.log"

        # Crear directorio
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        # File handler personalizado
        backup_count = log_config.get('backup_count', 35)
        file_handler = HeaderFileHandler(
            log_file,
            backupCount=backup_count,
            encoding='utf-8',
            process_id=process_id
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.info(f"Log iniciado para proceso {process_id}: {log_file}")

    return logger
