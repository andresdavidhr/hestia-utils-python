"""
Módulo de logging personalizado para MSTR_STARDUST
"""

from .setup_logger import setup_logger
from .custom_logger import get_logger, get_fichero_log

# Exportar lo que necesiten otros módulos
__all__ = ['setup_logger', 'get_logger', 'get_fichero_log']

# Mantener compatibilidad con imports existentes
logger = None  # Se inicializará cuando se llame setup_logger

# Re-exportar para compatibilidad con código existente que usa:
# from utils.logger import setup_logger, get_logger