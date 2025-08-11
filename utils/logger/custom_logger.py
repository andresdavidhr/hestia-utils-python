"""
Logger personalizado con métodos adicionales
"""

import logging

class CustomLogger(logging.Logger):
    """Logger personalizado con métodos header(), title(), separador() y salto()"""


    def _custom_log(self, levelname, message="", *args, **kwargs):
        level = logging.getLevelName(levelname)
        if isinstance(level, int) and self.isEnabledFor(level):
            self._log(level, message, args, **kwargs)

    def header(self, message, *args, **kwargs):
        self._custom_log('HEADER', message, *args, **kwargs)

    def title(self, message, *args, **kwargs):
        self._custom_log('TITLE', message, *args, **kwargs)

    def separador(self, *args, **kwargs):
        self._custom_log('SEPARADOR', "", *args, **kwargs)

    def salto(self, *args, **kwargs):
        self._custom_log('SALTO', "", *args, **kwargs)

def get_logger():
    """Obtiene el logger configurado"""
    return logging.getLogger("ProcessManager")