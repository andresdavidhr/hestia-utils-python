"""
Logger personalizado con métodos adicionales
"""

import logging
from utils.flog import flog

class CustomLogger(logging.Logger):
    """Logger personalizado """

    def _custom_log(self, levelname, pintar, message="", *args, **kwargs):
        level = logging.getLevelName(levelname)
        if pintar:
            if isinstance(level, int) and self.isEnabledFor(level):
                self._log(level, message, args, **kwargs)
                flog(pintar, message)
        # Si pintar es False, no hace nada (ni log, ni flog)

    def header(self, pintar, message, *args, **kwargs):
        self._custom_log('HEADER', pintar, message, *args, **kwargs)

    def title(self, pintar, message, *args, **kwargs):
        self._custom_log('TITLE', pintar, message, *args, **kwargs)

    def separador(self, pintar, *args, **kwargs):
        self._custom_log('SEPARADOR', pintar, "", *args, **kwargs)

    def salto(self, pintar, *args, **kwargs):
        self._custom_log('SALTO', pintar, "", *args, **kwargs)

    def info(self, pintar, message, *args, **kwargs):
        if pintar:
            super().info(message, *args, **kwargs)
            flog(pintar, message)

    def error(self, pintar, message, *args, **kwargs):
        if pintar:
            super().error(message, *args, **kwargs)
            flog(pintar, message)

    def debug(self, pintar, message, *args, **kwargs):
        if pintar:
            super().debug(message, *args, **kwargs)
            flog(pintar, message)

    def critical(self, pintar, message, *args, **kwargs):
        if pintar:
            super().critical(message, *args, **kwargs)
            flog(pintar, message)

    def warning(self, pintar, message, *args, **kwargs):
        if pintar:
            super().warning(message, *args, **kwargs)
            flog(pintar, message)

    def exception(self, pintar, message, *args, **kwargs):
        if pintar:
            super().exception(message, *args, **kwargs)
            flog(pintar, message)

def get_logger():
    """Obtiene el logger configurado"""
    return logging.getLogger("ProcessManager")