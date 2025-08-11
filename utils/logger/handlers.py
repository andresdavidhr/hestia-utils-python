"""
Handlers personalizados para el sistema de logging
"""

from logging.handlers import RotatingFileHandler

from utils.flog import flog

from .helpers.separador import create_separador
from .helpers.header import create_header
from .helpers.title import create_title

class HeaderFileHandler(RotatingFileHandler):
    """Handler personalizado que detecta cuando escribir encabezado y maneja niveles custom"""

    def __init__(self, *args, **kwargs):
        self.process_id = kwargs.pop('process_id', None)
        self.header_written = False
        super().__init__(*args, **kwargs)


    def emit(self, record):
        # Diccionario de funciones para cada nivel
        custom_actions = {
            'HEADER': self._write_header,
            'TITLE': lambda r: self._write_text(create_title(r.getMessage())),
            'SEPARADOR': lambda r: self._write_text(create_separador()),
            'SALTO': lambda r: self._write_text(""),  # Solo un salto de línea
        }
        action = custom_actions.get(record.levelname)
        if action:
            action(record)
            return
        super().emit(record)

    def _write_text(self, text):
        # Si text es vacío, solo un salto de línea
        if text == "":
            with open(self.baseFilename, 'a', encoding='utf-8') as f:
                f.write("\n")
            flog("")
        else:
            with open(self.baseFilename, 'a', encoding='utf-8') as f:
                f.write(text + "\n")
            flog(text)

    def _write_header(self, record):
        if not self.header_written and self.process_id:
            header_text = create_header(self.process_id)
            with open(self.baseFilename, 'w', encoding='utf-8') as f:
                f.write(header_text + "\n")
            flog(header_text)
            self.header_written = True
            # Escribir encabezado directamente
            with open(self.baseFilename, 'w', encoding='utf-8') as f:
                f.write(header_text + "\n")