"""
Logger personalizado con métodos adicionales
"""

import logging

class CustomLogger(logging.Logger):
    """Logger personalizado con métodos header(), title(), helper() y separador()"""

    def header(self, message, *args, **kwargs):
        """Método personalizado para crear encabezado + log"""
        if self.isEnabledFor(25):  # Nivel HEADER
            self._log(25, message, args, **kwargs)
    
    def title(self, message, *args, **kwargs):
        """Método personalizado para crear título con líneas"""
        if self.isEnabledFor(26):  # Nivel TITLE
            self._log(26, message, args, **kwargs)
    
    def helper(self, *args, **kwargs):
        """Método personalizado para mostrar ayuda del logger"""
        if self.isEnabledFor(27):  # Nivel HELPER
            self._log(27, "AYUDA DEL LOGGER", args, **kwargs)

    def separador(self, *args, **kwargs):
        """Método personalizado para mostrar un separador"""
        if self.isEnabledFor(27):  # Nivel SEPARADOR
            self._log(27, "", args, **kwargs)




def get_logger():
    """Obtiene el logger configurado"""
    return logging.getLogger("ProcessManager")