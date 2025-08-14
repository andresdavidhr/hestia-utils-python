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

    def info(self, message, *args, pintar=True, **kwargs):
        if pintar:
            super().info(message, *args, **kwargs)
            flog(pintar, message)
        else:
            super().info(message, *args, **kwargs)

    def error(self, message, *args, pintar=True, **kwargs):
        if pintar:
            super().error(message, *args, **kwargs)
            flog(pintar, message)
        else:
            super().error(message, *args, **kwargs)

    def debug(self, message, *args, pintar=True, **kwargs):
        if pintar:
            super().debug(message, *args, **kwargs)
            flog(pintar, message)
        else:
            super().debug(message, *args, **kwargs)

    def critical(self, message, *args, pintar=True, **kwargs):
        if pintar:
            super().critical(message, *args, **kwargs)
            flog(pintar, message)
        else:
            super().critical(message, *args, **kwargs)

    def warning(self, message, *args, pintar=True, **kwargs):
        if pintar:
            super().warning(message, *args, **kwargs)
            flog(pintar, message)
        else:
            super().warning(message, *args, **kwargs)

    def exception(self, pintar=True, message=None, *args, **kwargs):
        """
        Pinta la excepción y el traceback en el log y por pantalla.
        Compatible con la llamada estándar.
        """
        import traceback
        if message is None and args:
            message = args[0]
            args = args[1:]
        tb = traceback.format_exc()
        if pintar:
            super().exception(message, *args, **kwargs)
            self.error(f"EXCEPCIÓN: {message}\n{tb}", pintar=pintar)
            flog(pintar, f"EXCEPCIÓN: {message}")
            flog(pintar, tb)
        else:
            super().exception(message, *args, **kwargs)

def get_logger():
    """Obtiene el logger configurado"""
    return logging.getLogger("ProcessManager")